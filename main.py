'''
Basic script.
main function is executed only if you execute the script,
not when you import the module.

@author: vlehoux
'''
import csv
from typing import Dict, List
from tournee import Tournee
from vehicle import Vehicle

from visite import Visite
def lire_visites_de_csv(nom_fichier):
    visites: Dict[int, Visite] = {}
    with open(nom_fichier, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            visit_id, visit_name, _, _, demand = row
            # Convertir demand et visit_id en entier
            demand = int(demand)
            visit_id = int(visit_id)
            # Instancier la classe Visite avec les données de chaque ligne
            visite = Visite(visit_id, visit_name, demand)
            visites[visite.visitID] = visite
    return visites

def jePeuxRajouterUnClient(tournee: Tournee, visites: Dict[int, Visite], monVehicule: Vehicle) -> Visite:
    for uneVisite in visites.values():
        if uneVisite.demand + tournee.chargement <=  monVehicule.capacity and tournee.distance + tournee.getLastVisite().getDistanceToVisit(uneVisite) <= monVehicule.max_dist:
            return uneVisite
    return None
    
def main(): 
    visites = lire_visites_de_csv("visits.csv")
    
    tournee = Tournee(visites[0])
    visites.pop(0)
    vehicule = Vehicle('vehicle.ini')

    while visite_suivante := jePeuxRajouterUnClient(tournee, visites, vehicule):
        tournee.addVisite(visite_suivante)
        print(visite_suivante.visitID, tournee.distance, tournee.chargement)
        visites.pop(visite_suivante.visitID)

    print(str(tournee))


if __name__ == '__main__':
    main()
