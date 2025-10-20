#!/usr/bin/env python3
import PySimpleGUI as sg
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

# Funções
def parse_ports(ports_arg: str) -> List[int]:
    ports: List[int] = []
    for part in ports_arg.split(","):
        part = part.strip()
        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start, end = int(start_str), int(end_str)
            ports.extend(range(min(start, end), max(start, end) + 1))
        else:
            ports.append(int(part))
    return sorted(set(p for p in ports if 1 <= p <= 65535))

def check_port(host: str, port: int, timeout: float):
    start = time.perf_counter()
    err_msg = ""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            ok = True
    except Exception as e:
        ok = False
        err_msg = str(e)
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    return port, ok, elapsed_ms, err_msg

def resolve_host(host: str) -> str:
    try:
        return socket.gethostbyname(host)
    except Exception:
        return ""

#GUI
layout = [
    [sg.Text("Host/IP:"), sg.Input(key="-HOST-")],
    [sg.Text("Portas (ex.: 22,80,8000-8010):"), sg.Input(key="-PORTS-")],
    [sg.Text("Timeout (s):"), sg.Input("3", size=(5,1), key="-TIMEOUT-")],
    [sg.Text("Threads:"), sg.Input("50", size=(5,1), key="-THREADS-")],
    [sg.Button("Testar"), sg.Button("Sair")],
    [sg.Multiline(size=(70,20), key="-OUTPUT-", autoscroll=True)]
]

window = sg.Window("Teste de Portas TCP (GUI)", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Testar":
        host = values["-HOST-"].strip()
        ports_input = values["-PORTS-"].strip()
        try:
            timeout = float(values["-TIMEOUT-"])
        except ValueError:
            timeout = 3.0
        try:
            threads = int(values["-THREADS-"])
        except ValueError:
            threads = 50

        if not host or not ports_input:
            sg.popup("Por favor, preencha Host/IP e Portas!")
            continue

        ports = parse_ports(ports_input)
        if not ports:
            sg.popup("Nenhuma porta válida foi informada!")
            continue

        ip = resolve_host(host)
        window["-OUTPUT-"].update("")  # limpa output
        if ip:
            window["-OUTPUT-"].print(f"Testando {host} ({ip}) - {len(ports)} porta(s), timeout {timeout}s, threads {threads}\n")
        else:
            window["-OUTPUT-"].print(f"Testando {host} - {len(ports)} porta(s), timeout {timeout}s, threads {threads}\n")

        results = []
        max_threads = min(threads, len(ports))
        with ThreadPoolExecutor(max_workers=max_threads) as exe:
            future_to_port = {exe.submit(check_port, host, p, timeout): p for p in ports}
            for fut in as_completed(future_to_port):
                port_num, ok, elapsed_ms, err = fut.result()
                status = "OPEN " if ok else "CLOSED"
                line = f"{host}:{port_num:>5}  {status}  {elapsed_ms:7.2f} ms" + (f"  ({err})" if (not ok and err) else "")
                window["-OUTPUT-"].print(line)
                results.append((port_num, ok))

        # Resumo final
        open_ports = [p for p, ok in results if ok]
        window["-OUTPUT-"].print("\n=== Resumo ===")
        window["-OUTPUT-"].print(f"Total testadas: {len(results)}")
        window["-OUTPUT-"].print(f"Abertas: {len(open_ports)} -> {', '.join(map(str, open_ports)) if open_ports else 'Nenhuma'}")
        window["-OUTPUT-"].print("Fim do teste.\n")

window.close()
