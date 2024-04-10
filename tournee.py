'''
Classes basic example

@author: Vassilissa Lehoux
'''

from typing import Dict, List
from visite import Visite


class Tournee(object):
    '''
    classdocs
    '''
    distance = 0.0
    chargement = 0

    def __init__(self, depart: Visite):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.visites: List[Visite] = []
        self.visites.append(depart)
        self.chargement += depart.demand

    def addVisite(self, visite: Visite):
        self.visites.append(visite)
        self.chargement += visite.demand
        self.distance += self.getLastVisite().getDistanceToVisit(visite)
    
    def getLastVisite(self):
        return self.visites[-1]
        
    def computeDistance(self):
        for i in range(len(self.visites) - 1):
            self.distance = self.distance + self.visites[i].getDistanceToVisit(self.visites[i+1])
        self.distance = self.distance + self.visites[-1].getDistanceToVisit(self.visites[0])

    def computeChargement(self):
        for i in range(len(self.visites) - 1):
            self.chargement = self.chargement + self.visites[i].getDemand()
        self.chargement = self.chargement + self.visites[-1].getDemand()
        self.chargement

    # evaluer la solution
    def evalTemps(self):
        temps_livraison = -1

        for visite in self.visites:
            #visite.




         return 0


    def __str__(self):
        """
        custom object string representation
        """
        return "listeVisites : " + ",".join(v.visitName for v in self.visites)

