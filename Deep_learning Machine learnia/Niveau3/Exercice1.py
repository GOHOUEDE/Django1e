# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:32:42 2024

@author: HOME
"""

from PIL import Image

def printRGB(pimg, ppixel):
    """
    Affiche le code RGB du pixel spécifié dans l'image donnée.

    Description:
    Affiche le code RGB du pixel spécifié dans l’image pimg.

    Paramètres:
    pimg : Image PIL
        L'image dans laquelle rechercher le pixel.
    ppixel : tuple
        Un tuple (x, y) représentant les coordonnées du pixel.

    Retour:
    Aucun retour.
    """
    x, y = ppixel
    rgb_value = pimg.getpixel((x, y))
    print(f"Code RGB du pixel ({x}, {y}) : {rgb_value}")

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Pixel à tester
pixel_a_tester = (100, 50)  # Coordonnées du pixel à tester

printRGB(image, pixel_a_tester)


import os

def afficher_info(pimg):
    """
    Affiche les informations de base sur l'image.

    Description:
    Affiche diverses informations sur l'image telles que le nom du fichier,
    le format, le mode de couleur, la taille, le nombre de pixels et le poids
    non compressé en Mo.

    Paramètres:
    pimg : Image PIL
        L'image dont les informations doivent être affichées.

    Retour:
    Aucun retour.
    """
    # Récupération des informations sur l'image
    nom_fichier = os.path.basename(pimg.filename)
    format_image = pimg.format
    mode_couleur = pimg.mode
    taille = pimg.size
    nb_pixels = taille[0] * taille[1]
    poids_mo = os.path.getsize(pimg.filename) / (1024 * 1024)  # Poids en Mo

    # Affichage des informations
    largeur_barre = 50
    barre = '+' + '-' * (largeur_barre - 2) + '+'
    print(barre)
    print(f"| {nom_fichier:<{largeur_barre-3}} |")
    print(barre)
    print(f"| FORMAT : {format_image:<{largeur_barre-12}} |")
    print(f"| MODE : {mode_couleur:<{largeur_barre-10}} |")
    print(f"| TAILLE : {taille[0]} x {taille[1]:<{largeur_barre-17}} |")
    print(f"| NB PIXELS : {nb_pixels:<{largeur_barre-13}} |")
    print(f"| POIDS(non compressé) en Mo : {poids_mo:.2f}{'':<{largeur_barre-32}} |")
    print(barre)

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

afficher_info(image)
def retailler_sauver(pimg, plarg):
    """
    Modifie la largeur de l'image en conservant ses proportions et l'enregistre au format PNG.

    Description:
    Cette fonction redimensionne l'image en conservant ses proportions tout en changeant sa largeur
    selon la valeur spécifiée. L'image redimensionnée est ensuite enregistrée au format PNG.

    Paramètres:
    pimg : Image PIL
        L'image à redimensionner et à enregistrer.
    plarg : int
        La nouvelle largeur souhaitée pour l'image. La hauteur est ajustée proportionnellement.

    Retour:
    Aucun retour.
    """
    # Calcul de la nouvelle hauteur en conservant les proportions
    largeur_originale, hauteur_originale = pimg.size
    nouvelle_hauteur = int(plarg * (hauteur_originale / largeur_originale))
    
    # Redimensionnement de l'image
    img_redimensionnee = pimg.resize((plarg, nouvelle_hauteur), Image.ANTIALIAS)
    
    # Enregistrement de l'image redimensionnée au format PNG
    nom_fichier = "image_redimensionnee.png"
    img_redimensionnee.save(nom_fichier, format="PNG")
    print(f"L'image redimensionnée a été enregistrée sous le nom : {nom_fichier}")

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Nouvelle largeur souhaitée pour l'image redimensionnée
nouvelle_largeur = 400

retailler_sauver(image, nouvelle_largeur)