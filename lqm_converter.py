import os
import cv2
import pytesseract
from pathlib import Path
import shutil
from zipfile import ZipFile
from dotenv import load_dotenv
load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('CAMINHO_TSERACT') # Caminho do executável do Tesseract

def converte_lqm():
    contagem = -2
    pasta_raiz = os.getenv('CAMINHO_NOTAS_LG')
    caminho_imagem = Path('./images')
    caminho_txt = Path(f'./txt')
    caminho_txt.mkdir(exist_ok=True)
    for raiz, pastas, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if arquivo.endswith('.txt'):
                contagem += 1

    for raiz, pastas, arquivos in os.walk(pasta_raiz): # Procurando por arquivos .lqm e .zip
        for arquivo in arquivos:
            if not arquivo.endswith('.lqm') and not arquivo.endswith('.zip'): # Verificando se há arquivos para processar
                print(f"Não há arquivos para serem processados no diretório.")
                continue
            if arquivo.endswith('.lqm'): # Extraindo arquivos .lqm
                with ZipFile(arquivo, 'r') as zip_in:
                    zip_in.extractall()
            elif arquivo.endswith('.zip'): # Extraindo arquivos .zip
                with ZipFile(arquivo, 'r') as zip_out:
                    zip_out.extractall()
            else: # Ignorando arquivos que não são .lqm ou .zip
                print(f"Arquivo {arquivo} não é um arquivo .lqm ou .zip, ignorando.")
                continue

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
                    with open(f"{caminho_txt}/{contagem}.txt", 'wb') as arquivo_texto: # Salvando o texto extraído em um arquivo .txt
                        arquivo_texto.write(texto.encode('utf-8'))
                        arquivo_texto.close()
    
    print("Processamento de imagens concluído!")
    try: # Removendo pastas e arquivos temporários
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
        return

if __name__ == "__main__":
    converte_lqm()
