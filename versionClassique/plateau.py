# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *
import random

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant aléatoirement nbTresors trésors
    Cette fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    Paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    Résultat: la liste mélangée aléatoirement des cartes amovibles créées
    """
    listeCartesAmovibles=[]

    #Création des cartes amovibles
    
    for i in range(12):#Création de 12 cartes "Tout-droit"
        nvCarteToutdroit=Carte(True,False,True,False)
        tourneAleatoire(nvCarteToutdroit)
        listeCartesAmovibles.append(nvCarteToutdroit)

    for i in range(16):#Création de 16 cartes "Angles"
        nvCarteAngle=Carte(True,True,False,False)
        tourneAleatoire(nvCarteAngle)
        listeCartesAmovibles.append(nvCarteAngle)

    for i in range(6):#Création de 6 cartes "Jonction"
        nvCarteJonction=Carte(False,False,False,False)
        listeCartesAmovibles.append(nvCarteJonction)
    
    #Mélange de la liste des cartes amovibles

    random.shuffle(listeCartesAmovibles)

    #Création de la liste des trésors
    listeTresors=[]
    for i in range(tresorDebut,nbTresors):
        listeTresors.append(i)
    
    #Mélange de la liste des trésors

    random.shuffle(listeTresors)

    #Attribution des trésors

    for carte in listeCartesAmovibles:          #Pour chaque carte amovible
        if len(listeTresors)>0:                 #S'il reste encore des trésors à attribuer
            tresor=random.choice(listeTresors)  #Tirage au sort d'un trésor
            listeTresors.remove(tresor)         #On retire le trésor de la liste pour pas qu'il ne soit attribué deux fois
            mettreTresor(carte,tresor)          #On pose le trésor sur la carte
            nbTresors-=1                        #Mise à jour du nombre de trésors (à voir)

    return listeCartesAmovibles

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 12 et 46)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    
    dictionnairePlateau=dict()
    
    #Création du plateau vierge

    nouveauPlateau=Matrice(7,7)

    #Création des cartes fixes et attribution de  leur trésor (16 cartes)

    #Création de la liste des trésors
    nbTresorsPlaces=0
    listeTresors=[]
    for i in range(1,nbTresors+1):
        listeTresors.append(i)
    random.shuffle(listeTresors)

    #Carte des Angles (4 cartes)

    carteAngleHautGauche       =  Carte(True,False,False,True,0,[])     #indice 0    (0,0)
    carteAngleHautDroite       =  Carte(True,True,False,False,0,[])     #indice 6    (0,6)
    carteAngleBasGauche        =  Carte(False,False,True,True,0,[])     #indice 42   (6,0)
    carteAngleBasDroite        =  Carte(False,True,True,False,0,[])     #indice 48   (6,6)
    
    #Insertion des joueurs en fonction du nombre de joueurs
    
    if nbJoueurs <= 0 and nbTresors > 4:#NbJoueurs incorrect
        return None
    else:
        if nbJoueurs >= 4:
            poserPion(carteAngleHautGauche,1) #Vert
            poserPion(carteAngleHautDroite,2) #Bleu
            poserPion(carteAngleBasGauche,3)  #Jaune
            poserPion(carteAngleBasDroite,4)  #Rouge
        else:
            if nbJoueurs >= 3:
                poserPion(carteAngleHautGauche,1)
                poserPion(carteAngleHautDroite,2)
                poserPion(carteAngleBasGauche,3)
            else:
                if nbJoueurs >= 2:
                    poserPion(carteAngleHautGauche,1)
                    poserPion(carteAngleBasDroite,2)
                else:
                    if nbJoueurs >= 1:
                        poserPion(carteAngleHautGauche,1)
        
    
    #Carte de la forme ╠ (3 cartes)

    tresorCarteCoteSuperieurGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteSuperieurGauche)
    carteCoteSuperieurGauche   =  Carte(False,False,False,True,tresorCarteCoteSuperieurGauche,[])    #indice 14   (2,0)
    nbTresorsPlaces+=1

    tresorCarteCoteInferieurGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteInferieurGauche)
    carteCoteInferieurGauche   =  Carte(False,False,False,True,tresorCarteCoteInferieurGauche,[])    #indice 28   (3,0)
    nbTresorsPlaces+=1

    tresorCarteMilieuHautGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteMilieuHautGauche)
    carteMilieuHautGauche      =  Carte(False,False,False,True,tresorCarteMilieuHautGauche,[])       #indice 16   (2,2)
    nbTresorsPlaces+=1


    #Carte de la forme ╣ (3 cartes)

    tresorCarteCoteSuperieurDroit=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteSuperieurDroit)
    carteCoteSuperieurDroit    =  Carte(False,True,False,False,tresorCarteCoteSuperieurDroit,[])    #indice 20   (2,6)
    nbTresorsPlaces+=1

    tresorCarteCoteInferieurDroit=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteInferieurDroit)
    carteCoteInferieurDroit    =  Carte(False,True,False,False,tresorCarteCoteInferieurDroit,[])    #indice 34   (3,6)
    nbTresorsPlaces+=1

    tresorCarteMilieuBasDroit=random.choice(listeTresors)
    listeTresors.remove(tresorCarteMilieuBasDroit)
    carteMilieuBasDroit        =  Carte(False,True,False,False,tresorCarteMilieuBasDroit,[])        #indice 32   (3,4)
    nbTresorsPlaces+=1


    #Carte de la forme ╦ (3 cartes)

    tresorCarteCoteHautGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteHautGauche)
    carteCoteHautGauche        =  Carte(True,False,False,False,tresorCarteCoteHautGauche,[])    #indice 2    (0,2)
    nbTresorsPlaces+=1

    tresorCarteCoteHautDroite =random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteHautDroite)
    carteCoteHautDroite        =  Carte(True,False,False,False,tresorCarteCoteHautDroite,[])    #indice 4    (0,4)
    nbTresorsPlaces+=1

    tresorCarteMilieuHautDroite=random.choice(listeTresors)
    listeTresors.remove(tresorCarteMilieuHautDroite)
    carteMilieuHautDroite      =  Carte(True,False,False,False,tresorCarteMilieuHautDroite,[])  #indice 18   (2,4)
    nbTresorsPlaces+=1


    #Carte de la forme ╩ (3 cartes)

    tresorCarteCoteBasGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteBasGauche)
    carteCoteBasGauche         =  Carte(False,False,True,False,tresorCarteCoteBasGauche)        #indice 44   (6,2)
    nbTresorsPlaces+=1

    tresorCarteCoteBasDroite=random.choice(listeTresors)
    listeTresors.remove(tresorCarteCoteBasDroite) 
    carteCoteBasDroite         =  Carte(False,False,True,False,tresorCarteCoteBasDroite,[])     #indice 46   (6,4)
    nbTresorsPlaces+=1

    tresorCarteMilieuBasGauche=random.choice(listeTresors)
    listeTresors.remove(tresorCarteMilieuBasGauche)
    carteMilieuBasGauche       =  Carte(False,False,True,False,tresorCarteMilieuBasGauche,[])    #indice 30   (3,2)
    nbTresorsPlaces+=1


    #Création des cartes amovibles (34 cartes)

    listeNouvellesCartesAmovibles=creerCartesAmovibles(nbTresorsPlaces,nbTresors+1)
    
    #Positionnement des cartes fixes

    #Positionnement des coins

    setVal(nouveauPlateau,0,0,carteAngleHautGauche)
    setVal(nouveauPlateau,0,6,carteAngleHautDroite)
    setVal(nouveauPlateau,6,0,carteAngleBasGauche)
    setVal(nouveauPlateau,6,6,carteAngleBasDroite)
    
    #Positionnement côté gauche

    setVal(nouveauPlateau,2,0,carteCoteSuperieurGauche)
    setVal(nouveauPlateau,3,0,carteCoteInferieurGauche)
    setVal(nouveauPlateau,2,2,carteMilieuHautGauche)
    
    #Positionnement côté droite
    
    setVal(nouveauPlateau,2,6,carteCoteSuperieurDroit)
    setVal(nouveauPlateau,3,6,carteCoteInferieurDroit)
    setVal(nouveauPlateau,3,4,carteMilieuBasDroit)
    
    #Positionnement côté haut
    
    setVal(nouveauPlateau,0,2,carteCoteHautGauche)
    setVal(nouveauPlateau,0,4,carteCoteHautDroite)
    setVal(nouveauPlateau,2,4,carteMilieuHautDroite)
    
    #Positionnement côté bas
    
    setVal(nouveauPlateau,6,2,carteCoteBasGauche)
    setVal(nouveauPlateau,6,4,carteCoteBasDroite)
    setVal(nouveauPlateau,3,2,carteMilieuBasGauche)

    #Plateau avec cartes fixes défini
    
    #Liste des indices des cartes amovibles (33 placées + 1 libre)
    
    #    1     3     5 
    # 7  8  9  10 11 12 13
    #    15    17    19   
    # 21 22 23 24 25 26 27
    #    29    31    33   
    # 35 36 37 38 39 40 41
    #    43    45    47
    
    #Positionnement aléatoires des cartes amovibles

    for i in range(getNbLignes(nouveauPlateau)):                        #Pour chaque ligne du plateau
        for j in range(getNbColonnes(nouveauPlateau)):                  #Pour chaque case du plateau
            if getVal(nouveauPlateau,i,j) == 0:                         #La case n'a pas encore de carte attribué
                if len(listeNouvellesCartesAmovibles) > 0:              #S'il reste encore des cartes amovibles disponibles
                    valeurAjoutee=listeNouvellesCartesAmovibles[0]
                    setVal(nouveauPlateau,i,j,valeurAjoutee)            #Attribution d'une carte amovibles sur la case
                    listeNouvellesCartesAmovibles.remove(valeurAjoutee) #On retire la carte de la liste des cartes disponibles
         
    #Création de la carte libre
    
    carteLibre=listeNouvellesCartesAmovibles[0]

    #Retour de la fonction
    dictionnairePlateau["Plateau"]=nouveauPlateau
    dictionnairePlateau["Carte libre"]=carteLibre
    return dictionnairePlateau


def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lig,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    tresor=getTresor(plateau["Liste de valeurs"][(getNbColonnes(plateau)*lig+col)])
    if tresor==numTresor:
        prendreTresor(plateau["Liste de valeurs"][(getNbColonnes(plateau)*lig+col)])
        return True
    else :
        return False

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    coordonnees=None
    for i in range(getNbLignes(plateau)):
        for j in range(getNbColonnes(plateau)): 
            tresor=getTresor(plateau['Liste de valeurs'][(getNbColonnes(plateau)*i+j)])
            if tresor==numTresor:
                coordonnees=(i,j)
    return coordonnees

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    coordonnees=None
    for i in range(getNbLignes(plateau)):
        for j in range(getNbColonnes(plateau)): 
            listePion=getListePions(plateau['Liste de valeurs'][(getNbColonnes(plateau)*i+j)])
            if numJoueur in listePion:
                coordonnees=(i,j)
    return coordonnees


def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    prendrePion(plateau["Liste de valeurs"][(getNbColonnes(plateau)*lin+col)], numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(plateau["Liste de valeurs"][(getNbColonnes(plateau)*lin+col)], numJoueur)

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    def marquageDirect(calque,plateau):

        estMarque=False

        for lig in range(getNbLignes(plateau)):#Pour chaque ligne de notre labyrinthe

            for col in range(getNbColonnes(plateau)):#Pour chaque case de la ligne

                if getVal(calque,lig,col)==0:#Case susceptible d'être marqué
                    
                    #Vérification des 4 voisins

                    if col-1 >= 0 and getVal(calque,lig,col-1)==1 :#Case de gauche
                        if passageOuest(getVal(plateau,lig,col),getVal(plateau,lig,col-1)):#S'il existe un passage à gauche de la carte actuelle
                            setVal(calque,lig,col,1)
                            estMarque=True
                    else:

                        if lig-1 >= 0 and getVal(calque,lig-1,col)==1:#Case du haut
                            if passageNord(getVal(plateau,lig,col),getVal(plateau,lig-1,col)):#S'il existe un passage à gauche de la carte actuelle
                                setVal(calque,lig,col,1)
                                estMarque=True
                        else:
                            
                            if col+1 < getNbColonnes(plateau) and getVal(calque,lig,col+1)==1:#Case de droite
                                if passageEst(getVal(plateau,lig,col),getVal(plateau,lig,col+1)):#S'il existe un passage à gauche de la carte actuelle
                                    setVal(calque,lig,col,1)
                                    estMarque=True
                            else:
                                
                                if lig+1 < getNbLignes(plateau) and getVal(calque,lig+1,col)==1 :#Case du bas
                                    if passageSud(getVal(plateau,lig,col),getVal(plateau,lig+1,col)):#S'il existe un passage à gauche de la carte actuelle
                                        setVal(calque,lig,col,1)
                                        estMarque=True
        
        return estMarque

    estMarque=True
    calque=Matrice(getNbLignes(plateau),getNbColonnes(plateau))
    setVal(calque,0,0,1)

    while estMarque:
        
        estMarque=marquageDirect(calque,plateau)

    if getVal(calque,ligD,colD) != 0 and getVal(calque,ligA,colA) != 0:
        res=True
    else:
        res=False
    return res

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    def marquageDirect(calque,plateau):
        estMarque=False
        for lig in range(getNbLignes(plateau)):#Pour chaque ligne de notre labyrinthe
            for col in range(getNbColonnes(plateau)):#Pour chaque case de la ligne
                if getVal(calque,lig,col)==0:#Case susceptible d'être marqué
                    #Vérification des 4 voisins
                   
                    if col-1 >= 0:
                        val=getVal(calque,lig,col-1)
                        if val>0:#Case de gauche
                            if passageEst(getVal(plateau,lig,col),getVal(plateau,lig,col-1)):
                                setVal(calque,lig,col,val+1)
                                estMarque=True
                    if lig-1 >= 0:
                        val=getVal(calque,lig-1,col)
                        if val>0:
                            if passageNord(getVal(plateau,lig,col),getVal(plateau,lig-1,col)):
                                setVal(calque,lig,col,val+1)
                                estMarque=True
                    if col+1 < getNbColonnes(plateau):
                        val=getVal(calque,lig,col+1)
                        if val>0 :
                            if passageOuest(getVal(plateau,lig,col),getVal(plateau,lig,col+1)):
                                setVal(calque,lig,col,val+1)
                                estMarque=True
                    if lig+1 < getNbLignes(plateau):
                        val=getVal(calque,lig+1,col)
                        if val>0:
                            if passageSud(getVal(plateau,lig,col),getVal(plateau,lig+1,col)):
                                setVal(calque,lig,col,val+1)
                                estMarque=True
        return estMarque

    if accessible(plateau,ligD,colD,ligA,colA):

        estMarque=True
        
        calque=Matrice(getNbLignes(plateau),getNbColonnes(plateau))
        setVal(calque,0,0,1)

        while estMarque:        
        
            estMarque=marquageDirect(calque,plateau)
        
        val=getVal(calque,ligA,colA)

        listeCoord=[(ligA,colA)]

        while (ligD,colD) != (ligA,colA):
            if ligA - 1 >= 0:
                val_haut = getVal(calque,ligA-1,colA)
                if val_haut==val-1:
                    ligA -= 1
                    val=val_haut
                    listeCoord.append((ligA,colA))
            if ligA + 1 < getNbLignes(calque):
                val_bas=getVal(calque,ligA+1,colA)
                if val_bas==val-1:
                    ligA+=1
                    val=val_bas
                    listeCoord.append((ligA,colA))
            if colA - 1 >=0:
                val_gauche=getVal(calque,ligA,colA-1)
                if val_gauche==val-1:
                    colA-=1
                    val=val_gauche
                    listeCoord.append((ligA,colA))
            if colA + 1 < getNbColonnes(calque):
                val_droite=getVal(calque,ligA,colA+1)
                if val_droite==val-1:
                    colA+=1
                    val=val_droite
                    listeCoord.append((ligA,colA))
        listeCoord.reverse()
        return listeCoord
    else:
        return None
    
