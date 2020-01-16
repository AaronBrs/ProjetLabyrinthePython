# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    
    joueurs=[]
    listeProvisoireJoueurs=[]
    joueurs.append(0)
    
    for nom in nomsJoueurs:
        
        unJoueur=Joueur(nom)
        
        listeProvisoireJoueurs.append(unJoueur)
        
    joueurs.append(listeProvisoireJoueurs)
        
    return joueurs

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs[1].append(joueur)
    
    

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nombreDeJoueurs=len(joueurs[1])
    nombreAleatoire=random.randint(0,nombreDeJoueurs)        
    for i in range(nombreDeJoueurs):
        if i == nombreAleatoire:
            joueurs[0]=i


    
def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    listeDesJoueurs=joueurs[1]
    nombreDeJoueurs=len(listeDesJoueurs)
    nombreDeTresorsParJoueur=nbTresors/nombreDeJoueurs
    
    listeDesTresorsADistribuer=[]
    for i in range(nbTresors):
        listeDesTresorsADistribuer.append(i+1)
    i=0
    while i < nombreDeTresorsParJoueur:
        for unJoueur in listeDesJoueurs:
            if len(unJoueur['listetresor'])<nbTresorMax:
                unTresorAleatoire=random.choice(listeDesTresorsADistribuer)
                unJoueur['listetresor'].append(unTresorAleatoire)
                listeDesTresorsADistribuer.remove(unTresorAleatoire)
        i+=1

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nombreDeJoueurs=len(joueurs[1])
    indiceSuivant=joueurs[0]+1
    if indiceSuivant>=nombreDeJoueurs:
        joueurs[0]=0
    else:
        joueurs[0]=indiceSuivant

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs[1])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    indiceCourant=joueurs[0]
    return joueurs[1][indiceCourant]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    indiceCourant=joueurs[0]
    listeDesJoueurs=joueurs[1]
    listeDesJoueurs[indiceCourant]['listetresor'].pop(0)           
    
def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    listeDesJoueurs=joueurs[1]
    return len(listeDesJoueurs[numJoueur-1]['listetresor'])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    indiceDuJoueurCourant=joueurs[0]
    return indiceDuJoueurCourant+1

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    indiceDuJoueurCourant=joueurs[0]
    listeDesJoueurs=joueurs[1]
    return getNom(listeDesJoueurs[indiceDuJoueurCourant])
            
def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    listeDesJoueurs=joueurs[1]
    return getNom(listeDesJoueurs[numJoueur-1])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    if joueurs[numJoueur]['listetresor']!=[]:
        return joueurs[numJoueur]['listetresor'][0]
            

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    indiceJoueurCourant=joueurs[0]
    listeDesJoueurs=joueurs[1]
    return prochainTresorJoueur(listeDesJoueurs,indiceJoueurCourant+1)

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if len(getJoueurCourant(joueurs)['listetresor'])==0:
        return True
    else:
        return False