import configparser
from datetime import datetime




class Vehicle:
    def canAffect(self, tournee): #: Tournee
        return self.affectation.tempsTotal + tournee.duree + self.charge_medium <= self.duration
    def affect(self, tournee): #: Tournee
        self.affectation.addTournee(tournee)
        
    def __str__(self):
        res = ""
        for tournee in self.affectation.tournees:
            res += "\n" + str(tournee)
        return "Tournees : " + res
        

    def __init__(self, filename):
         from tournee import Tournee
         from affectation import Affectation
         self.config = configparser.ConfigParser()
         self.config.read(filename)
         self.max_dist = self.config.getint('Vehicle', 'max_dist')
         self.capacity = self.config.getint('Vehicle', 'capacity')
         self.charge_fast = self.config.getint('Vehicle', 'charge_fast') * 60
         self.charge_medium = self.config.getint('Vehicle', 'charge_medium') * 60
         self.charge_slow = self.config.getint('Vehicle', 'charge_slow') * 60
         self.start_time = self.config.get('Vehicle', 'start_time')
         self.end_time = self.config.get('Vehicle', 'end_time')
         self.duration = abs((datetime.strptime(self.end_time, '%H:%M') - datetime.strptime(self.start_time, '%H:%M')).seconds)
         self.affectation: Affectation = Affectation(None)
         
        
    