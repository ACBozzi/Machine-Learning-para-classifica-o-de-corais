import random
import os, glob
import os


home = '/home/carol/Área de Trabalho/ML/Trabalhao/Balanceado/150x150/SE'

for (pastaAtual, subpastas, arquivos) in os.walk(home, topdown=True):
	print(pastaAtual)
	os.chdir(pastaAtual)
	#print(arquivos)
	excluir = random.sample(arquivos,563)
	#print(excluir)
	for foto in excluir:
		for arquivo in arquivos:
			if foto == arquivo:
				os.remove(arquivo)
