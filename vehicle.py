import configparser

class Vehicle:

	def __init__(self, filename):
         self.config = configparser.ConfigParser()
         self.config.read(filename)
         self.max_dist = self.config.getint('Vehicle', 'max_dist')
         self.capacity = self.config.getint('Vehicle', 'max_dist')
         self.charge_fast = self.config.getint('Vehicle', 'max_dist')
         self.charge_medium = self.config.getint('Vehicle', 'max_dist')
         self.charge_slow = self.config.getint('Vehicle', 'max_dist')
         self.start_time = self.config.get('Vehicle', 'max_dist')
         self.end_time = self.config.get('Vehicle', 'max_dist')
