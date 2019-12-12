# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    """
    creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé
    """
    pass
def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
    pass

def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    pass

def tresorTrouve(joueur):
    """ 
    enleve le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    pass

def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qui reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    pass

def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    pass
