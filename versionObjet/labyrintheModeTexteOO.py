#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Programme principal du labyrinthe en mode texte
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from labyrintheOO import *
from ansiColor import *
import sys
import time

class LabyrintheModeTexte(object):
    def __init__(self):
        labyrinthe=None
        
    def setLabyrinthe(self,labyrinthe):
        self.labyrinthe=labyrinthe
        
    def afficheCarte(self, carte,pion=1,tresor=-1):
            coulFond=NORMAL
            coulCar=NORMAL
            style=AUCUN
            if carte.getTresor()==tresor:
                coulFond=GRIS
                coulCar=NOIR
            lesPions=carte.getListePions()
            if len(lesPions)>0:
                if len(lesPions)>1:
                    style=GRAS
                if carte.possedePion(pion):
                    coulCar=pion
                else:  
                    coulCar=lesPions[0]
            pcouleur(carte.toChar(),coulCar,coulFond,style)
     
    def afficheLabyrinthe(self,message="",sauts=0):
        clearscreen();
        print(message)
        print('Cartes restantes :',end='')
        for i in range(1,self.labyrinthe.getNbJoueurs()+1):
            pcouleur('Joueur '+str(i)+' '+str(self.labyrinthe.nbTresorsRestants(i))+' ',i)
        print()
        print("C'est au tour du ",end='')
        pcouleur('Joueur '+str(self.labyrinthe.getJoueurCourant())+ " de jouer",self.labyrinthe.getJoueurCourant())
        print()
        tresor=self.labyrinthe.getTresorCourant()
        print("Le trésor recherché est :",tresor, "caché ",end='')
        coord=self.labyrinthe.getCoordonneesTresorCourant()
        if coord==None:
            print("sur la carte à jouer")
        else:
            print("en",coord)
        print()
        print(' ',sep='',end='')
        plateau=self.labyrinthe.plateau
        remplissage=' '*30
        print(remplissage,end='')
        for i in range(1,7,2):
            print(" "+str(i),sep='',end='')
        print()
        for i in range(plateau.getNbLignes()):
            print(remplissage,end='')            
            if i%2==0:
                print(' ',sep='',end='')
            else:
                print(str(i),sep='',end='')
            for j in range(plateau.getNbColonnes()):
                self.afficheCarte(plateau.getVal(i,j),self.labyrinthe.getJoueurCourant(),tresor)
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
        self.afficheCarte(self.labyrinthe.getCarteAJouer(),tresor)
        for i in range(sauts):
            print()
        print()

    def animationChemin(self,chemin, joueur,pause=0.1):
        (xp,yp)=chemin.pop(0)
        for (x,y) in chemin:
            self.labyrinthe.prendrePion(xp,yp,joueur)
            self.labyrinthe.mettrePion(x,y,joueur)
            self.afficheLabyrinthe(sauts=1)
            time.sleep(pause)
            xp,yp=x,y
        return xp,yp

    def saisirOrdre(self):
        pass    
    def saisirDeplacement(self):
        pass        
            

    def main(self):
        print("Bienvenue dans le jeu du labyrinthe")
        nbJoueurs=input("Combien de joueurs? ")
        while nbJoueurs not in ['2','3','4']:
            print("Le nombre de joueurs doit être compris entre 2 et 4")
            nbJoueurs=input("Combien de joueurs? ")
        l=Labyrinthe(int(nbJoueurs))
        self.setLabyrinthe(l)
        self.afficheLabyrinthe()
    
        fini=False
        while not fini:
            finOrdre=False
            while(not finOrdre):
                ordre=self.saisirOrdre()
                if ordre[0] in 'tT':
                    self.labyrinthe.tournerCarte()
                    self.afficheLabyrinthe("La carte a été tournée")
                elif ordre[0] in 'qQ':
                    print("Abandon de la partie!")
                    sys.exit()
                else:
                    self.labyrinthe.jouerCarte(ordre[0].upper(),int(ordre[1]))
                    self.afficheLabyrinthe("La carte a été insérée en "+ordre[0].upper()+" "+ordre[1])                
                    finOrdre=True
            
            #xA,yA=self.saisirDeplacement()
            chemin=self.saisirDeplacementAnime()
            jc=self.labyrinthe.getJoueurCourant()
            xA,yA=self.animationChemin(chemin,jc)
            c=self.labyrinthe.plateau.getVal(xA,yA)
            t=self.labyrinthe.getTresorCourant()
            message=""
                
            if c.getTresor()==t:
                c.prendreTresor()
                if self.labyrinthe.joueurCourantTrouveTresor()==0:
                    message="Le joueur "+str(jc)+" a gagné"
                    fini=True
                else:
                    message="Le joueur "+str(jc)+" vient de trouver le trésor "+str(t)
            self.labyrinthe.changerJoueurCourant()
            self.afficheLabyrinthe(message)
    
        print("Merci au revoir")
    
g=LabyrintheModeTexte()
g.main()
