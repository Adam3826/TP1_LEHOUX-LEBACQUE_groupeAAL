'''
Classes basic example

@author: Vassilissa Lehoux
'''

from typing import List
import numpy as np

from tournee import Tournee

class Affectation(object):
    '''
    classdocs
    '''
    tempsTotal = -1

    def __init__(self, tournee: Tournee):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.tournees: List[Tournee] = []
        self.tempsTotal = 0
        if(tournee):
            self.tournees.append(tournee)
            self.tempsTotal = self.computeTemps()

    def computeTemps(self):
        res = 0
        for tournee in self.tournees:
            res += tournee.duree + 10*60 #On rajoute les 10 minutes de chargement entre chaque tournée
        
        return res
    
    def addTournee(self, tournee: Tournee):
        self.tournees.append(tournee)
        self.tempsTotal = self.computeTemps()

    def __str__(self):
        """
        custom object string representation
        """
        return "numeroVisite : " + str(self.visitID) +"\n visitName : " + str(self.visitName) + "\n demand : " + str(self.demand)
        
    
    def getDistanceToVisit(self, autreVisite: 'Visite'):
        try:
            with open('distances.txt', 'r') as file:
                lines = np.loadtxt(file)
                distance = float(lines[self.visitID][autreVisite.visitID])
                return distance
        except FileNotFoundError:
            print("Le fichier distances.txt n'a pas été trouvé.") 
            return None
        except IndexError:
            print("Erreur: Les données de distance pour ces visites ne sont pas disponibles.")
            return None
    def getDemand(self):
        return self.demand
        
    
    def getTempsVers(self, autreVisite):

        try:
            with open('times.txt', 'r') as file:
                lines = file.readlines()
                time = float(lines[self.visitID][autreVisite.visitID])
                return time
        except FileNotFoundError:
            print("Le fichier times.txt n'a pas été trouvé.")
            return None
        except IndexError:
            print("Erreur: Les données de temps pour ces visites ne sont pas disponibles.")
            return None

    
    @classmethod
    def getTempsChargement(self):
        loadingTime = self.demand * 10 + 5*60
        return loadingTime
