# CONVERSOR LQM PARA TXT
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-green)

## O QUE É O .LQM?:
  -  Arquivos .lqm são notas criadas pelo aplicativo QuickMemo+ em dispositivos LG, geralmente contendo texto e imagens comprimidas em formato .zip
## Objetivo:
  - O objetivo desse script é simples, ele fará a conversão dos arquivos .lqm para arquivos .txt na pasta indicada.

## Como funciona:
  - Os arquivos .lqm vem como um .zip, o script extrai esse .zip.
  - Dentro desse .zip, existem outras pastas, mas a pasta que nos interessa é a "/images/";
  - Dentro dessa pasta (em todos os testes que fiz), contém arquivos de imagens com o texto escrito;
  - O script localiza essa imagem (sendo uma imagem por arquivo .zip), e faz a leitura do texto ali contido;
  - Em seguida, armazena esse texto em uma variável e, posteriormente, o salva em um arquivo .txt.

# Estrutura
```
conversor_lqm\
  L .gitignore
  L lqm_converter.py
  L README.md
```
## Utilização:
  - Para utilizar, clone o projeto no seu PC:
  ```
    - git clone https://github.com/gustavozequim/conversor_lqm
  ```
  - Em seguida, instale o requirements.txt:
  ```
    - pip install -r requirements.txt
  ```
  - Execute:
  ```
    - python .\lqm_converter.py
  ```
  Assim, o script irá percorrer o diretório atual e até encontrar uma arquivo .zip, extrair ele, procurar a pasta de "images/", e extrair o texto da imagem presente nesta pasta.