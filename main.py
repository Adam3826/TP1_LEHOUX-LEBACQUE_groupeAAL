'''
Basic script.
main function is executed only if you execute the script,
not when you import the module.

@author: vlehoux
'''
import csv
import random
import copy
from typing import Dict, List
from affectation import Affectation
from tournee import Tournee
from vehicle import Vehicle

from visite import Visite



##############################################################################################################################################################################
########             Vérifier qu'une solution est réalisable
##############################################################################################################################################################################
def isAffectationRealisable(vehicule: Vehicle):
    res = vehicule.affectation.tempsTotal < vehicule.duration
    return res

def isRealisableAutonomie(vehicule:Vehicle):
    for tournee in vehicule.affectation.tournees:
        if(tournee.distance > vehicule.max_dist):
            return False
    return True
def isRealisableDemande(vehicule:Vehicle):
    for tournee in vehicule.affectation.tournees:
        if(tournee.chargement > vehicule.capacity):
            return False
    return True



##############################################################################################################################################################################
########             Evaluer une solution
##############################################################################################################################################################################
# dans notre système de cout, un vehicule en moins est équivalent à 2h de moins de durée de livraison
# plus 
def eval(vehicules: List[Vehicle]):
    cout = maxDureeTournees(vehicules) + len(vehicules) * 2 * 3600   
    return cout

###########################################################################################################################################
#########           Voisinages
#########################################################################################################################################

        ########### Voisinages déterministes #####################
# voisinageD1(vehicules)
# prend en argument une liste de vehicules (notre solution), retourne de manière  déterministe la liste de tous les voisins de type 1 (permutation au sein d'une tournée)
# attention, le dépot ne peut pas être permuté
def voisinageD1(vehicules: List[Vehicle]):
    voisinage = []
    vehiculesCopy = []
    for k in range(len(vehicules) -1):#vehicule in vehicules:
        for p in range(len(vehicules[k].affectation.tournees) -1):#tournee in vehicule.affectation.tournees:
            for i in range(1, len(vehicules[k].affectation.tournees[p].visites) - 3):
                for j in range(i + 1, len(vehicules[k].affectation.tournees[p].visites) - 2):
                    isVoisinRealisable = True
                    vehiculesCopy = copy.deepcopy(vehicules)
                    tourneeAPermuter = vehiculesCopy[k].affectation.tournees[p]
                    tourneeAPermuter.visites[i], tourneeAPermuter.visites[j] = tourneeAPermuter.visites[j], tourneeAPermuter.visites[i]
                    visitesAReCalculer = tourneeAPermuter.visites
                    maTournee = Tournee(visitesAReCalculer.pop(0), vehicules[k])
                    for visite in visitesAReCalculer:
                        if(maTournee.canAddVisite(visite)):
                            maTournee.addVisite(visite)
                        else:
                            isVoisinRealisable = False
                            break

                    if(isVoisinRealisable):
                        vehiculesCopy[k].affectation.tournees[p] = maTournee
                        vehiculesCopy[k].affectation.tempsTotal =  vehiculesCopy[k].affectation.computeTemps()
                        voisinage.append(vehiculesCopy)


            
            
    return voisinage

def getMeilleurVoisinD1(voisinage: List[List[Vehicle]]):
    meilleurVoisin = voisinage[0]
    meileureEval = eval(meilleurVoisin)    
    for voisin in voisinage:
        if(eval(voisin) < meileureEval):
            meileureEval = eval(voisin)
            meilleurVoisin = voisin

    return meilleurVoisin

# prend en argument une liste de vehicules (notre solution), retourne de manière  déterministe le voisin de type 1 (permutation au sein d'une tournée) qui améloire au mieux la solution
def getMeilleurVoisin(voisinage: List[List[Vehicle]]):
    
    cout = eval(voisinage[0])
    res = voisinage[0]
    for voisin in voisinage:
        if(eval(voisin) < cout):
            cout = eval(voisin)
            res = voisin
    return res





# voisinageND1(vehicules)
#prend en argument une liste de vehicules, retourne de manière non déterministe un voisin de type 1 (permutation au sein d'une tournée)
# On prend un vehicule au hazard, on prend l'une de ses tournées au hazard, on y echange de place 2 visites au hazard
def voisinageND1(vehicules: List[Vehicle]):
    random.shuffle(vehicules)
    random.shuffle(vehicules[0].affectation.tournees)
    random.shuffle(vehicules[0].affectation.tournees[0].visites)
    return vehicules











def lire_visites_de_csv(nom_fichier):
    visites = []
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
            visites.append(visite)
    return visites

