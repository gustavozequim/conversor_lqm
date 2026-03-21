import os

def detecta_arquivo(pasta, extensao):
    for raiz, pastas, arquivos in os.walk(pasta):
            print(f"Diretório atual: {raiz}")
    for arquivo in arquivos:
        print(f" - Arquivo: {os.path.join(raiz, arquivo)}")