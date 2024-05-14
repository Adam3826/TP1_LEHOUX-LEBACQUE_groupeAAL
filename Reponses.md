# Réponses aux question

## Modélisation
 
### Variables de décision : 
- Affectation des vehicules (le vehicule i doit livrer le client j)
- Rechargement des vehicules (le vehicule i doit recharger au point i)
- L'ordre des visites (Visite)


### Contraintes : 
- Capacité max de chargement (à chaque instant un camion ne doit pas transporter plus que Capacity)
- Autonomie du vehicule (Il ne peux pas y avoir plus de x depuis le dernier chargement)
- Les clients doivent être livrés
- Un client ne doit être livré qu'une seule fois par un seul camion
- Les horaires de livraison (une tournée ne peut pas durer plus que start_time - end_time)

### Objectifs :
- Minimiser le temps de livraison (livrer tout le monde en le moins de temps possible)
- Minimiser le nombre de camions à posséder


## Représentation d'une solution :

Représenter l'ordonnancement d'une tournée et le nombre de vehicules par des listes Li exemple : [4, 1, 7, charge_fast, 2, depot, 9]

## Evaluation d'une solution :
Pour une liste L vérifier : 
La somme des demandes des clients consécutifs n'excède pas la capacité **Capacity** 

## Voisins

- Permutation dans une tournée (echange de deux éléments d'une même tournée)
- Ajouter une visite dans une tournée (depuis une autre tournée)
- Permutation entre deux tournées (echange de deux éléments de tournées différentes)