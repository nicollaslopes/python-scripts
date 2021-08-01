import requests
from sys import argv
import re
from time import sleep

GREEN = '\033[92m'
RED = '\033[91m'

print(f'{RED}!-' * 50)
print("Modo de uso: python3 sitemap.py <full-url/sitemap.xml>")
print(f'!-' * 50)

url = argv[1]

req = requests.get(url)

result = req.text

m = re.search("<loc>", result)

def retirar_tags(linha):
    linha = linha.replace("<loc>", "")
    linha = linha.replace("</loc>", "")
    linha = linha.replace("<url>", "")
    linha = linha.replace("</url>", "")

def salvar_arquivo():
    arquivo = open('sitemap.txt', "w")
    arquivo.write(result)

# a url do diretório fica entre as tagas <loc> e </loc>
def verificar_linha():
    arquivo = open('sitemap.txt', 'r')
    for linha in arquivo:
        if '<loc>' in linha:
            linha = linha.replace("<loc>", "")
            linha = linha.replace("</loc>", "")
            print(f'{GREEN} Diretório encontrado -> {RED}{linha}')
            sleep(0.02)

def main():
    if(len(argv) != 2):
        print(f'{RED}!-' * 50)
        print(f'Argumentos inválidos! Modo de uso: python3 sitemap.py <url/sitemap.xml>')   
        print(f'!-' * 50)

    else:
        salvar_arquivo()    
        verificar_linha()


if __name__ == "__main__":
    main()


