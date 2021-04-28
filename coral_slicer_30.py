# este código vai pegar um valor x e y e cortar o coral em epdaõs desse tampnho
# https://coderwall.com/p/ovlnwa/use-python-and-pil-to-slice-an-image-vertically

from __future__ import division
from PIL import Image
import math
import os

def has_transparency(img):
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False

def slicer(image_path, out_name, outdir, slice_size_x, slice_size_y):
    img = Image.open(image_path)


    if not has_transparency(img):
        mask = Image.new('L', img.size, color = 255)
        img.putalpha(mask)

    angulo = 0
    prop_x = 0.5
    prop_y = 0.5


    # gira a imagem
    img = img.rotate(angulo, expand=True)

    width, height = img.size
  
    upper = 0
    lower = 0
    left = 0
    right = 0

    count_save = 1

    #img.save(os.path.join(outdir, "ORIGINAL_" + out_name + ".png"))

    lower = slice_size_y
    while (lower <= height):
        right = slice_size_x
        while (right <= width):
            if count_save <= 40:
                bbox = (left, upper, right, lower)
                working_slice = img.crop(bbox)

                if not has_transparency(working_slice):
                    working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(count_save) + "_" + str(angulo) + "_graus.png"))
                    count_save += 1

                left += int(slice_size_x * prop_x)
                right += int(slice_size_x * prop_x)
            else:
                return
        left = 0
        upper += int(slice_size_y * prop_y)
        lower += int(slice_size_y * prop_y)

if __name__ == '__main__':

    home = '/home/carol/Área de Trabalho/ML/Trabalhao/Desbalanceado/150/SE'
    
    for (pastaAtual, subpastas, arquivos) in os.walk(home, topdown=True):
        print(pastaAtual)
        os.chdir(pastaAtual)
        for arquivo in arquivos:
            nome = arquivo.split('.png')[0]
            slicer(arquivo,nome, os.getcwd(), 150, 150)
