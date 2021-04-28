from skimage.feature import local_binary_pattern
import numpy as np
import os, glob
import os
import cv2

def Lbp(home, features, label):

	METHOD = 'uniform'
	radius = 3
	n_points = 8 * radius

	for (pastaAtual, subpastas, arquivos) in os.walk(home, topdown=True):
		os.chdir(pastaAtual)
		lbp=[]
		unique = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
		
		for img in arquivos:
			print(img)
			img = cv2.imread(img,0)
			lbp_pred = local_binary_pattern(img, n_points, radius, METHOD)
			lbp_pred = lbp_pred.ravel()
			hist = np.histogram(lbp_pred, bins=unique)
			result = hist[0]/22500 #mudar de acordo com tamanho do patch!!!NÂO ESQUEÇA LINDONA
			result.ravel
			
			features.write(str(label)+ " ")
			indice = 0
			
			for x in result:
				features.write(str(indice)+":"+str(x)+" ")
				indice = indice +1

			features.write("\n")


if __name__ == '__main__':


	features = open("Desbalanfeatures150LBP.txt", "a")
	label = 6

	home = '/home/carol/Área de Trabalho/ML/Trabalhao/Desbalanceado/150/SE'
	Lbp(home,features,label)
