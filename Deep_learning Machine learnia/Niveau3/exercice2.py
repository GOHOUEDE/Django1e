# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:52:42 2024

@author: HOME
"""

from PIL import Image

def convertir_NB_seuil(pimg, seuil):
    """
    Convertit l'image en noir et blanc en utilisant un seuil personnalisé.

    Description:
    Cette fonction prend une image en paramètre et la convertit en noir et blanc en comparant la moyenne
    des composantes RGB de chaque pixel avec un seuil donné. Si la moyenne est supérieure au seuil, le pixel
    est converti en blanc, sinon en noir.

    Paramètres:
    pimg : Image PIL
        L'image à convertir en noir et blanc.
    seuil : int
        Le seuil à utiliser pour la conversion. Les valeurs supérieures à ce seuil seront considérées comme blanches.

    Retour:
    Image PIL : L'image convertie en noir et blanc.
    """
    # Création d'une copie de l'image
    img_nb = pimg.copy()
    
    # Parcours de chaque pixel de l'image
    largeur, hauteur = img_nb.size
    for y in range(hauteur):
        for x in range(largeur):
            # Récupération des composantes RGB du pixel
            r, g, b = img_nb.getpixel((x, y))
            # Calcul de la moyenne des composantes
            moyenne = (r + g + b) / 3
            # Conversion en noir ou blanc selon le seuil
            if moyenne > seuil:
                img_nb.putpixel((x, y), (255, 255, 255))  # Blanc
            else:
                img_nb.putpixel((x, y), (0, 0, 0))  # Noir
    
    return img_nb

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Seuil personnalisé
seuil_personnalise = 120

# Conversion en noir et blanc avec seuil personnalisé
image_nb_seuil = convertir_NB_seuil(image, seuil_personnalise)

# Affichage de l'image convertie
image_nb_seuil.show()
def convertir_gris_luminance(pimg):
    """
    Convertit l'image en niveaux de gris en utilisant la formule de luminance.

    Description:
    Cette fonction prend une image en paramètre et la convertit en niveaux de gris en utilisant la formule de luminance.
    Chaque composante RGB est pondérée selon certains coefficients et leur moyenne est utilisée comme intensité de gris.

    Paramètres:
    pimg : Image PIL
        L'image à convertir en niveaux de gris.

    Retour:
    Image PIL : L'image convertie en niveaux de gris.
    """
    # Création d'une copie de l'image
    img_gris = pimg.copy()
    
    # Parcours de chaque pixel de l'image
    largeur, hauteur = img_gris.size
    for y in range(hauteur):
        for x in range(largeur):
            # Récupération des composantes RGB du pixel
            r, g, b = img_gris.getpixel((x, y))
            # Calcul de la luminance selon la formule
            luminance = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            # Affectation de la luminance au pixel
            img_gris.putpixel((x, y), (luminance, luminance, luminance))
    
    return img_gris

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Conversion en niveaux de gris avec formule de luminance
image_gris_luminance = convertir_gris_luminance(image)

# Affichage de l'image convertie
image_gris_luminance.show()

def filtrer_canaux(pimg):
    """
    Filtre le rouge, le vert et le bleu de l'image.

    Description:
    Cette fonction filtre chaque canal de rouge, de vert et de bleu de l'image passée en paramètre.
    Elle crée trois nouvelles images, chacune contenant un seul canal de couleur, en fixant les autres à 0.

    Paramètres:
    pimg : Image PIL
        L'image à filtrer.

    Retour:
    tuple : Un 3-tuple contenant les images filtrées pour chaque canal (rouge, vert, bleu).
    """
    # Séparation des canaux de couleur
    rouge = pimg.split()[0]
    vert = pimg.split()[1]
    bleu = pimg.split()[2]
    
    # Création des images filtrées en conservant un seul canal de couleur à chaque fois
    img_filtre_rouge = Image.merge('RGB', (rouge, Image.new('L', pimg.size, 0), Image.new('L', pimg.size, 0)))
    img_filtre_vert = Image.merge('RGB', (Image.new('L', pimg.size, 0), vert, Image.new('L', pimg.size, 0)))
    img_filtre_bleu = Image.merge('RGB', (Image.new('L', pimg.size, 0), Image.new('L', pimg.size, 0), bleu))
    
    return img_filtre_rouge, img_filtre_vert, img_filtre_bleu

# Tester la fonction
# Assurez-vous d'avoir une image existante à utiliser
# Remplacez 'chemin/vers/votre/image.png' par le chemin de votre propre image
image = Image.open('jl.jpg')

# Filtrer les canaux de couleur
rouge_filtre, vert_filtre, bleu_filtre = filtrer_canaux(image)

# Affichage des images filtrées
rouge_filtre.show()
vert_filtre.show()
bleu_filtre.show()
