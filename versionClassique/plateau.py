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
    dictionnairePlateau=dict()
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 12 et 46)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
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
    listeIndiceCartesAmovibles=[1,3,5,7,8,9,10,11,12,13,15,17,19,21,22,23,24,25,26,27,29,31,33,35,36,37,38,39,40,]
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
    tresor=getTresor(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*lig+col)])
    if tresor==numTresor:
        prendreTresor(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*lig+col)])
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
    for i in range(getNbLignes(plateau["Plateau"])):
        for j in range(getNbColonnes(plateau["Plateau"])): 
            tresor=getTresor(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*i+j)])
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
    for i in range(getNbLignes(plateau["Plateau"])):
        for j in range(getNbColonnes(plateau["Plateau"])): 
            listePion=getListePion(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*i+j)])
            if joueur in listePion:
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
    prendrePion(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*lin+col)], numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(plateau["Plateau"][(getNbColonnes(plateau["Plateau"])*lin+col)], numJoueur)

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
    def marquageDirect(calque,plateau,val,marque):
        '''
        marque avec la valeur marque les éléments du calque tel que la valeur 
        correspondante n'est pas un mur (de valeur differente de 1) et 
        qu'un de ses voisins dans le calque à pour valeur val
        la fonction doit retourner True si au moins une case du calque a été marquée
        '''
        estMarque=False

        for lig in range(getNbLignes(plateau["Plateau"])):#Pour chaque ligne de notre labyrinthe

            for col in range(getNbColonnes(plateau["Plateau"])):#Pour chaque case de la ligne

                carteActuelle = getVal(plateau["Plateau"],lig,col)

                if col - 1 >= 0:#Carte de gauche existante
                    carteGauche = getVal(plateau["Plateau"],lig,col-1)
                else:
                    carteGauche = None
                
                if lig - 1 >= 0:#Carte du haut existante
                    carteHaut = getVal(plateau["Plateau"],lig-1,col)
                else:
                    carteHaut = None
                
                if col + 1 < getNbColonnes(plateau["Plateau"]):#Carte de droite existante
                    carteDroite = getVal(plateau["Plateau"],lig,col+1)
                else:
                    carteDroite = None
                
                if lig + 1 < getNbLignes(plateau["Plateau"]):#Carte du bas existante
                    carteBas = getVal(plateau["Plateau"],lig+1,col)
                else:
                    carteBas = None

                def unPassagePossible(carte):
                    if passageSud(carte,carteBas):
                        return True
                    else:
                        if passageEst(carte,carteDroite):
                            return True
                        else:
                            if passageNord(carte,carteHaut):
                                return True
                            else:
                                if passageOuest(carte,carteGauche):
                                    return True
                                else:
                                    return False

                if getVal(calque,lig,col)==0 and unPassagePossible(carteActuelle):#Case susceptible d'être marqué (valoir 0 dans le calque et avoir un passage existant avec un voisin)
                    
                    #Vérification des 4 voisins

                    if j-1 >= 0 and (getVal(calque,lig,j-1)==val):#Si la case de gauche est marquée et qu'il n'y a pas de dépassement
                        setVal(calque,i,j,marque)#On marque la case actuelle
                        estMarque=True#Au moins une case a été marqué dans le calque
                    else:#La case de gauche n'est pas marquée
                        
                        if i-1 >= 0 and (getVal(calque,i-1,j)==val):#Si la case du haut est marquée et qu'il n'y a pas de dépassement
                            setVal(calque,i,j,marque)#On marque la case actuelle
                            estMarque=True#Au moins une case a été marqué dans le calque
                        else:#La case de gauche et la case du haut ne sont pas marquées
                            
                            if j+1 < getNbColonnes(plateau["Plateau"]) and getVal(calque,i,j+1)==val:#Si la case de droite est marquée et qu'il n'y a pas de dépassement
                                setVal(calque,i,j,marque)#On marque la case actuelle
                                estMarque=True#Au moins une case a été marqué dans le calque
                            else:#La case de gauche, la case du haut et la case de droite ne sont pas marquées
                                
                                if i+1 < getNbLignes(plateau["Plateau"]) and getVal(calque,i+1,j)==val:#Si la case du bas est marquée et qu'il n'y a pas de dépassement
                                    setVal(calque,i,j,marque)#On marque la case actuelle
                                    estMarque=True#Au moins une case a été marqué dans le calque
        
        return estMarque

    estMarque=True
    calque=Matrice(getNbLignes(plateau["Plateau"]),getNbColonnes(plateau["Plateau"]))
    setVal(calque,0,0,1)

    while estMarque:
        
        estMarque=marquageDirect(calque,plateau["Plateau"],1,1)

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
    listeChemin=[]

    fini=False
    
    while not fini :#Tant qu'on n'est pas arrivé à destination

        #Vérification des voisins     
        
        if colD-1 < getNbLignes(calque) and getVal(calque,ligD,colD-1)==getVal(calque,ligD,colD+1)+1:#Si la case de gauche vaut la case -1
            listeChemin.append((ligD,colD))#On ajoute la position à la liste des chemins
            colD-=1
            print("Positions créant le chemin possible :",listeChemin,"\n")
        else:
            if ligD-1 < getNbColonnes(calque) and getVal(calque,ligD-1,colD)==getVal(calque,ligD,colD)+1 :#Si la case de dessus vaut la case -1
                listeChemin.append((ligD,colD))#On ajoute la position à la liste des chemins
                ligD-=1
                print("Positions créant le chemin possible :",listeChemin,"\n")
        if (ligD,colD) == (ligA,colA):
            listeChemin.append((ligD,colD))
            fini=True
    return listeChemin