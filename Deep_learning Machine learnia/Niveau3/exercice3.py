# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:14:51 2024

@author: HOME
"""

from PIL import Image

def convolution_filtre_passe_haut(pimg):
    """
    Applique la convolution avec un filtre passe-haut sur l'image.

    Description:
    Cette fonction prend une image en paramètre et applique la convolution avec un filtre passe-haut.
    Pour chaque pixel, la nouvelle valeur est calculée comme la somme pondérée de ses 8 voisins selon le filtre.

    Paramètres:
    pimg : Image PIL
        L'image à modifier par convolution.

    Retour:
    Image PIL : L'image modifiée par convolution avec le filtre passe-haut.
    """
    largeur, hauteur = pimg.size
    img_modifiee = Image.new('RGB', (largeur, hauteur))

    # Filtre passe-haut
    filtre = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]

    for y in range(1, hauteur - 1):
        for x in range(1, largeur - 1):
             
            somme = [0, 0, 0]
            for j in range(-1, 2):
                for i in range(-1, 2):
                    pixel = pimg.getpixel((x + i, y + j))  # Valeur du pixel voisin
                    poids = filtre[j + 1][i + 1]  # Poids du filtre correspondant
                    somme[0] += poids * pixel[0]
                    somme[1] += poids * pixel[1]
                    somme[2] += poids * pixel[2]
            # Limiter les valeurs aux bornes de 0 et 255
            nouvelle_valeur = tuple(min(max(int(s), 0), 255) for s in somme)
            img_modifiee.putpixel((x, y), nouvelle_valeur)

    return img_modifiee

# Charger l'image sur laquelle appliquer la convolution
image = Image.open('jl.jpg')

# Appliquer la convolution avec le filtre passe-haut
image_modifiee = convolution_filtre_passe_haut(image)

# Afficher l'image originale et l'image modifiée
image.show()
image_modifiee.show()
