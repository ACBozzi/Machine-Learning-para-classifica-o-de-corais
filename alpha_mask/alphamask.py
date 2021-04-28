# esse script  pega uma imagem que está anotada e tem um json
# e corta todas as anotações e salvar como PNG, sem o fundo

from PIL import Image, ImageDraw
import sys
import json
from os.path import splitext
import os

def createAlphaMask (image_path, image_id):

    # importando imagem
    im = Image.open(image_path)
    base = splitext(image_path)[0]
    js = base + ".json"

    # se tiver JS, OBS: ****não implementado*******, é pra sempre ter
    if js:
        with open(js, 'r', encoding='latin-1') as f:
            dados = json.load(f)

    # indice que vai contar a quantidade de imagens por foto, para salvar com nome diferente
    indice = 1

    # lê os 'shapes' que existe no json e para cada um vai criar uma imagem cortada
    for poligonos in dados["shapes"]:
        mask = Image.new('L', im.size, color = 0) # cria uma máscara toda preta
        draw = ImageDraw.Draw(mask) #aplica

        saving_area = [] # cria lista vazia do poligono que vai ser salvo

        menor_y = poligonos["points"][0][1] # inicializa os valores de x e y com o primeiro valor
        maior_y = poligonos["points"][0][1]
        menor_x = poligonos["points"][0][0]
        maior_x = poligonos["points"][0][0]

        for pontos in poligonos["points"]: # cada points tem dois valores x e y, adiciona cada um deles a lsita
            saving_area.append(pontos[0]) # x
            saving_area.append(pontos[1]) # y

            # esses serão as dimensões da nova imagem
            if pontos[0] < menor_x:
                menor_x = pontos[0]
            if pontos[0] > maior_x:
                maior_x = pontos[0]
            if pontos[1] < menor_y:
                menor_y =  pontos[1]
            if pontos[1] > maior_y:
                maior_y = pontos[1]

        # aqui vai aplicar a máscara branca "a região que vai ficar"
        if (len(saving_area)>2):
            draw.polygon(saving_area, fill = 255)
            im.putalpha(mask)

            # pega a label para fazer o nome do arquivo
            label = poligonos["label"]
            nome = "alpha_masked/" + label + "/" + "img" + str(image_id) + "piece" + str(indice) + ".png"

            os.makedirs(os.path.dirname(nome), exist_ok=True)
            # corta a imagem e salva
            im.crop((menor_x, menor_y, maior_x, maior_y)).save(nome)
        else:
            print("\n Poligono inválido encontrado. Caminho: ", image_path,"\n")

        # apaga a lista com os pontos anteriores
        saving_area.clear
        indice += 1

        # aqui acaba  a iteração e vai para a próxima forma
    return