def jePeuxRajouterUnClient(tournee: Tournee, visites: List[Visite]) -> Visite:
    for uneVisite in visites:
        if tournee.canAddVisite(uneVisite):
            return uneVisite
    return None
def maxDureeTournees(vehicules: List[Vehicle]):
    max = 0
    for vehicule in vehicules:
        if vehicule.affectation.tempsTotal > max:
            max = vehicule.affectation.tempsTotal
        
    return max
    
def main(): 
    visites = lire_visites_de_csv("visits.csv")

    depot: Visite = visites.pop(0)
    # TP 1 Question 2 : décommentez la ligne ci-dessous pour l'heuristique non-déterministe
    # TP 2 Question 3 : décommentez la ligne ci-dessous pour l'heuristique non-déterministe
    #random.shuffle(visites)
 
    vehicule = Vehicle('vehicle.ini')
    
    Tournees = []
    
##################################### Créer les tournées pour toutes les visites ###################################################################################
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n Créer les tournées pour toutes les visites")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    while len(visites) !=0:
        tournee = Tournee(depot, vehicule)
        while visite_suivante := jePeuxRajouterUnClient(tournee, visites):
            tournee.addVisite(visite_suivante)
            print("\n visite suivante ID : " + str(visite_suivante.visitID) + ", distance tournée : " + str(tournee.distance) + "km, chargement tournée : " +  str(tournee.chargement))
            visites.remove(visite_suivante)
        # s'assurer qu'on puisse retourner au dépôt
        while not tournee.canAddVisite(depot):
            tournee.visites.pop(-1)

        tournee.addVisite(depot)

        Tournees.append(tournee)
        
        print("\n distance tournée : " + str(tournee.distance) + "km, chargement tournée : " +  str(tournee.chargement))

        print("taile visit après : "+ str(len(visites)))

        print(str(tournee))
        print("durée : " + str(tournee.duree/3600) + " heures")
        print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
        



##################################### FIN Créer les tournées pour toutes les visites ###################################################################################

    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n MODELISATION QUESTION 2 : représentation d'une tournée et de ses visites")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    numeroTournee = 0
    for tourne in Tournees:
        numeroTournee += 1
        print("\n Tournée n°"+ str(numeroTournee)+ "\n" + str(tourne))

    print("\n-----------------\n")
    affectation = Affectation(tournee)
    pileTournees = copy.deepcopy(Tournees)
    vehicules: list[Vehicle] = []

##################################### Affecter les tournées à des vehicules ###################################################################################

    while len(pileTournees) != 0:
        unVehicule: Vehicule = Vehicle('vehicle.ini')
        while unVehicule.canAffect(pileTournees[0]):
            unVehicule.affect(pileTournees[0])
            pileTournees.pop(0)
            if len(pileTournees) == 0:
                break
        vehicules.append(unVehicule)
##################################### FIN Affecter les tournées à des vehicules ###################################################################################
    nombreTournees = 1
    for monVehicule in vehicules:
        print("\n-----------------------------")
        print("\nmonVehicule numéro: " + str(nombreTournees) + "\n tournées :")
        
        for maTournee in monVehicule.affectation.tournees:
            nombreTournees += 1
            print("\n \tTournée : " + str(maTournee))
        
        nombreTournees = 1

    print("\n----------------------------------\-----------------\-----------------\-----------------\-----------------\\n")
    print("Résumé :\n")
    print("Nombre de vehicules necessaires pour livrer toutes les visites en une journée : " + str(len(vehicules)) +"\n")
    print("\n Durée necessaire pour accomplir toutes les visites : " + str(maxDureeTournees(vehicules)/3600) + " heures")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n-isAffectationRealisable ? : "+ str(isAffectationRealisable(vehicules[0])))


    ############################################################################################################""
    print("\n ------------------------------------------------------------------------------------") 
    print("\n ------------------------------------------------------------------------------------") 
    print("\n -----------------    Voisinage       ----------------------------------------") 

    ## TP 2 question 2 :
    print(" cout solution initiale : " + str(eval(vehicules)))
    print(" cout meilleur voisinage : " + str(eval(getMeilleurVoisin(voisinageD1(vehicules)))))
    
    # TP2 question 6
    maxDistance = 0 #Distance parcourue par le vehicule qui a parcouru le plus de km dans une journée
    for vehicule in vehicules:
        if(vehicule.affectation.getDistanceTotale() > maxDistance):
            maxDistance = vehicule.affectation.getDistanceTotale()
    print("\n Distance maximale parcourue par un seul véhicule : " + str(maxDistance))



if __name__ == '__main__':
    main()
