# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:00:16 2024

@author: HOME
"""

from PIL import Image

def inverser_couleurs(pimg):
    """
    Inverse les composantes RGB de chaque pixel de l'image.

    Description:
    Cette fonction prend une image en paramètre et remplace les composantes (r, g, b)
    de chaque pixel par leur complément inverse (255-r, 255-g, 255-b).

    Paramètres:
    pimg : Image PIL
        L'image dont les composantes de chaque pixel doivent être inversées.

    Retour:
    Image PIL : L'image avec les couleurs inversées.
    """
    largeur, hauteur = pimg.size
    img_inverse = Image.new(pimg.mode, (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            pixel_inverse = tuple(255 - c for c in pixel)
            img_inverse.putpixel((x, y), pixel_inverse)

    return img_inverse

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Inverser les couleurs de l'image
image_inverse = inverser_couleurs(image)

# Affichage de l'image avec les couleurs inversées
image_inverse.show()

def composantes_rouges_seules(pimg):
    """
    Affiche uniquement les composantes rouges de l'image.

    Description:
    Cette fonction prend une image en paramètre et ne garde que les composantes rouges de chaque pixel,
    en mettant à 0 les composantes vertes et bleues.

    Paramètres:
    pimg : Image PIL
        L'image dont seules les composantes rouges doivent être affichées.

    Retour:
    Image PIL : L'image avec seulement les composantes rouges.
    """
    largeur, hauteur = pimg.size
    img_rouge_seul = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            pixel_rouge_seul = (pixel[0], 0, 0)  # Garder seulement la composante rouge
            img_rouge_seul.putpixel((x, y), pixel_rouge_seul)

    return img_rouge_seul

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Afficher uniquement les composantes rouges de l'image
image_rouge_seul = composantes_rouges_seules(image)

# Affichage de l'image avec seulement les composantes rouges
image_rouge_seul.show()
def composantes_vertes_seules(pimg):
    """
    Affiche uniquement les composantes vertes de l'image.

    Description:
    Cette fonction prend une image en paramètre et ne garde que les composantes vertes de chaque pixel,
    en mettant à 0 les composantes rouges et bleues.

    Paramètres:
    pimg : Image PIL
        L'image dont seules les composantes vertes doivent être affichées.

    Retour:
    Image PIL : L'image avec seulement les composantes vertes.
    """
    largeur, hauteur = pimg.size
    img_verte_seule = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            pixel_verte_seule = (0, pixel[1], 0)  # Garder seulement la composante verte
            img_verte_seule.putpixel((x, y), pixel_verte_seule)

    return img_verte_seule

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Afficher uniquement les composantes vertes de l'image
image_verte_seule = composantes_vertes_seules(image)

# Affichage de l'image avec seulement les composantes vertes
image_verte_seule.show()
def composantes_bleues_seules(pimg):
    """
    Affiche uniquement les composantes bleues de l'image.

    Description:
    Cette fonction prend une image en paramètre et ne garde que les composantes bleues de chaque pixel,
    en mettant à 0 les composantes rouges et vertes.

    Paramètres:
    pimg : Image PIL
        L'image dont seules les composantes bleues doivent être affichées.

    Retour:
    Image PIL : L'image avec seulement les composantes bleues.
    """
    largeur, hauteur = pimg.size
    img_bleue_seule = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            pixel = pimg.getpixel((x, y))
            pixel_bleue_seule = (0, 0, pixel[2])  # Garder seulement la composante bleue
            img_bleue_seule.putpixel((x, y), pixel_bleue_seule)

    return img_bleue_seule

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Afficher uniquement les composantes bleues de l'image
image_bleue_seule = composantes_bleues_seules(image)

# Affichage de l'image avec seulement les composantes bleues
image_bleue_seule.show()