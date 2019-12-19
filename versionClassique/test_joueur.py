#!/usr/bin/python3
import unittest
import sys
import copy
from unittest.mock import patch

import joueur
class TestJoueur(unittest.TestCase):
    def setUp(self):
        ...
        
        
    def test_getNom(self):
        noms=["toto","azerty","nom23"]
        for nom in noms:
            j=joueur.Joueur(nom)
            nom_res=joueur.getNom(j)
            self.assertEqual(nom_res,nom,"Le nom du joueur "+str(j)+" devrait être "+nom+" et getNom a retourné "+str(nom_res)+
                             "\nCela peut provenir de la fonction getNom ou de la fonction Joueur")
        
    def test_getNbTresorsRestants(self):
        j=joueur.Joueur("test")
        for i in range(10):
            res=joueur.getNbTresorsRestants(j)
            self.assertEqual(res,i,"Le nombre de trésors du joueur "+str(j)+" devrait être "+str(i)+" mais getNbTresors a retourné "+str(res)+
                             "\nCela peut provenir des fonctions getNbTresorsRestants, ajouterTresor ou Joueur")
            joueur.ajouterTresor(j,i+1)
            
    def test_tresorTrouve(self):
        j=joueur.Joueur("test")
        liste_tresors=[2,8,4,6,10,14]
        for tresor in liste_tresors:
            joueur.ajouterTresor(j,tresor)
            
        for i in range(len(liste_tresors),0,-1):
            res=joueur.getNbTresorsRestants(j)
            self.assertEqual(res,i,"Le nombre de trésors du joueur "+str(j)+" devrait être "+str(i)+" mais getNbTresors a retourné "+str(res)+
                             "\nCela peut provenir des fonctions getNbTresorsRestants, tresorTrouve ou Joueur")
            joueur.tresorTrouve(j)
        res=joueur.getNbTresorsRestants(j)
        self.assertEqual(res,0,"Le nombre de trésors du joueur "+str(j)+" devrait être "+str(0)+" mais getNbTresors a retourné "+str(res)+
                             "\nCela peut provenir des fonctions getNbTresorsRestants, tresorTrouve ou Joueur")
            
    def test_prochainTresor(self):
        j=joueur.Joueur("test")
        liste_tresors=[2,8,4,6,10,14]
        for tresor in liste_tresors:
            joueur.ajouterTresor(j,tresor)
        for i in range(len(liste_tresors)):
            j_copie=copy.deepcopy(j)
            res=joueur.prochainTresor(j)
            self.assertEqual(res,liste_tresors[i],"Le prochain trésor du joueur "+str(j_copie)+" devrait être "+str(liste_tresors[i])+" mais prochainTresor a retourné "+str(res)+
                             "\nCela peut provenir des fonctions prochainTresor, tresorTrouve ou Joueur")
            joueur.tresorTrouve(j)
        j_copie=copy.deepcopy(j)
        res=joueur.prochainTresor(j)
        self.assertEqual(res,None,"Le joueur "+str(j_copie)+" ne devrait pas avoir de trésor à trouver mais prochainTresor a retourné "+str(res)+
                             "\nCela peut provenir des fonctions prochainTresor, tresorTrouve ou Joueur")
        
    def test_ajouterTresor(self):
        j=joueur.Joueur("test")
        liste_tresors=[(2,1),(6,2),(4,3),(6,3),(2,3),(14,4)]
        for tresor,nb_attendu in liste_tresors:
            joueur.ajouterTresor(j,tresor)
            res=joueur.getNbTresorsRestants(j)
            self.assertEqual(res,nb_attendu,"Le nombre de trésors du joueur "+str(j)+" devrait être "+str(nb_attendu)+" mais getNbTresors a retourné "+str(res)+
                             "\nCela peut provenir des fonctions getNbTresorsRestants, ajouterTresor ou Joueur")
        
if __name__ == '__main__':
    unittest.main()
