'''
Basic script.
main function is executed only if you execute the script,
not when you import the module.

@author: vlehoux
'''
import csv
from tournee import Tournee
from vehiicle import Vehicle

from visite import Visite
def lire_visites_de_csv(nom_fichier):
    visites = []
    with open(nom_fichier, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            visit_id, visit_name, _, _, demand = row
            # Convertir demand en entier
            demand = int(demand)
            # Instancier la classe Visite avec les données de chaque ligne
            visite = Visite(visit_id, visit_name, demand)
            visites.append(visite)
    return visites

def jePeuxRajouterUnClient(tournee, visites, monVehicule):
    capacityOk = False
    distanceOk = False
    #vérifier que la capacité du vehicule n'est pas dépassée
    demandeTotale = 0
    for etape in tournee.visites:
        demandeTotale += etape.demande
    for uneVisite in visites:
        if uneVisite.demande + demandeTotale <= monVehicule.capacity and tournee.getDistance() + uneVisite.getDistance() <= monVehicule.maxDist:
            return True, uneVisite
    return False, None
    
def main():
    
    visites = lire_visites_de_csv("visits.csv")

    print("Hello word!\n")
    print(" visite 1 : " + str(visites[1])) # mesVisites[0]

    tournee = Tournee([visites[0]])
    vehicule = Vehicle('vehicle.ini')

    visites[0]


if __name__ == '__main__':
    main()
