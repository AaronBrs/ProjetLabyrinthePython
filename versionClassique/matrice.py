# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    Matrice3=dict()
    Matrice3['Nombre de lignes']=nbLignes
    Matrice3['Nombre de colonnes']=nbColonnes
    Matrice3['Liste de valeurs']=[valeurParDefaut]*nbLignes*nbColonnes
    return Matrice3

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice['Nombre de lignes']

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice['Nombre de colonnes']

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice['Liste de valeurs'][getNbColonnes(matrice)*ligne+colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice['Liste de valeurs'][getNbColonnes(matrice)*ligne+colonne]=valeur


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    indicedebutligne =  getNbColonnes(matrice)*numLig+(getNbColonnes(matrice)-getNbColonnes(matrice)) # 54
    indicefinligne   =  getNbColonnes(matrice)*numLig+(getNbColonnes(matrice)-1) # 62
    valeurexpulsee=getVal(matrice,numLig,0)
    matrice['Liste de valeurs'].pop(indicedebutligne)
    matrice['Liste de valeurs'].insert(indicefinligne)
    return valeurexpulsee

def Test(valeur):
    ligne6=[53,54,55,56,57,58,59,60,61,62,63]
    print(ligne6)
    ligne6.pop(9)
    print(ligne6)
    ligne6.insert(1,valeur)
    print(ligne6)
print (Test(84))

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramètres: matrice la matrice considérée
                numLig le numéro de la ligne à décaler
                nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    indicedebutligne =  getNbColonnes(matrice)*numLig+(getNbColonnes(matrice)-getNbColonnes(matrice)) # 54
    indicefinligne   =  getNbColonnes(matrice)*numLig+(getNbColonnes(matrice)-1) # 62
    valeurexpulsee=getVal(matrice,numLig,(getNbColonnes(matrice)-1))
    matrice['Liste de valeurs'].pop(indicedebutligne)
    matrice['Liste de valeurs'].insert(indicefinligne,nouvelleValeur)
    return valeurexpulsee

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramètres: matrice la matrice considérée
                numCol le numéro de la colonne à décaler
                nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """

    valeurexpulsee=getVal(matrice,0,numCol)#Sauvegarde de la valeur expulsée
    matrice['Liste de valeurs'].pop(numCol)#Expulsion de la valeur 
    
    for i in range(getNbLignes(matrice)-1):#boucle de 0 à 8
        valeur=getVal(matrice,i+1,numCol-1)#Valeur de la ligne d'en dessous
        matrice['Liste de valeurs'].insert(numCol+(i*getNbColonnes(matrice)),valeur)#Mouvement de la valeur vers le haut
        matrice['Liste de valeurs'].pop(getNbColonnes(matrice)*(i+1)+numCol)#Suppression de la valeur précédente
    
    matrice['Liste de valeurs'].insert(numCol+((getNbLignes(matrice)-1)*getNbColonnes(matrice)),nouvelleValeur)#Insertion de la nouvelle valeur sur la dernière ligne

    return valeurexpulsee

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """

    valeurexpulsee=getVal(matrice,getNbLignes(matrice)-1,numCol)#Sauvegarde de la valeur expulsée
    matrice['Liste de valeurs'].pop(getNbLignes(matrice)*getNbLignes(matrice)-1+numCol)#Expulsion de la valeur
    
    for i in range(getNbLignes(matrice)-1,0,-1):#Boucle de 8 à 1
        valeur=getVal(matrice,i-1,numCol)#Valeur de la ligne du dessus
        matrice['Liste de valeurs'].insert(getNbColonnes(matrice)*i+numCol,valeur)#Mouvement de la valeur vers le haut
        matrice['Liste de valeurs'].pop(getNbColonnes(matrice)*(i-1)+numCol)#Suppression de la valeur précédent
        
    matrice['Liste de valeurs'].insert(numCol,nouvelleValeur)#Insertion de la nouvelle valeur sur la premiere ligne
    return valeurexpulsee