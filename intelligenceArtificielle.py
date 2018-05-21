import numpy as np
import random
import time

import poidsEtBiais



HAUT = 0
BAS = 1
GAUCHE = 2
DROITE = 3
ZZZ = 4


class Reseau_Neurones:

    ## Initialisation des poids et des biais
    ## En fonction d'un entrainement fait précédemment
    def __init__(self):
        self.biais = poidsEtBiais.biais
        self.poids = poidsEtBiais.poids


    ## Prend en entrée un numpy.array
    ## Retourne numpy.array
    def propagation(self, a):
        for b, p in zip(self.biais, self.poids):
            a = sigmoide(np.dot(p, a)+b)
        return a


class IA_Ouvriers:
    def __init__(self):
        self.r = Reseau_Neurones()


    ## prend en entrée les 9 cases qui entourent l'ouvrier
    ## retourne ZZZ,HAUT,BAS,GAUCHE,DROITE
    def deplacement(self,cases):
        ## sortie :: [HAUT,BAS,GAUCHE,DROITE,ZZZ,RANDOM]
        sortie = self.r.propagation(np.array(cases).reshape(9,1)).reshape(1,6).tolist()[0]

        valTotal = 0
        for i in range(len(sortie)):
            valTotal = valTotal + sortie[i]

        for i in range(len(sortie)):
            sortie[i] = sortie[i]/valTotal

        for i in range(len(sortie)):
            sortie[i]=sortie[i] + sortie[5]/5

        sortie = sortie[:5]

        rand = random.random()

        for i in range(len(sortie)):
            rand = rand - sortie[i]
            if rand < 0:
                return i
            



def sigmoide(z):
    return 1.0/(1.0+np.exp(-z))
