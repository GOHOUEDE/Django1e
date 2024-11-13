# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:07:43 2024

@author: HOME
"""

from PIL import Image

def filtrage_seuil_rouge(pimg):
    """
    Filtre les composantes rouges d'une image par seuil.

    Description:
    Cette fonction prend une image en paramètre et met à zéro les composantes rouges des pixels
    si elles sont inférieures à 127, et les fixe à 255 sinon. Les autres composantes restent inchangées.

    Paramètres:
    pimg : Image PIL
        L'image à traiter.

    Retour:
    Image PIL : L'image avec les composantes rouges filtrées par seuil.
    """
    largeur, hauteur = pimg.size
    img_filtree = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            if pixel[0] < 127:
                pixel_filtre = (0, pixel[1], pixel[2])  # Mettre à zéro la composante rouge si < 127
            else:
                pixel_filtre = (255, pixel[1], pixel[2])  # Fixer la composante rouge à 255 sinon
            img_filtree.putpixel((x, y), pixel_filtre)

    return img_filtree

# Charger l'image de la Joconde
image_joconde = Image.open('joconde.jpg')

# Appliquer le filtrage par seuil sur les composantes rouges
image_filtree = filtrage_seuil_rouge(image_joconde)

# Afficher l'image originale et l'image filtrée
image_joconde.show()
image_filtree.show()
