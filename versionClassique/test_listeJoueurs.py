#!/usr/bin/python3
import unittest
import sys
import copy
from unittest.mock import patch

import listeJoueurs
import joueur
class TestListeJoueurs(unittest.TestCase):
    def setUp(self):
        self.liste_noms=[["test1","test2","test3","test4"],
                          ["essai2","essai4"]]
        
        
    def test_Joueur(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            jo=joueur.Joueur(noms[0])
            nbj=listeJoueurs.getNbJoueurs(liste_joueurs)
            self.assertEqual(nbj,len(noms),"La liste de joueur crée à partir de "+str(noms)+" devrait contenir "+
                             str(len(noms))+" joueurs mais la fonction getNbJoueurs retourne "+str(nbj)+
                             "\nCela peut provenir des fonctions ListeJoueurs ou getNbJoueurs")
            jc=listeJoueurs.getJoueurCourant(liste_joueurs)
            self.assertEqual(jc,jo,"La liste de joueur crée à partir de "+str(noms)+" devrait avoir pour joueur courant "+
                             str(jo)+" mais la fonction getJoueurCourant retourne "+str(jc)+
                             "\nCela peut provenir des fonctions ListeJoueurs ou getJoueurCourant")

            
    def test_ajouterJoueur(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs([])
            cpt=0
            nbj=listeJoueurs.getNbJoueurs(liste_joueurs)
            self.assertEqual(nbj,cpt,"La liste de joueur crée à partir de [] devrait contenir aucun joueur mais "+
                             "la fonction getNbJoueurs retourne "+str(nbj)+
                             "\nCela peut provenir des fonctions ListeJoueurs ou getNbJoueurs")
            for nom in noms:
                cpt+=1
                listeJoueurs.ajouterJoueur(liste_joueurs,joueur.Joueur(nom))
                nbj=listeJoueurs.getNbJoueurs(liste_joueurs)
                self.assertEqual(nbj,cpt,"La liste de joueur devrait contenir "+str(cpt)+" joueur(s) mais "+
                             "la fonction getNbJoueurs retourne "+str(nbj)+
                             "\nCela peut provenir des fonctions  ajouterJoueur ou getNbJoueurs")


    def test_changerJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            taille=len(noms)
            for i in range(6):
                jca=joueur.Joueur(noms[i%taille])
                jc=listeJoueurs.getJoueurCourant(liste_joueurs)
                self.assertEqual(jc,jca,"Le joueur courant de la liste joueur créée à partir de "+str(noms)+" au bout de "+str(i)+
                                 " tour(s) devrait être "+str(jca)+" mais la fonction getJoueurCourant retourne "+str(jc)+
                                 "\nCela peut provenir des fonctions ListeJoueurs, getJoueurCourant ou changerJoueurCourant")
                listeJoueurs.changerJoueurCourant(liste_joueurs)
        
        
    def test_numJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            taille=len(noms)
            for i in range(6):
                njc=listeJoueurs.numJoueurCourant(liste_joueurs)
                self.assertEqual(njc,i%taille+1,"Le numero du joueur courant de la liste joueur créée à partir de "+str(noms)+" au bout de "+str(i)+
                                 " tour(s) devrait être "+str(i%taille+1)+" mais la fonction getJoueurCourant retourne "+str(njc)+
                                 "\nCela peut provenir des fonctions ListeJoueurs, numJoueurCourant ou changerJoueurCourant")
                listeJoueurs.changerJoueurCourant(liste_joueurs)

    def test_nomJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            taille=len(noms)
            for i in range(6):
                njc=listeJoueurs.nomJoueurCourant(liste_joueurs)
                self.assertEqual(njc,noms[i%taille],"Le nom du joueur courant de la liste joueur créée à partir de "+str(noms)+" au bout de "+str(i)+
                                 " tour(s) devrait être "+str(noms[i%taille])+" mais la fonction getJoueurCourant retourne "+str(njc)+
                                 "\nCela peut provenir des fonctions ListeJoueurs, nomJoueurCourant ou changerJoueurCourant")
                listeJoueurs.changerJoueurCourant(liste_joueurs)


    def test_distribuerTresors(self):
        def recolter_tresor(jo):
            j=copy.deepcopy(jo)
            res=[]
            while joueur.getNbTresorsRestants(j)!=0:
                res.append(joueur.prochainTresor(j))
                joueur.tresorTrouve(j)
            return res
        
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            listeJoueurs.distribuerTresors(liste_joueurs,12,3)
            recolte=[]
            for i in range(len(noms)):
                tresors=recolter_tresor(listeJoueurs.getJoueurCourant(liste_joueurs))
                self.assertEqual(len(tresors),3,"La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir "+
                                 str(noms)+" devrait donner 3 trésors à chaque joueur or votre fonction a donné "+str(len(tresors))+
                                 " au joueur "+str(i+1)+
                                 "\nCela peut provenir des fonctions ListeJoueurs, distribuerTresors ou getJoueurCourant")
                recolte.extend(tresors)
                listeJoueurs.changerJoueurCourant(liste_joueurs)
            recolte.sort()
            for i in range(len(recolte)-1):
                self.assertIn(recolte[i],list(range(1,13)),"La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir "+
                                 str(noms)+" a distribué un trésor inconnu "+str(recolte[i]))
                self.assertTrue(recolte[i]!=recolte[i+1],"La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir "+
                                 str(noms)+" a distribué deux fois le même trésor "+str(recolte[i]))
            self.assertIn(recolte[len(recolte)-1],list(range(1,13)),"La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir "+
                          str(noms)+" a distribué un trésor inconnu "+str(recolte[len(recolte)-1]))
            
            
    def test_joueurCourantTrouveTresor(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            listeJoueurs.distribuerTresors(liste_joueurs,16,4)
            cpt=4
            for i in range(4):
                cpt-=1
                for j in range(len(noms)):
                    jo=copy.deepcopy(listeJoueurs.getJoueurCourant(liste_joueurs))
                    joueur.tresorTrouve(jo)
                    listeJoueurs.joueurCourantTrouveTresor(liste_joueurs)
                    jo_res=listeJoueurs.getJoueurCourant(liste_joueurs)
                    nbt=joueur.getNbTresorsRestants(jo_res)
                    self.assertEqual(nbt,cpt,"Un joueur qui a trouvé "+str(i+1)+
                                     " trésor(s) sur 4 devrait en avoir "+str(cpt)+
                                     " à trouver mais la fonction getNbTresorsRestants retourne "+str(nbt)+
                                     "\nCela peut provenir des fonctions ListeJoueurs, changerJoueurCourant, distribuerTresors ou joueurCourantTrouveTresor") 
                    self.assertEqual(jo,jo_res,"Il y a une incohérence entre les fonctions tresorTrouve et joueurCourantTrouveTresor")
                    listeJoueurs.changerJoueurCourant(liste_joueurs)
                    
    def test_nbTresorsRestantsJoueur(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            listeJoueurs.distribuerTresors(liste_joueurs,16,4)
            for i in range(1,len(noms)+1):
                nbt=listeJoueurs.nbTresorsRestantsJoueur(liste_joueurs,i)
                self.assertEqual(nbt,4,"Après avoir distribué 4 trésor à chaque joueur,"+
                                 " nbTresorsRestantsJoueur devrait retourner 4 mais elle retourne "+ str(nbt)+
                                 " le joueur "+str(i)+
                                 "\nCela peut provenir des fonctions ListeJoueurs, distribuerTresors ou nbTresorsRestantsJoueur")
    def test_joueurCourantAFini(self):
        for noms in self.liste_noms:
            liste_joueurs=listeJoueurs.ListeJoueurs(noms)
            for i in range(1,len(noms)+1):
                self.assertTrue(listeJoueurs.joueurCourantAFini(liste_joueurs),"Le joueur courant de la liste "+
                                str(liste_joueurs)+ " n'a aucun trésor la fonction joueurCourantAFini devrait retourner True"+
                                "\nCela peut provenir des fonctions ListeJoueurs ou joueurCourantAFini")
                listeJoueurs.changerJoueurCourant(liste_joueurs)
            
            listeJoueurs.distribuerTresors(liste_joueurs,16,4)
            for i in range(1,len(noms)+1):
                self.assertFalse(listeJoueurs.joueurCourantAFini(liste_joueurs),"Le joueur courant de la liste "+
                                str(liste_joueurs)+ " a 4 trésors la fonction joueurCourantAFini devrait retourner True"+
                                "\nCela peut provenir des fonctions distribuerTresors ou joueurCourantAFini")
                listeJoueurs.changerJoueurCourant(liste_joueurs)
                
if __name__ == '__main__':
    print("*"*50)
    print("* ATTENTION! Note importante".ljust(48),"*")
    print("* les tests ne peuvent s'effectuer avant".ljust(48),"*")
    print("* d'avoir implémenté les fonctions ".ljust(48),"*")
    print("*"," "*10,"- ListeJoueurs".ljust(35),"*")
    print("*"," "*10,"- getNbJoueurs".ljust(35),"*")
    print("*"," "*10,"- getJoueurCourant".ljust(35),"*")
    print("*"*50)
    unittest.main()
