# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 45
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    labyrinthe=dict()

    #Plateau de jeu
    nbJoueurs=len(nomsJoueurs)
    labyrinthe["Plateau de jeu"]=Plateau(nbJoueurs,nbTresors)

    #Liste des joueurs
    labyrinthe["Liste des joueurs"]=ListeJoueurs(nomsJoueurs)

    #Distribution des trésors
    joueurs=labyrinthe["Liste des joueurs"]
    distribuerTresors(joueurs,nbTresors,nbTresorsMax)

    #Phase de jeu
    labyrinthe["Phase de jeu"]=1

    #retenu du coup jouer precedement
    labyrinthe["Dernier coup"]=(None,None)

    return labyrinthe

def getPlateau(labyrinthe): #Fonctionne
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe['Plateau de jeu']["Plateau"]

def getNbParticipants(labyrinthe): #Fonctionne
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return len(labyrinthe["Liste des joueurs"])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe["Liste des joueurs"])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe["Liste des joueurs"])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe["Phase de jeu"]

def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """      
    if labyrinthe["Phase de jeu"] == 1 :
        labyrinthe["Phase de jeu"] = 2
    else : 
        if labyrinthe["Phase de jeu"] == 2 : 
            labyrinthe["Phase de jeu"] = 1



def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """    
    nombreDeTresorsSurLePlateau = 0
    
    listeJoueurs = labyrinthe['Liste des joueurs']
    
    for joueur in listeJoueurs:
        nb = len(joueur['listeTresor'])
        nombreDeTresorsSurLePlateau+=nb
    
    return nombreDeTresorsSurLePlateau 

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe["Liste des joueurs"]


def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    prendreTresorPlateau(getPlateau(labyrinthe),lin,col,numTresor)

def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    prendrePion(getPlateau(labyrinthe)[(getNbColonnes(unPlateauDeJeu)*lin+col)],getJoueurCourant(labyrinthe["Liste des joueurs"]))

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    poserPion(getPlateau(ŀabyrinthe)[(getNbColonnes(getPlateau(ŀabyrinthe))*lin+col)],getJoueurCourant(labyrinthe["Liste des joueurs"]))

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """
    return labyrinthe["Plateau de jeu"]["Carte libre"]

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    if labyrinthe["Dernier coup"][0]==direction and labyrinthe["Dernier coup"][1]==rangee:
        return False
    else :
        if labyrinthe["Dernier coup"][0]=='N' and direction=='S' and labyrinthe["Dernier coup"][1]==rangee:
            return True
        else :
            return False
        if labyrinthe["Dernier coup"][0]=='S' and direction=='N' and labyrinthe["Dernier coup"][1]==rangee:
            return True
        else :
            return False
        if labyrinthe["Dernier coup"][0]=='O' and direction=='E' and labyrinthe["Dernier coup"][1]==rangee:
            return True
        else :
            return False
        if labyrinthe["Dernier coup"][0]=='E' and direction=='O' and labyrinthe["Dernier coup"][1]==rangee:
            return True
        else :
            return False

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    carteAmovible=getCarteAJouer(labyrinthe)
    if direction=='N' and not coupInterdit(labyrinthe,direction,rangee):
        plateau=getPlateau(labyrinthe)
        nouvelleCarteAJouer=decalageColonneEnHaut(plateau, rangee, carteAmovible)
        nouvelleDirectionInterdite='S'
        

    else :
        if direction=='S' and not coupInterdit(labyrinthe,direction,rangee):
            plateau=getPlateau(labyrinthe)
            nouvelleCarteAJouer=decalageColonneEnBas(plateau, rangee, carteAmovible)
            nouvelleDirectionInterdite='N'

        else :
            if direction=='E' and not coupInterdit(labyrinthe,direction,rangee):
                plateau=getPlateau(labyrinthe)
                nouvelleCarteAJouer=decalageLigneADroite(plateau, rangee, carteAmovible)
                nouvelleDirectionInterdite='O'

            else:
                if direction=='O' and not coupInterdit(labyrinthe,direction,rangee):
                    plateau=getPlateau(labyrinthe)
                    nouvelleCarteAJouer=decalageLigneAGauche(plateau, rangee, carteAmovible)
                    nouvelleDirectionInterdite='E'  

    labyrinthe["Dernier coup"] = (direction,rangee)

def tournerCarte(labyrinthe,sens='H'): #Fonctionne
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyrinthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    carteATourner=getCarteAJouer(labyrinthe)
    if sens=='H':
        tournerHoraire(carteATourner)
    else: 
        if sens=='A':
            tournerAntiHoraire(carteATourner)

def getTresorCourant(labyrinthe): 
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(getListeJoueurs(labyrinthe))

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(getPlateau(labyrinthe),(getListeJoueurs(labyrinthe)))


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(getPlateau(labyrinthe),numJoueurCourant(getListeJoueurs(labyrinthe)))


def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """

    if getPhase(labyrinthe)==1:
        if action=='T' and not coupInterdit(labyrinthe,action,rangee):
            tournerCarte(labyrinthe)
            return 0
        else :
            if action=='N' or action=='S' or action=='E' or action=='O' and rangee==1 or rangee==3 or rangee==5 and not coupInterdit(labyrinthe,action,rangee) :
                jouerCarte(labyrinthe,action,rangee)
                return 1
            else :
                if coupInterdit(labyrinthe,action,rangee):
                    return 2
                else:
                    if action >=0 and rangee>=0 :
                        return 3
                    else :
                        return 4
    else :
        return 4
def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    ligJoueurCourant,colJoueurCourant=getCoordonneesJoueurCourant(labyrinthe)
    return accessibleDist(getPlateau(labyrinthe),ligJoueurCourant,colJoueurCourant,ligA,colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    if nbTresorsRestantsJoueur(getListeJoueurs(labyrinthe),getNumJoueurCourant(labyrinthe))==0: #partie terminée car le nb de tresor restant au joueur courant est a 0
        return 2 
    else :
        if (nbTresorsRestantsJoueur(getListeJoueurs(labyrinthe),getNumJoueurCourant(labyrinthe))==(nbTresorsRestantsJoueur(getListeJoueurs(labyrinthe),getNumJoueurCourant(labyrinthe))-1)) and nbTresorsRestantsJoueur(getListeJoueurs(labyrinthe),getNumJoueurCourant(labyrinthe))>0:
            changerJoueurCourant(getListeJoueurs(labyrinthe))
            changerPhase(labyrinthe)
            return 1
        else :
            changerJoueurCourant(getListeJoueurs(labyrinthe))
            changerPhase(labyrinthe)
            return 0

LabyrintheTest=(Labyrinthe(["Joueur1","Joueur2"],12,0)
print(getCoordonneesTresor(getPlateau(LabyrintheTest)),1))