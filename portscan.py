import socket
import sys

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW  = '\033[33m'

quantidadePortasAbertas = 0

if (len(sys.argv) != 2):
    print(f"{RED}Modo de uso: python3 portscan.py <ip>")

else:
    print(f'{YELLOW}=> Iniciando scan no host {sys.argv[1]} nas 65535 portas')
    for porta in range(1, 65535):
        meuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if meuSocket.connect_ex((sys.argv[1], porta)) == 0: # conect ex retorna 0 se a conexão funcionou
            print(f"{GREEN}[!] Porta {porta} aberta [!]")
            quantidadePortasAbertas = 1     

if quantidadePortasAbertas == 0:
    print(f'{RED}[!] Nenhuma porta aberta foi encontrada no alvo [!]')

print(f'{GREEN}Scan finalizado!')  