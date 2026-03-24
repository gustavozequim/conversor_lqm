import os
from pathlib import Path
import shutil
from dotenv import load_dotenv
from extrai_arquivos import extrai_arquivos
from salva_arquivos import salva_arquivos
from pathlib import Path
import os


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

    extrai_arquivos(pasta_raiz)

    salva_arquivos(caminho_imagem, caminho_txt, contagem)

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
