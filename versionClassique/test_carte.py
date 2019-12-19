#!/usr/bin/python3
import unittest
import sys
import copy
from unittest.mock import patch

import carte
class TestCarte(unittest.TestCase):
    def setUp(self):
        self.O=8
        self.S=4
        self.E=2
        self.N=1        
        self.liste_cartes=[]
        self.liste_cartes_droite=[]
        for i in range(16):
            self.liste_cartes.append(carte.Carte(i&self.N==self.N,i&self.E==self.E,i&self.S==self.S,i&self.O==self.O))
            self.liste_cartes_droite.append(carte.Carte(i&self.O==self.O,i&self.N==self.N,i&self.E==self.E,i&self.S==self.S))
            
        
    def test_estValide(self):
        for i in range(16):
            if i in [7,11,13,14,15]:
                self.assertFalse(carte.estValide(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+
                                 "ne devrait pas être valide car elle ne possède qu'une ou 0 ouverture")
            else:
                self.assertTrue(carte.estValide(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+
                                 "devrait être valide car elle possède 2, 3 ou 4 ouvertures")
                
    def test_murNord(self):
        for i in range(13):
            if i not in (7,11):
                if i&self.N==self.N:
                    self.assertTrue(carte.murNord(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" devrait posséder un mur au nord")
                else:
                    self.assertFalse(carte.murNord(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" ne devrait pas posséder de mur au nord")


    def test_murSud(self):
        for i in range(13):
            if i not in (7,11):
                if i&self.S==self.S:
                    self.assertTrue(carte.murSud(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" devrait posséder un mur au sud")
                else:
                    self.assertFalse(carte.murSud(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" ne devrait pas posséder de mur au sud")

    def test_murOuest(self):
        for i in range(13):
            if i not in (7,11):
                if i&self.O==self.O:
                    self.assertTrue(carte.murOuest(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" devrait posséder un mur à l'ouest")
                else:
                    self.assertFalse(carte.murOuest(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" ne devrait pas posséder de mur à l'ouest")


    def test_murEst(self):
        for i in range(13):
            if i not in (7,11):
                if i&self.E==self.E:
                    self.assertTrue(carte.murEst(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" devrait posséder un mur à l'est")
                else:
                    self.assertFalse(carte.murEst(self.liste_cartes[i]),"la carte "+str(self.liste_cartes[i])+" ne devrait pas posséder de mur à l'est")

    def test_listePions(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,pions=[1,3])
        self.assertEqual(carte.getListePions(c1),[],"la carte "+str(c1)+" devrait avoir une liste de pions vide\n"+
                         "Le problème vient sans doute de la fonction Carte")
        self.assertEqual(carte.getListePions(c2),[1,3],"la carte "+str(c2)+" devrait avoir une liste de pions égale à [1,3]\n"+
                         "Le problème vient sans doute de la fonction Carte lorsque le paramètre pions est instancié à une liste non vide")
        carte.setListePions(c1,[1,2])
        self.assertEqual(carte.getListePions(c1),[1,2],"la carte "+str(c1)+" devrait avoir une liste de pions égale à [1,2]\n"+
                         "Le problème vient sans doute de la fonction setListePions")
        carte.setListePions(c2,[])
        self.assertEqual(carte.getListePions(c2),[],"la carte "+str(c2)+" devrait avoir une liste de pions égale à [1,2]\n"+
                         "Le problème vient sans doute de la fonction setListePions")
        
    def test_getNbPions(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,pions=[1,3])
        self.assertEqual(carte.getNbPions(c1),0,"la carte "+str(c1)+" devrait avoir un nombre de pions égal à 0\n"+
                         "Le problème vient sans doute de la fonction Carte")
        self.assertEqual(carte.getNbPions(c2),2,"la carte "+str(c2)+" devrait avoir un nombre de pions égal à 2\n"+
                         "Le problème vient sans doute de la fonction Carte lorsque le paramètre pions est instancié à une liste non vide")

    def test_possede_Pion(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,pions=[1,3])
        for i in range(1,5):
            self.assertFalse(carte.possedePion(c1,i),"la carte "+str(c1)+" ne possède pas le pion "+str(i)+"\n"+
                             "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")
        for i in range(1,5):
            if i==1 or i==3:
                self.assertTrue(carte.possedePion(c2,i),"la carte "+str(c2)+" possède bien le pion "+str(i)+"\n"+
                                "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")
            else:
                self.assertFalse(carte.possedePion(c2,i),"la carte "+str(c2)+" ne possède pas le pion "+str(i)+"\n"+
                                 "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")
        
    def test_possede_pendre_Pion(self):
        c1=carte.Carte(True,False,True,False,pions=[1,3])
        for nb in range(2):
            carte.prendrePion(c1,3)
            for i in range(1,5):
                if i==1:
                    self.assertTrue(carte.possedePion(c1,i),"la carte "+str(c1)+" possède bien le pion "+str(i)+"\n"+
                                    "Le problème vient sans doute de la fonction prendrePion ou de la fonction possedePion")
                else:
                    self.assertFalse(carte.possedePion(c1,i),"la carte "+str(c1)+" ne possède pas le pion "+str(i)+"\n"+
                                     "Le problème vient sans doute de la fonction prendrePion ou de la fonction possedePion")
        
    def test_possede_poser_Pion(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,pions=[1,3])
        carte.poserPion(c1,2)
        for i in range(1,5):
            if i==2:
                self.assertTrue(carte.possedePion(c1,i),"la carte "+str(c1)+" possède bien le pion "+str(i)+"\n"+
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
            else:
                self.assertFalse(carte.possedePion(c1,i),"la carte "+str(c1)+" ne possède pas le pion "+str(i)+"\n"+
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
        carte.poserPion(c2,4)
        for i in range(1,5):
            if i==1 or i==3 or i==4:
                self.assertTrue(carte.possedePion(c2,i),"la carte "+str(c2)+" possède bien le pion "+str(i)+"\n"+
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
            else:
                self.assertFalse(carte.possedePion(c2,2),"la carte "+str(c2)+" ne possède pas le pion "+str(i)+"\n"+
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
                
    def test_tournerHoraire(self):
        for i in range(13):
            if i not in (7,11):
                c=copy.deepcopy(self.liste_cartes[i])
                carte.tournerHoraire(c)
                self.assertEqual(c,self.liste_cartes_droite[i],"problème avec la fonction l'appel tournerHoraire("+
                                 str(self.liste_cartes[i])+")\nRésultat attendu "+str(self.liste_cartes_droite[i])+
                                 "\nRésultat obtenu "+str(c))
    
    
    def test_tournerAntiHoraire(self):
        for i in range(13):
            if i not in (7,11):
                c=copy.deepcopy(self.liste_cartes_droite[i])
                carte.tournerAntiHoraire(c)
                self.assertEqual(c,self.liste_cartes[i],"problème avec la fonction l'appel tournerAntiHoraire("+
                                 str(self.liste_cartes_droite[i])+")\nRésultat attendu "+str(self.liste_cartes[i])+
                                 "\nRésultat obtenu "+str(c))
                
    def test_getTresor(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,10)
        self.assertEqual(carte.getTresor(c1),0,"la carte "+str(c1)+" ne possède aucun trésor => valeur attendue 0\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction getTresor")
        self.assertEqual(carte.getTresor(c2),10,"la carte "+str(c2)+" possède le trésor 10 => valeur attendue 10\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction getTresor")
        
    def test_getTresor_mettreTresor(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,10)
        self.assertEqual(carte.mettreTresor(c1,5),0,"la carte "+str(c1)+" ne possèdait aucun trésor => valeur attendue 0\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction mettreTresor")
        self.assertEqual(carte.getTresor(c1),5,"la carte "+str(c1)+" doit posséder le trésor 5\n"+
                         "Le problème vient sans doute de la fonction mettreTresor ou de la fonction getTresor")
        self.assertEqual(carte.mettreTresor(c2,7),10,"la carte "+str(c2)+" possédait le trésor 10 => valeur attendue 10\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction mettreTresor")
        self.assertEqual(carte.getTresor(c2),7,"la carte "+str(c2)+" doit posséder le trésor 7\n"+
                         "Le problème vient sans doute de la fonction mettreTresor ou de la fonction getTresor")
    
    def test_getTresor_prendreTresor(self):
        c1=carte.Carte(True,False,True,False)
        c2=carte.Carte(True,False,True,False,10)
        self.assertEqual(carte.prendreTresor(c1),0,"la carte "+str(c1)+" ne possèdait aucun trésor => valeur attendue 0\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction prendreTresor")
        self.assertEqual(carte.getTresor(c1),0,"la carte "+str(c1)+" ne devrait plus posséder de trésor \n"+
                         "Le problème vient sans doute de la fonction prendreTresor ou de la fonction getTresor")
        self.assertEqual(carte.prendreTresor(c2),10,"la carte "+str(c2)+" possédait le trésor 10 => valeur attendue 10\n"+
                         "Le problème vient sans doute de la fonction Carte ou de la fonction prendreTresor")
        self.assertEqual(carte.getTresor(c2),0,"la carte "+str(c2)+" ne devrait plus posséder de trésor \n"+
                         "Le problème vient sans doute de la fonction prendreTresor ou de la fonction getTresor")
        
    def test_coderMurs(self):
        for i in range(16):
            res=carte.coderMurs(self.liste_cartes[i])
            self.assertEqual(res,i,"la carte "+str(self.liste_cartes[i])+
                                       " devrait avoir pour code "+str(i)+ " mais coderMur a retourné "+str(res))
    
    def test_decoderMurs(self):
        c=carte.Carte(True,True,True,True)
        for i in range(16):
            carte.decoderMurs(c,i)
            self.assertEqual(c,self.liste_cartes[i],"le resultat de decoderMur avec le code "+str(i)+
                             " aurait du donner "+str(self.liste_cartes[i])+" mais on a obtenu "+str(c))
            
    
        
    def test_toChar(self):
        for i in range(16):
            carac=carte.toChar(self.liste_cartes[i])
            self.assertEqual(carac,carte.listeCartes[i],"la carte "+str(self.liste_cartes[i])+
                             " devrait avoir pour caractère "+carte.listeCartes[i]+ " mais toChar retourne "+str(carac))

    def message_passage(self,direction,existe,c1,c2):
        commun=" passage direction "+direction+" entre "+str(c1)+" et "+str(c2) +" mais la fonction passage"+\
                   direction+" "
        if existe:
            return "il existe un"+commun+"ne le trouve pas"
        else:
            return "il n'existe pas de"+commun+"en trouve un"
        
    def test_passageNord(self):
        for i in range(13):
            if i not in (7,11):
                for j in range(13):
                    if j not in (7,11):
                        passage=i&self.N==0 and j&self.S==0
                        self.assertEqual(carte.passageNord(self.liste_cartes[i],self.liste_cartes[j]),passage,
                                         self.message_passage("Nord",passage,self.liste_cartes[i],self.liste_cartes[j]))
            
    def test_passageSud(self):
        for i in range(13):
            if i not in (7,11):
                for j in range(13):
                    if j not in (7,11):
                        passage=i&self.S==0 and j&self.N==0
                        self.assertEqual(carte.passageSud(self.liste_cartes[i],self.liste_cartes[j]),passage,
                                         self.message_passage("Sud",passage,self.liste_cartes[i],self.liste_cartes[j]))

    def test_passageEst(self):
        for i in range(13):
            if i not in (7,11):
                for j in range(13):
                    if j not in (7,11):
                        passage=i&self.E==0 and j&self.O==0
                        self.assertEqual(carte.passageEst(self.liste_cartes[i],self.liste_cartes[j]),passage,
                                         self.message_passage("Est",passage,self.liste_cartes[i],self.liste_cartes[j]))
    def test_passageOuest(self):
        for i in range(13):
            if i not in (7,11):
                for j in range(13):
                    if j not in (7,11):
                        passage=i&self.O==0 and j&self.E==0
                        self.assertEqual(carte.passageOuest(self.liste_cartes[i],self.liste_cartes[j]),passage,
                                         self.message_passage("Ouest",passage,self.liste_cartes[i],self.liste_cartes[j]))

        
if __name__ == '__main__':
    unittest.main()
