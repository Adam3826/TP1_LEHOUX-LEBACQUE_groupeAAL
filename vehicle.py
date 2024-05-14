import configparser
from datetime import datetime

class Vehicle:

	def __init__(self, filename):
         self.config = configparser.ConfigParser()
         self.config.read(filename)
         self.max_dist = self.config.getint('Vehicle', 'max_dist')
         self.capacity = self.config.getint('Vehicle', 'capacity')
         self.charge_fast = self.config.getint('Vehicle', 'charge_fast')
         self.charge_medium = self.config.getint('Vehicle', 'charge_medium')
         self.charge_slow = self.config.getint('Vehicle', 'charge_slow')
         self.start_time = self.config.get('Vehicle', 'start_time')
         self.end_time = self.config.get('Vehicle', 'end_time')
         self.duration = abs((datetime.strptime(self.end_time, '%H:%M') - datetime.strptime(self.start_time, '%H:%M')).seconds)
        