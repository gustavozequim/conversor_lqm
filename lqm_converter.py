import os
import cv2
import pytesseract
from pathlib import Path
from zipfile import ZipFile
from dotenv import load_dotenv
load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('CAMINHO_TSERACT')

def converte_lqm():
    contagem = 0
    pasta = Path('./')
    print(pasta)
    caminho_imagem = Path('./images')
    caminho_txt = Path('./txt')
    caminho_txt.mkdir(exist_ok=True)
    print(contagem)
    for raiz, pastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.endswith('.txt'):
                contagem += 1

    for raiz, pastas, arquivos in os.walk(pasta):
        if raiz == ".\.git":
            continue
        for arquivo in arquivos:
            if arquivo.endswith('.zip'):
                with ZipFile(arquivo, 'r') as zip_out:
                    zip_out.extractall()
              
    if caminho_imagem.exists():
        if contagem != 0:
            pass
        else:
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
