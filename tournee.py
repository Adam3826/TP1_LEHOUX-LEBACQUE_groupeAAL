'''
Classes basic example

@author: Vassilissa Lehoux
'''

from typing import Dict, List
from visite import Visite
from vehicle import Vehicle


class Tournee(object):
    '''
    classdocs
    '''

    def tempsLivraison(self, visite: Visite):
        return visite.demand * 5 + 5*60
    
    def __init__(self, depart: Visite , vehicule: Vehicle):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.vehicule = vehicule
        self.distance = 0.0
        self.duree = 0
        self.visites: List[Visite] = []
        self.visites.append(depart)
        self.chargement = 0 + depart.demand

    def addVisite(self, visite: Visite):
        self.distance += self.getLastVisite().getDistanceToVisit(visite)
        self.duree += self.getLastVisite().getDureeTo(visite) + self.tempsLivraison(visite)
        self.visites.append(visite)
        self.chargement += visite.demand
    
    def canAddVisite(self, visite: Visite):
        checkDemande = visite.demand + self.chargement <= self.vehicule.capacity 
        checkDistance =  self.distance + self.getLastVisite().getDistanceToVisit(visite) <= self.vehicule.max_dist
        checkDuration = self.duree + self.getLastVisite().getDureeTo(visite) + self.tempsLivraison(visite) <= self.vehicule.duration
        return checkDemande and checkDistance and checkDuration

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
            # TODO ???

         return 0


    def __str__(self):
        """
        custom object string representation
        """
        return "listeVisites : " + ",".join(v.visitName for v in self.visites) + "\n Durée tournée : " + str(self.duree/3600) + " heures \n distance tournée : " + str(self.distance) + " km" #\n chargement tournée : " + str(self.chargement) + " kg

