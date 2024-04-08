'''
Classes basic example

@author: Vassilissa Lehoux
'''

class Tournee(object):
    '''
    classdocs
    '''
    visites = []
    distance = 0
    chargement = 0
    #class_var = "ex_class_var"  # attribute of the class, shared between instances

    def __init__(self, listeVisites):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.visites = listeVisites  # attribute different for each instance
        self.computeDistance()
        self.computeChargement()

    def addVisite(self, visite):
        self.visites.append(visite)
        
    def computeDistance(self):
        for i in range(len(self.visites) - 1):
            self.distance = self.distance + self.visites[i].getDistanceToVisit(self.visites[i+1])
        self.distance = self.distance + self.visites[-1].getDistanceToVisit(self.visites[0])

    def computeChargement(self):
        for i in range(len(self.visites) - 1):
            self.chargement = self.chargement + self.visites[i].getDemand()
        self.chargement = self.chargement + self.visites[-1].getDemand()
        self.chargement

    def getDistance(self):
        return self.distance
    
    def __str__(self):
        """
        custom object string representation
        """
        return "listeVisites : " + str(self.attribute1)

