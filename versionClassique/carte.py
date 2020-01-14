# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    carte=[nord,est,sud,ouest,tresor,pions]
    return carte
def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    cptMur=0
    valide=False #La carte n'est pas valide par défaut
    if c[0]:
        cptMur+=1
    if c[1]:
        cptMur+=1
    if c[2]:
        cptMur+=1
    if c[3]:
        cptMur+=1
    if (cptMur < 3): #S'il y a moins de 3 murs
        valide = True #La carte est valide
    return valide
def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c[0]

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c[2]

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c[1]

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c[3]

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c[5]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c[5]=listePions

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c[5])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    if pion in c[5]:
        res=True
    else:
        res=False
    return res


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c[4]

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c[4]
    c[4]=0
    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c[4]
    c[4]=tresor
    return res

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for indice in range(len(c[5])):
        if c[5][indice]==pion:
            c[5].pop(indice)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c[5]:
        c[5].append(pion)


def tournerHoraire(c):
    """
    NESO
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    aux=c[0]
    c[0]=c[3]
    c[3]=c[2]
    c[2]=c[1]
    c[1]=aux

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    aux=c[0]
    c[0]=c[1]
    c[1]=c[2]
    c[2]=c[3]
    c[3]=aux
    
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    nbTours = random.randint(1,3)
    i=0
    while i < nbTours:
        tournerHoraire(c)
        i+=1

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    #Codage de la carte
    code = 0
    if murNord(c):
        code += 1
    if murEst(c):
        code += 10
    if murSud(c):
        code += 100
    if murOuest(c):
        code += 1000
    #Vérifier l'utilité de cette étape
    i=0
    fini = False
    while i <= code and not fini:
        if code == i:
            fini = True
            res=i
        i+=1
    ##############
    if res == 0:
        indice = 0
    if res == 1:
        indice = 1
    if res == 10:
        indice = 2
    if res == 11:
        indice = 3
    if res == 100:
        indice = 4
    if res == 101:
        indice = 5
    if res == 110:
        indice = 6
    if res == 111:
        indice = 7
    if res == 1000:
        indice = 8
    if res == 1001:
        indice = 9
    if res == 1010:
        indice = 10
    if res == 1011:
        indice = 11
    if res == 1100:
        indice = 12
    if res == 1101:
        indice = 13
    if res == 1110:
        indice = 14
    if res == 1111:
        indice = 15
    return indice

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    
    c[0] = False
    c[1] = False
    c[2] = False
    c[3] = False
    ###############
    print("\nindice :",code)
    if code == 0:
        indice = 0
    if code == 1:
        indice = 1
    if code == 2:
        indice = 10
    if code == 3:
        indice = 11
    if code == 4:
        indice = 100
    if code == 5:
        indice = 101
    if code == 6:
        indice = 110
    if code == 7:
        indice = 111
    if code == 8:
        indice = 1000
    if code == 9:
        indice = 1001
    if code == 10:
        indice = 1010
    if code == 11:
        indice = 1011
    if code == 12:
        indice = 1100
    if code == 13:
        indice = 1101
    if code == 14:
        indice = 1110
    if code == 15:
        indice = 1111

    print("code référence à l'indice",indice)
    
    if indice >= 1000 : #Mur Ouest Présent
        c[3] = True
        indice -= 1000
    
    print(indice)
    
    if indice >= 100 : #Mur Sud Présent
        c[2] = True
        indice -= 100
    
    print(indice)
    
    if indice >= 10 : #Mur Est Présent
        c[1] = True
        indice -= 10
    
    print(indice)
    
    if indice >= 1 : #Mur Nord Présent
        c[0] = True
    else:
        c[0] = False
#listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
#              0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15 
def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return listeCartes[coderMurs(c)]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return  not carte1[0] and not carte2[2]
    

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not carte1[2] and not carte2[0]
def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not carte1[3] and not carte2[1]

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    return not carte1[1] and not carte2[3]