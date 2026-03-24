from zipfile import ZipFile
import os


def extrai_arquivos(pasta_raiz):
    for raiz, pastas, arquivos in os.walk(pasta_raiz): # Procurando por arquivos .lqm e .zip
        for arquivo in arquivos:
            if not arquivo.endswith('.lqm') and not arquivo.endswith('.zip'): # Verificando se há arquivos para processar
                continue
            if arquivo.endswith('.lqm'): # Extraindo arquivos .lqm
                with ZipFile(f'{raiz}/{arquivo}', 'r') as zip_in:
                    zip_in.extractall()
            elif arquivo.endswith('.zip'): # Extraindo arquivos .zip
                with ZipFile(f'{raiz}/{arquivo}', 'r') as zip_out:
                    zip_out.extractall()
            else: # Ignorando arquivos que não são .lqm ou .zip
                print(f"Arquivo {arquivo} não é um arquivo .lqm ou .zip, ignorando.")
                continue

