# CONVERSOR LQM PARA TXT

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
