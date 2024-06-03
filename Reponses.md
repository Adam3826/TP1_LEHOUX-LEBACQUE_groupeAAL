# Réponses aux question

## Modélisation

NB : Nous définissons une tournée comme un circuit que fait un vehicule, commençant par un arrêt au dépôt et finissant au dépôt.
Ainsi, dans notre modélisation, un vahicule peut effectuer plusieurs tournées en une seule journée. 
 
### Variables de décision : 
- Affectation des vehicules (le vehicule i doit livrer le client j)
- Rechargement des vehicules (le vehicule i doit recharger au point i)
- L'ordre des visites (Visite)


### Contraintes : 
- Capacité max de chargement (à chaque instant un camion ne doit pas transporter plus que Capacity)
- Autonomie du vehicule (Il ne peux pas y avoir plus de x depuis le dernier chargement)
- Tous les clients doivent être livrés
- Un client ne doit être livré qu'une seule fois par un seul camion
- Les horaires de livraison (une tournée ne peut pas durer plus que start_time - end_time)

### Objectifs :
- Minimiser le temps de livraison (livrer tout le monde en le moins de temps possible)
- Minimiser le nombre de camions à posséder


## Représentation d'une solution :

Représenter l'ordonnancement d'une tournée par des objets Tournee ayant pour attribut une liste de visites.
Représenter le nombre de vehicules par la liste vehicules

## Evaluation d'une solution :
Pour une tournée vérifier : 
    La somme des demandes des clients visités n'excède pas la capacité **Capacity** (voir fonction isRealisableDemande(vehicule:Vehicle) dans main.py)
    La distance d'une tournée n'excede pas l'autonomie du vehicule (voir fonction isRealisableAutonomie(vehicule:Vehicle) dans main.py)
Pour un vehicule vérifier :
    La durée totale des affectations* d'un vehicule est inférieure à la durée d'une journée de travail. Avec notre modélisation, on rajoute un vehicule tant qu'on n'en a pas assez pour tout livrer en une journée. (fonction isAffectationRealisable(vehicule: Vehicle) dans main.py)
    (*nous appelons affectations d'un vehicule l'ensemble des tournées qui lui sont affectées)

## Instances sans solutions réalisables
Voici des instances pour lesquelles il n'existe pas de solution réalisables :
- Une liste de une visite dont la distance par rapport au dépôt est supérieure à l'autonomie du vehicule (5000km par exemple)
- Une liste de une visite dont la demande client est supérieure à la capacité du vehicule.
- Une liste de une visite dont la durée de trajet depuis le dépôt est supérieure à la durée d'une journée de travail (20h par exemple).

# Premières heuristiques

## Methode déterministe pour construire une solution qui passe par le dépôt autant de fois que nécessaire

Nous avons choisi la démarche suivante : 
Tant qu'il reste des clients à visiter faire :
    créer une tournée
    tant qu'on peut rajouter une visite dans la tournée sans dépasser la distance max et la capacité max :
        ajouter une visite à la tournée

Tel qu'implémentée dans notre code python, la complexité se calcule comme suit :
les lignes de code dont la complexité est en O(1) seront représentées avec "..."
On suppose que l'ajout d'un élément dans une liste avec append() ou le dépilement avec pop() sont de complexité en O(1)
    Partie créer les tournées :
    while len(visites) !=0: --> boucle répétée n fois (avec n nombre de visites)
        ... --> O(1)
        while visite_suivante := jePeuxRajouterUnClient(tournee, visites):  --> boucle répétée n fois au pire des cas
            ... --> O(1)
        # s'assurer qu'on puisse retourner au dépôt
        while not tournee.canAddVisite(depot): --> au pire des cas n fois
            tournee.visites.pop(-1)
    Pour cette première partie, on a une complexité en O(n) * (O(n) + O(n)) = O(n) * O(n) 
    = O(n²)
    
    Partie affecter les tournées :
     while len(pileTournees) != 0: --> n fois
        ...
        while unVehicule.canAffect(pileTournees[0]):  --> n fois dans le pire des cas
            unVehicule.affect(pileTournees[0]) --> vehicule.affect(liste) appelle la fonction affectation.addTournee() qui elle même appelle la fonction computeTemps(). Or la fonction compute temps a une complexité en O(n)
            ...
    En résumé : O(n) * O(n) * O(n) (on ne note pas les O(1) à chaque fois)

    Cette partie a une complexité en O(n^3)

    Les deux parties se succèdent. L'algorithme complet a donc une complexité de O(n^2) + O(n^3) = O(n^3)
    Nous avons effectivement une complexité polynomiale.

## Instances (Questions 1.b et 1.c)

- L'instance lyon_100_3_1 nécessite plus qu'un vehicule.
- Une instance contenant une seule visite de demande 1 et de distance 10 est affectée à un seul vehicule avec notre algorithme. Il s'agit d'un cas où la solution de notre algorithme est la solution optimale.

# Question 2 : heuristiques non déterministes

Nous avons choisi de mélanger la liste des visites avant la création des tournées pour créer une variante non-déterministe de notre algorithme.


# TP 2

## Voisins

- Permutation dans une tournée (echange de deux visites d'une même tournée)
    --> La taille du voisinage est le nombre de permutations qui est de n(n - 1)/2 avec n le nombre de visites dans une tournée
        Démonstration : on prend le premier élément, on peut le permuter avec les n-1 autres de la tournée.
        On prend le deuxième élément, on peut le permuter avec les n - 1 autres éléments de la tournée, mais on a déjà comptabilisé sa permutation avec le premier élément.
        On prend le troisième élément et ainsi de suite. Si on compte, on obtient
        (n - 1) + (n - 2) + ... + (n - n)
        la somme des entiers de 0 à n - 1
    --> La taille de ce voisinage est effectivement polynomiale (uniquement des sommes de puissances de n multipliées par des constantes)
    --> Ce voisinage peut contenir des solutions non réalisables. Changer l'ordre de passage peut changer la durée et la distance de la tournée.

- Ajouter une visite dans une tournée (depuis une autre tournée)
    --> La taille du voisinage est de au plus n avec n le nombre total de visites.
    --> La taille de ce voisinage est polynomiale
    --> Ce voisinage peut contenir des solutions non réalisables. Il peut ajouter des visites à une tournée déjà pleine.

- Permutation entre deux tournées (echange de deux visites de tournées différentes)
    --> La taille de ce voisinage est de n avec n la taille de l'instance. 
    --> La taille de ce voisinage est polynomiale
    --> Ce voisinage peut contenir des solutions non réalisables. Une tournée déjà pleine peut se retrouver à echanger une visite de faible demande avec une visite de plus forte demande, excédant la capacité du vehicule.