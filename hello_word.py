'''
Basic script.
main function is executed only if you execute the script,
not when you import the module.

@author: vlehoux
'''
import csv
from tournee import Tournee

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
def main():
    
    mesVisites = lire_visites_de_csv("visits.csv")

    print("Hello word!\n")
    print(" visite 1 : " + str(mesVisites[1])) # mesVisites[0]

    maTournee = Tournee(mesVisites[0:2])
    for etape in maTournee.visites:
        print(str(etape))


if __name__ == '__main__':
    main()
