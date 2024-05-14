'''
Basic script.
main function is executed only if you execute the script,
not when you import the module.

@author: vlehoux
'''
import csv
from typing import Dict, List
from affectation import Affectation
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

def jePeuxRajouterUnClient(tournee: Tournee, visites: Dict[int, Visite]) -> Visite:
    for uneVisite in visites.values():
        if tournee.canAddVisite(uneVisite):
            return uneVisite
    return None
    
def main(): 
    visites = lire_visites_de_csv("visits.csv")

    depot: Visite = visites.pop(0)
 
    vehicule = Vehicle('vehicle.ini')
    
    Tournees = []
    print("taile visit avant : "+ str(len(visites))) 

    while len(visites) !=0:
        tournee = Tournee(depot, vehicule)
        while visite_suivante := jePeuxRajouterUnClient(tournee, visites):
            tournee.addVisite(visite_suivante)
            print("\n visite suivante ID : " + str(visite_suivante.visitID) + ", distance tournée : " + str(tournee.distance) + "km, chargement tournée : " +  str(tournee.chargement))
            visites.pop(visite_suivante.visitID)
        # s'assurer qu'on puisse retourner au dépôt
        while not tournee.canAddVisite(depot):
            tournee.visites.pop(-1)

        tournee.addVisite(depot)

        Tournees.append(tournee)
        
        print("\n distance tournée : " + str(tournee.distance) + "km, chargement tournée : " +  str(tournee.chargement))

        print("taile visit après : "+ str(len(visites))) 

        print(str(tournee))
        print("durée : " + str(tournee.duree/3600) + " heures")
    

    print("durée d'une journée : " + str(tournee.vehicule.duration/3600) + " heures")
    print("--------------------------------------------------------------")
    for tourne in Tournees:
        print("\n "+ str(tourne))

    print("\n-----------------\n")
    affectation = Affectation(tournee)


if __name__ == '__main__':
    main()
