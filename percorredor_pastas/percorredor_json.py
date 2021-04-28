#percorredor.py
import os # módulo tem relação com seu sistema operacional
#import subprocess # módulo tem relação com os comandos deste sistema
from os.path import splitext
import sys

def findAnnotatedImagesPath (root_folder, print_missing = False):

	caminho = os.path.abspath(root_folder)
	# guarda o caminho absoluto da pasta atual do programa. Seria interessante pegar como entrada!

	arquivosImagem = [] # uma lista com todas as imagens (começa vazia) [vai ser guardado o caminho absoluto]
	arquivosJson = [] # lista com todos os jsons (vazia) [same]

	# o os.walk devolve:
	# raiz = conem a raiz, ou seja "onde está" na iteração
	# diretorios = contem uma lista com todas os diretorios da raiz na iteração
	# arquivos = contém uma lista com todos os arquivos na da raiz na iteração
	# topdown true = vai percorrer de baixo pra cima
	for (raiz, diretorios, arquivos) in os.walk(caminho, topdown=True):
	    arquivosImagem.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.png') or arquivo.endswith('.jpg') or arquivo.endswith('.JPG') or arquivo.endswith('.PNG') ])
	    arquivosJson.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.json')])

	# cria um conjunto, cortando o texto. Documentos contém o nomes dos txt, sem o .txt
	documentos = set([splitext(filename)[0] for filename in arquivosJson])

	annotated = [filename for filename in set(arquivosImagem) if splitext(filename)[0] in documentos]

	if (print_missing):
		# Compara a lista "documentos" com a lista arquivosImg que vai ser divida, se elas não estiverem nas duas, vai entrar pra lista semTXT
		semJson = [filename for filename in set(arquivosImagem) if splitext(filename)[0] not in documentos]
		print("\n\nATENÇÃO: As seguintes imagens não tem JSON:\n", semJson)
		print("\n\n Total: ", len(semJson))

	return annotated

#root = sys.argv[1]
#annotated = findAnnotatedImagesPath(root)
#print(annotated, len(annotated))