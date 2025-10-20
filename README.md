# TCP-Port-Scanner-GUI

Aplicativo Python simples e rápido para testar portas TCP, com interface gráfica feita em **PySimpleGUI**.  
Permite escanear portas individuais ou ranges, visualizar resultados em tempo real e obter um resumo das portas abertas.

---

## 🔹 Funcionalidades

- Teste de portas TCP individuais ou em ranges (ex.: `22,80,443` ou `20-25,80,443`)
- Multithread para acelerar o teste
- Interface gráfica **simples e intuitiva** com PySimpleGUI
- Resultados exibidos em tempo real
- Tabela organizada mostrando:
  - Porta
  - Status (OPEN / CLOSED)
  - Tempo de resposta (ms)
  - Mensagem de erro, se houver
- Resumo final com total de portas testadas e portas abertas

---

## 🔹 Instalação

1. Certifique-se de ter **Python 3.8+** instalado.
2. Instale a dependência necessária:

``
python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
``
3. Clone o repositório:

git clone https://github.com/SEU_USUARIO/TCP-Port-Scanner-GUI.git
cd TCP-Port-Scanner-GUI

## Como usar

1. Execute o script: 

python telnet_port_check_gui.py

Preencha os campos na interface:

Host/IP: o endereço que deseja testar (ex.: 192.168.0.1 ou google.com)

Portas: lista de portas ou ranges (ex.: 22,80,443 ou 20-25,80)

Timeout: tempo máximo de espera por porta (em segundos)

Threads: número de portas testadas simultaneamente

3. Clique em Testar.

4. A tabela exibirá o status de cada porta em tempo real.

5. Ao final, um resumo das portas abertas aparecerá automaticamente.


🔹 Exemplo de uso

Após o teste, a tabela mostra portas abertas em verde e fechadas em vermelho, com tempo de resposta e mensagens de erro.

Resumo final exibido ao terminar:

Total portas testadas: 10
Portas abertas: 22, 80


🔹 Estrutura do projeto
TCP-Port-Scanner-GUI/
│
├─ telnet_port_check_gui.py   # Script principal
├─ screenshot.png             # Print da aplicação (opcional)
├─ README.md                  # Este arquivo
└─ .gitignore                 # Ignorar __pycache__ e arquivos temporários


🔹 Observações

PySimpleGUI foi escolhido pela simplicidade e facilidade de manter a interface leve.

Multithreading ajuda a reduzir o tempo total do scan, especialmente em grandes ranges de portas.

Este projeto é educacional, use de forma ética e somente em redes que você tem permissão para testar.


---

Se você quiser, posso **melhorar ainda mais o README** incluindo:

- Links rápidos para instalação do Python  
- Um **GIF animado** mostrando a interface funcionando  
- Destaque visual para comandos no terminal  

Quer que eu faça essa versão “premium” do README também?
