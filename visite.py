'''
Classes basic example

@author: Vassilissa Lehoux
'''

class Visite(object):
    '''
    classdocs
    '''
    visitID = -1
    visitName = "N/A"
    demand = -1
    def __init__(self, visitID, visitName, demand):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.visitID = visitID  
        self.visitName = visitName  
        self.demand = demand

    def __str__(self):
        """
        custom object string representation
        """
        return "numeroVisite : " + str(self.visitID) +"\n visitName : " + str(self.visitName) + "\n demand : " + str(self.demand)
        
    
    @classmethod
    def getDistanceToVisit(self, autreVisite):
        try:
            with open('distances.txt', 'r') as file:
                lines = file.readlines()
                distance = float(lines[self.visiteID][autreVisite.visiteID])
                return distance
        except FileNotFoundError:
            print("Le fichier distances.txt n'a pas été trouvé.")
            return None
        except IndexError:
            print("Erreur: Les données de distance pour ces visites ne sont pas disponibles.")
            return None
    def getDemand(self):
        return self.demand
        
    
    @classmethod
    def getTempsVers(self, autreVisite):

        try:
            with open('times.txt', 'r') as file:
                lines = file.readlines()
                distance = float(lines[self.visiteID][autreVisite.visiteID])
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
