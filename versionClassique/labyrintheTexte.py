#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Programme principal du labyrinthe en mode texte
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from labyrinthe import *
from ansiColor import *

import time


def LabyrintheTexte(labyrinthe):
    """
    création d'une vue de labyrinthe en mode texte
    paramètre: labyrinthe le labyrinthe à afficher
    résultat: une vue texte du labyrinthe
    """
    return {"labyrinthe":labyrinthe}
    
def setLabyrinthe(lmt,labyrinthe):
    """
    association d'un jeu de labyrinthe à la vue mode texte
    paramètres: lmt: une vue de labyrinthe mode texte
                labyrinthe le labyrinthe à afficher
    La fonction ne retourne pas de résultat mais modifie lmt    
    """
    lmt["labyrinthe"]=labyrinthe

def getLabyrinthe(lmt):
    """
    retourne le labyrinthe associé à la vue mode texte
    paramètre: lmnt  une vue de labyrinthe mode texte
    resultat le labyrinthe associé
    """
    return lmt["labyrinthe"]
    
def afficheCarte(lmt, carte,pion=1,tresor=-1):
    """
    affiche une carte
    paramètres: lmt: une vue de labyrinthe mode texte
                carte: la carte à afficher
                pion: numéro du pion à afficher en priorité si plusieurs disponibles
                tresor: numero du trésor à afficher (le trésor recherché
    Le fonction ne retourne rien mais affiche à l'écran la carte
    """
    coulFond=NORMAL
    coulCar=NORMAL
    style=AUCUN
    if getTresor(carte)==tresor:
        coulFond=GRIS
        coulCar=NOIR
    lesPions=getListePions(carte)
    if len(lesPions)>0:
        if len(lesPions)>1:
            style=GRAS
        if possedePion(carte,pion):
            coulCar=pion
        else:  
            coulCar=lesPions[0]
    pcouleur(toChar(carte),coulCar,coulFond,style)
 
def afficheLabyrinthe(lmt,message="",sauts=0):
    """
    affiche un jeu de labyrinthe
    paramètres: lmt: une vue de labyrinthe mode texte
                message: une chaine de caractères contenant un message à afficher
                sauts: nombre de lignes à sauter à la fin de l'affichage
    Le fonction ne retourne rien mais affiche le labyrinthe à l'écran
    """
    clearscreen();
    print(message)
    labyrinthe=getLabyrinthe(lmt)
    listeJoueurs=getListeJoueurs(labyrinthe)
    print('Cartes restantes : ')
    for i in range(1,getNbParticipants(labyrinthe)+1):
        pcouleur(nomJoueur(listeJoueurs,i).ljust(10)+' '+str(nbTresorsRestantsJoueur(listeJoueurs,i))+' ',i)
        print()
    print()
    print("C'est au tour de ",end='')
    pcouleur(nomJoueurCourant(listeJoueurs),numJoueurCourant(listeJoueurs))
    print(" de jouer")
    tresor=tresorCourant(listeJoueurs)
    print("Le trésor recherché est :",tresor, "caché ",end='')
    coord=getCoordonneesTresorCourant(labyrinthe)
    if coord==None:
        print("sur la carte à jouer")
    else:
        print("en",coord)
    print()
    print(' ',sep='',end='')
    plateau=getPlateau(labyrinthe)
    remplissage=' '*30
    print(remplissage,end='')
    for i in range(1,7,2):
        print(" "+str(i),sep='',end='')
    print()
    for i in range(getNbLignes(plateau)):
        print(remplissage,end='')            
        if i%2==0:
            print(' ',sep='',end='')
        else:
            print(str(i),sep='',end='')
        for j in range(getNbColonnes(plateau)):
            afficheCarte(lmt,getVal(plateau,i,j),numJoueurCourant(listeJoueurs),tresor)
        if i%2==0:
            print(' ',sep='',end='')
        else:
            print(str(i),sep='',end='')            
        print()
    print(' ',sep='',end='')
    print(remplissage,end='')        
    for i in range(1,7,2):
        print(" "+str(i),sep='',end='')
    print()
    print("Carte à jouer: ",end='')
    afficheCarte(lmt,getCarteAJouer(labyrinthe),tresor=tresor)
    for i in range(sauts):
        print()
    print()

def animationChemin(lmt,chemin, joueur,pause=0.1):
    """
    affiche le déplacement du joueur courant vers sa destination
    paramètres: lmt: la vue texte du labyrinthe
                chemin: une liste de coordonnées indiquant le chemin suivi
                joueur: numéro du joueur qui se déplace
                pause: temporisation entre l'affichage de deux étapes
    """
    (xp,yp)=chemin.pop(0)
    plateau=getPlateau(getLabyrinthe(lmt))
    for (x,y) in chemin:
        prendrePionPlateau(plateau,xp,yp,joueur)
        poserPionPlateau(plateau,x,y,joueur)
        afficheLabyrinthe(lmt,sauts=1)
        time.sleep(pause)
        xp,yp=x,y
    return xp,yp

# -------------------------------------------
# fonctions de saisie des actions des joueurs
# CES FONCTIONS SONT A IMPLEMENTER
# -------------------------------------------


