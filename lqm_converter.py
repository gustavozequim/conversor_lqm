import os
import cv2
import pytesseract
from pathlib import Path
from zipfile import ZipFile

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\158666389\Desktop\tseract\tesseract.exe'

def converte_lqm():
    contagem = 0
    pasta = Path('./')
    caminho_imagem = Path('./images')
    caminho_txt = Path('./txt')
    caminho_txt.mkdir(exist_ok=True)

    for raiz, pastas, arquivos in os.walk(pasta):
        print(f"Diretório atual: {raiz}")
    for arquivo in arquivos:
        print(f" - Arquivo: {os.path.join(raiz, arquivo)}")
        if arquivo.endswith('.zip'):
            with ZipFile(arquivo, 'r') as zip_out:
                zip_out.extractall()
              
    if caminho_imagem.exists():
        contagem += 1
        print('blz')
        for raiz, pastas, arquivos in os.walk(caminho_imagem):
            print(f"Diretório atual: {raiz}")
        for arquivo in arquivos:
            print(f" - Arquivo: {os.path.join(raiz, arquivo)}")
            if arquivo.endswith('.jpg'):
                imagem = cv2.imread(f"{caminho_imagem}/{arquivo}")
                texto = pytesseract.image_to_string(imagem)
                print(f"Texto extraído da imagem: {texto}")
                with open(f"{caminho_txt}/{contagem}.txt", 'w') as arquivo_texto:
                    arquivo_texto.write(texto)
        
                

if __name__ == "__main__":
    converte_lqm()
