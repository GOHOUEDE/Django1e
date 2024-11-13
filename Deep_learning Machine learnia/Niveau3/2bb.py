# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:46:20 2024

@author: HOME
"""

from PIL import Image

def convertir_NB(pimg):
    """
    Convertit l'image en noir et blanc.

    Description:
    Cette fonction prend une image en paramètre et la convertit en noir et blanc.
    Elle crée une nouvelle image vide de même taille que l'image originale en mode 1 (noir et blanc).

    Paramètres:
    pimg : Image PIL
        L'image à convertir en noir et blanc.

    Retour:
    Image PIL : L'image convertie en noir et blanc.
    """
    # Création d'une nouvelle image vide en mode 1 (noir et blanc)
    img_nb = Image.new('1', pimg.size)
    
    # Conversion de l'image originale en noir et blanc
    img_nb.paste(pimg.convert('L'), (0, 0))
    
    return img_nb

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Conversion en noir et blanc
image_nb = convertir_NB(image)

# Affichage de l'image convertie
image_nb.show()

def convertir_gris(pimg):
    """
    Convertit l'image en niveaux de gris.

    Description:
    Cette fonction prend une image en paramètre et la convertit en niveaux de gris.
    Elle crée une nouvelle image vide de même taille que l'image originale en mode L (niveaux de gris).

    Paramètres:
    pimg : Image PIL
        L'image à convertir en niveaux de gris.

    Retour:
    Image PIL : L'image convertie en niveaux de gris.
    """
    # Création d'une nouvelle image vide en mode L (niveaux de gris)
    img_gris = Image.new('L', pimg.size)
    
    # Conversion de l'image originale en niveaux de gris
    img_gris.paste(pimg.convert('L'), (0, 0))
    
    return img_gris

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Conversion en niveaux de gris
image_gris = convertir_gris(image)

# Affichage de l'image convertie
image_gris.show()