def saisirOrdre(lmt):
    """
    permet de saisir soit l'ordre de tourner la carte à jouer
                     soit l'ordre d'insérer la carte à jouer
    la fonction vérifie la validité de l'ordre. On ne sort de la fonction que si
    l'ordre est valide.
    paramètre: lmt: une vue texte de labyrinthe
    résultat: l'ordre saisi sous la forme d'un couple (x,y)
              où x est un caractère valant un des cinq caractères 'T','N','E','S','O'
              dans le cas où x vaut 'T' la valeur de y n'est pas utilisée,
              dans le cas où x vaut une des quatre autres valeurs, y doit valoir 1, 3 ou 5
              c'est à dire le numéro de la ligne ou de la colonne où insérer la carte
              si l'ordre saisi n'est pas valide la focntion retourne (-1,-1)
    """
    pass

def saisirDeplacement(lmt):
    """
    permet de saisir les coordonnées du point d'arrivée visé par le joueur courant
    paramètre: lmt: une vue texte de labyrinthe
    résultat: un couple d'entier (lin,col) indiquant les coordonnées de la case destination. Si l'utilisateur a entré des coordonnées incorrecte la fonction retourne (-1,-1)
    """    
    pass
        
# demarre la partie en mode texte
def demarrer(lmt):
    """
    lance le jeu du labyrinte en mode texte, il faut que le labyrinthe et 
    les joueurs aient été créés avant ce lancement
    paramètre: lmt: une vue texte de labyrinthe
    la fonction ne retourne rien mais effectue une partie de labyrinthe
    """
    # premier affichage du jeu
    afficheLabyrinthe(lmt)
    labyrinthe=getLabyrinthe(lmt)
    plateau=getPlateau(labyrinthe)
    fini=False
    while not fini: # tant qu'aucun joueur n'a gagné
        while(getPhase(labyrinthe)==1):  # tant qu'on est dans la phase 1
            x,y=saisirOrdre(lmt) # on saisit une ordre de phase 1
            res=executerActionPhase1(labyrinthe,x,y) # on effectue les actions liées à cet ordre
            # traitement du résultat de l'ordre pour afficher le bon message à l'utilisateur
            if res==0: 
                message="La carte a été tournée"
            elif res==1:
                message="La carte a bien été insérée"
            elif res==2:
                message="Ce coup est interdit car l'opposé du précédent"
            elif res==3:
                message="Vous devez insérer la carte avant de vous déplacer"
            else:
                message="Veuillez soit tourner la carte soit l'insérer"
            afficheLabyrinthe(lmt,message)
            
        # la première phase est terminée, on va demander au joueur sa case destination
        chemin=None
        xDep,yDep=getCoordonneesJoueurCourant(labyrinthe)
        nomJC=getNomJoueurCourant(labyrinthe)
        pionJC=getNumJoueurCourant(labyrinthe)
        while chemin==None: # tant que la case destination n'est pas valide
            xA,yA=saisirDeplacement(lmt) # saisie de la destination
            if xA==-1 or yA==-1: # coordonées incorrectes
                afficheLabyrinthe(lmt,"Veuillez choisir une case du labyrinthe")
            else: # coordonées correctes 
                  #=> on va verifier l'accessibilité de la case destination pour le joueur courant 
                chemin=accessibleDist(plateau,xDep,yDep,xA,yA)
                if chemin==None:
                    afficheLabyrinthe(lmt,"Cette case n'est pas accessible au joueur "+nomJC)
        # le joueur a saisi une destination correcte et accessible
        # on déplace le joueur sur sa case destination
        animationChemin(lmt,chemin,pionJC)
        # sauvegarde du numéro de trésor à trouver pour l'affichage
        t=getTresorCourant(labyrinthe)
        # action finalisant le tour
        res2=finirTour(labyrinthe)
        message=""
        # traitement du résultat de la fonction finirTour pour afficher le bon message
        if res2==2:
            message="Le joueur "+nomJC+" a gagné"
            fini=True
        elif res2==1:
            message="Le joueur "+nomJC+" vient de trouver le trésor "+str(t)
        afficheLabyrinthe(lmt,message)
    # la partie est terminer
    print("Merci au revoir")


#------------------------------
# programme principal
#------------------------------

if __name__=='__main__': 
    print("Bienvenue dans le jeu du labyrinthe")
    # saisie des noms de joueurs
    listeJoueurs=[]
    rep='O'
    i=1
    while rep in ['o','O']:
        nom=input("Nom du joueur "+str(i)+"? ")
        listeJoueurs.append(nom)
        i+=1
        if i==5:
            rep ='N'
        else:
            rep=input("Y a-t-il un autre joueurs (o/N)? ")
    
    # saisie du nombre de trésors par joueur
    nbTresors=input("Combien de trésors à trouver par joueur (0 pour le maximum possible)?")
    ok=True
    try:
        nbTresorsInt=int(nbTresors)
    except:
        nbTresorsInt=0
        print("Le nombre maximum de trésor a été choisi")
    #initialisation du labyrinthe
    l=Labyrinthe(listeJoueurs,nbTresorsMax=nbTresorsInt)
    #initialisation de l'affichage
    g=LabyrintheTexte(l)
    #démarrage de la partie
    demarrer(g)
