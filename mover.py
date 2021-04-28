import os
import random
import shutil 

home = '/home/carol/Área de Trabalho/ML/Trabalhao/banco/Favia gravida'
balanceado = '/home/carol/Área de Trabalho/ML/Trabalhao/Balanceado'
 
for (pastaAtual, subpastas, arquivos) in os.walk(home, topdown=True):
	os.chdir(pastaAtual)
	for arquivo in arquivos:
		count = 0
		for foto in arquivos:
			if count < 40:
				print(foto)
				shutil.move(foto,balanceado)
				count = count+1