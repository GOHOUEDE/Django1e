# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:22:07 2024

@author: HOME
"""

from PIL import Image

def symetrie_horizontale(pimg):
    """
    Réalise une symétrie horizontale de l'image.

    Description:
    Cette fonction prend une image en paramètre et réalise une symétrie horizontale,
    c'est-à-dire qu'elle inverse l'ordre des lignes de l'image.

    Paramètres:
    pimg : Image PIL
        L'image à symétriser horizontalement.

    Retour:
    Image PIL : L'image avec la symétrie horizontale réalisée.
    """
    largeur, hauteur = pimg.size
    img_symetrie_horizontale = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            img_symetrie_horizontale.putpixel((x, hauteur - y - 1), pixel)

    return img_symetrie_horizontale

def symetrie_verticale(pimg):
    """
    Réalise une symétrie verticale de l'image.

    Description:
    Cette fonction prend une image en paramètre et réalise une symétrie verticale,
    c'est-à-dire qu'elle inverse l'ordre des colonnes de l'image.

    Paramètres:
    pimg : Image PIL
        L'image à symétriser verticalement.

    Retour:
    Image PIL : L'image avec la symétrie verticale réalisée.
    """
    largeur, hauteur = pimg.size
    img_symetrie_verticale = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            img_symetrie_verticale.putpixel((largeur - x - 1, y), pixel)

    return img_symetrie_verticale

# Charger l'image sur laquelle réaliser les symétries
image = Image.open('jl.jpg')

# Réaliser la symétrie horizontale et afficher l'image résultante
symetrie_horizontale_image = symetrie_horizontale(image)
symetrie_horizontale_image.show()

# Réaliser la symétrie verticale et afficher l'image résultante
symetrie_verticale_image = symetrie_verticale(image)
symetrie_verticale_image.show()
