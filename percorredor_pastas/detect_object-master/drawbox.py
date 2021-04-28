#!/usr/bin/python

import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import os
from os.path import splitext

try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range


pastaRaiz = '.'
caminho = os.path.abspath(pastaRaiz) # guarda o caminho absoluto da pasta atual do programa. Seria interessante pegar como entrada!
arquivosImagem = [] # uma lista com todas as imagens (começa vazia) [vai ser guardado o caminho absoluto]
arquivosTxt = [] # lista com todos os txts (vazia) [same]
for (raiz, diretorios, arquivos) in os.walk(caminho, topdown=True):
    arquivosImagem.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.png') or arquivo.endswith('.jpg')])
    arquivosTxt.extend ( [os.path.join(raiz, arquivo) for arquivo in arquivos if arquivo.endswith('.txt')])

# cria um conjunto, cortando o texto. Documentos contém o nomes dos txt, sem o .txt
documentos = set([splitext(filename)[0] for filename in arquivosTxt])

# Compara a lista "documentos" com a lista arquivosImg que vai ser divida, se elas não estiverem nas duas, vai entrar pra lista semTXT
semTxt = [filename for filename in set(arquivosImagem) if splitext(filename)[0] not in documentos]
print(semTxt)

#setting
wCanvas = 1000 # precisamos pegar o canvas para CADA imagem pq fica ridiculo
hCanvas = 700
datasave = 'box.txt' # tem que salvar varios
dirimg = 'image/wombat' # caminho absoluto


class BoundingBox(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.x = self.y = 0
		self.canvas = tk.Canvas(self, width=wCanvas, height=hCanvas, cursor="cross")


		self.canvas.pack(side="top", fill="both", expand=True)
		self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
		self.canvas.bind("<ButtonPress-1>", self.on_button_press)
		self.canvas.bind("<B1-Motion>", self.on_move_press)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

		self.canvas.focus_set()
		self.canvas.bind("<Left>", self.previmg)
		self.canvas.bind("<Right>", self.nextimg)
		self.canvas.bind("s", self.saveboxcord)
		self.canvas.bind("d", self.resetbox)

		#add label of numbering
		self.numbering = tk.Label(self, text='0')
		self.numbering.pack()

		#open data save
		self.allimg = sorted(os.listdir(dirimg))
		self.imgptr = 0

		self.boxdata = None

		self.allcord = []

		self.allrect = []
		self.rect = None

		self.start_x = None
		self.start_y = None
		self.end_x = None
		self.end_y = None
		self.totwidth = None
		self.totheight = None


		self._draw_image()


	def _draw_image(self):
		self.im = Image.open(dirimg+'/'+self.allimg[self.imgptr])
		self.tk_im = ImageTk.PhotoImage(self.im)
		self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)

	def saveboxcord(self, event):
		self.boxdata = open(datasave, 'a+')
		for i in xrange(len(self.allcord)):
			self.boxdata.write(self.allimg[self.imgptr]+','+
			str(self.allcord[i][0])+','+
			str(self.allcord[i][1])+','+
			str(self.allcord[i][2])+','+
			str(self.allcord[i][3])+','+
			str(self.allcord[i][4])+','+
			str(self.allcord[i][5])+'\n')
		for i in xrange(len(self.allrect)):
			self.canvas.delete(self.allrect[i])
		del self.allcord[:]
		del self.allrect[:]
		self.boxdata.close()
		self.numbering.configure(text="Caixa Salva")

	def resetbox(self, event):
		for i in xrange(len(self.allrect)):
			self.canvas.delete(self.allrect[i])
		del self.allcord[:]
		del self.allrect[:]
		self.numbering.configure(text="Caixa Resetada")

	def nextimg(self, event):
		for i in xrange(len(self.allrect)):
			self.canvas.delete(self.allrect[i])
		del self.allcord[:]
		del self.allrect[:]
		self.canvas.delete("all")

		self.imgptr += 1
		if self.imgptr > len(self.allimg)-1:
			self.imgptr = 0
		self._draw_image()
		self.numbering.configure(text=str(self.imgptr))

	def previmg(self, event):
		for i in xrange(len(self.allrect)):
			self.canvas.delete(self.allrect[i])
		del self.allcord[:]
		del self.allrect[:]
		self.canvas.delete("all")

		self.imgptr -= 1
		if self.imgptr < 0:
			self.imgptr = len(self.allimg)-1
		self._draw_image()
		self.numbering.configure(text=str(self.imgptr))


	def on_button_press(self, event):
		# save mouse drag start position
		self.start_x = event.x
		self.start_y = event.y

		# create rectangle if not yet exist
		#if not self.rect:
		self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='green', width=3)

	def on_move_press(self, event):
		curX, curY = (event.x, event.y)

		if curX > wCanvas:
			curX = wCanvas
		if curY > hCanvas:
			curY = hCanvas

		self.end_x = curX
		self.end_y = curY

		# expand rectangle as you drag the mouse
		self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)



	def on_button_release(self, event):
		self.imarray = np.array(self.im)
		self.totwidth = len(self.imarray)
		self.totheight = len(self.imarray[0])
		print(self.start_x, self.start_y, self.end_x, self.end_y, self.totwidth, self.totheight)
		self.allcord.append([self.start_x, self.start_y, self.end_x, self.end_y, self.totwidth, self.totheight])
		self.allrect.append(self.rect)
		print (len(self.allcord))


if __name__ == "__main__":
	draw = BoundingBox()
	draw.mainloop()
