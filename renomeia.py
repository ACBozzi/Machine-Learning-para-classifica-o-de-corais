import os, glob
import time
import os


pastaRaiz = '.'

home = '/home/carol/Área de Trabalho/ML/Trabalhao/Dataset/Sub3/7/Patchs'

for (pastaAtual, subpastas, arquivos) in os.walk(home, topdown=True):
	print(pastaAtual)
	os.chdir(pastaAtual)
	for arquivo in arquivos:
		if arquivo.endswith('.png'):
			nome = arquivo
			classe = '7'
			escrever = classe+nome
			os.rename(arquivo, escrever)
			print('Nome:',arquivo, 'Novo:', escrever)
