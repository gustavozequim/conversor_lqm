from pathlib import Path
import os
import cv2
import pytesseract
from dotenv import load_dotenv
load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('CAMINHO_TSERACT') # Caminho do executável do Tesseract



def salva_arquivos(caminho_imagem, caminho_txt, contagem):
    if caminho_imagem.exists(): # Verificando se o diretório de imagens existe
        if Path(f"{caminho_txt}/{contagem}.txt").exists():
            contagem += 1
        for raiz, pastas, arquivos in os.walk(caminho_imagem): # Processando arquivos de imagem
            print(f"Diretório atual: {raiz}")
            for arquivo in arquivos:
                contagem += 1
                print(f"Processando arquivo: {contagem}.txt")
                if arquivo.endswith('.jpg'):
                    imagem = cv2.imread(f"{caminho_imagem}/{arquivo}")
                    texto = pytesseract.image_to_string(imagem)
                    with open(f"{caminho_txt}/{contagem}.txt", 'w') as arquivo_texto: # Salvando o texto extraído em um arquivo .txt
                        arquivo_texto.write(texto)
                        arquivo_texto.close()