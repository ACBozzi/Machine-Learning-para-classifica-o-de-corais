#percorredor.py
import os # módulo tem relação com seu sistema operacional
#import subprocess # módulo tem relação com os comandos deste sistema
from os.path import splitext

pastaRaiz = '.'

caminho = os.path.abspath(pastaRaiz) # guarda o caminho absoluto da pasta atual do programa. Seria interessante pegar como entrada!

arquivosImagem = [] # uma lista com todas as imagens (começa vazia) [vai ser guardado o caminho absoluto]
arquivosTxt = [] # lista com todos os txts (vazia) [same]

# o os.walk devolve
# raiz = conem a raiz, ou seja "onde está" na iteração
# diretorios = contem uma lista com todas os diretorios da raiz na iteração
# arquivos = contém uma lista com todos os arquivos na da raiz na iteração
# topdown true = vai percorrer de baixo pra cima
for (raiz, diretorios, arquivos) in os.walk(caminho, topdown=True):
    arquivosImagem.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.png') or arquivo.endswith('.jpg')])
    arquivosTxt.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.txt')])


print("Todos os arquivos de imagens:")
print(arquivosImagem)
print("\n\n Todos os arquivos de texto:")
print(arquivosTxt)

# cria um conjunto, cortando o texto. Documentos contém o nomes dos txt, sem o .txt
documentos = set([splitext(filename)[0] for filename in arquivosTxt])

# Compara a lista "documentos" com a lista arquivosImg que vai ser divida, se elas não estiverem nas duas, vai entrar pra lista semTXT
semTxt = [filename for filename in set(arquivosImagem) if splitext(filename)[0] not in documentos]

print("\n\nATENÇÃO: As seguintes imagens não tem TXT:")
print (semTxt)
