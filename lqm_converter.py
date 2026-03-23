import os
import cv2
import pytesseract
from pathlib import Path
import shutil
from zipfile import ZipFile
from dotenv import load_dotenv
load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('CAMINHO_TSERACT')

def converte_lqm():
    contagem = -2
    pasta_raiz = Path('./')
    print(pasta_raiz)
    caminho_imagem = Path('./images')
    caminho_txt = Path('./txt')
    caminho_txt.mkdir(exist_ok=True)
    print(contagem)
    for raiz, pastas, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if arquivo.endswith('.txt'):
                contagem += 1
            print(arquivo)

    for raiz, pastas, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if arquivo.endswith('.lqm'):
                with ZipFile(arquivo, 'r') as zip_in:
                    zip_in.extractall()
            elif arquivo.endswith('.zip'):
                with ZipFile(arquivo, 'r') as zip_out:
                    zip_out.extractall()

    if caminho_imagem.exists():
        if Path(f"{caminho_txt}/{contagem}.txt").exists():
            contagem += 1
        for raiz, pastas, arquivos in os.walk(caminho_imagem):
            print(f"Diretório atual: {raiz}")
            for arquivo in arquivos:
                contagem += 1
                if arquivo.endswith('.jpg'):
                    imagem = cv2.imread(f"{caminho_imagem}/{arquivo}")
                    texto = pytesseract.image_to_string(imagem)
                    print(f"Texto extraído da imagem: {texto}")
                    with open(f"{caminho_txt}/{contagem}.txt", 'wb') as arquivo_texto:
                        arquivo_texto.write(texto.encode('utf-8'))
                        arquivo_texto.close()
    try:
        print("Removendo arquivos temporários...")    
        shutil.rmtree(caminho_imagem)
        shutil.rmtree(f"{pasta_raiz}/audios")
        shutil.rmtree(f"{pasta_raiz}/drawings")
        shutil.rmtree(f"{pasta_raiz}/videos")
        os.remove(f"{pasta_raiz}/memoinfo.jlqm")
        os.remove(f"{pasta_raiz}/metadata.mtd")
        print("Processo concluído!")
    except Exception as e:
        print(f"Erro ao remover arquivos temporários: {e}")

if __name__ == "__main__":
    converte_lqm()
