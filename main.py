array = []

"""
[INPUT]
array   --> list        | Tableau contenant les données

jour    --> int (0-31)  | numéro du jour
mois    --> int (0-12)  | numéro du mois
annee   --> int         | Numéro de l'année

heure   --> int (0-12)  | numéro de l'heure
minute  --> int (0-59)  | numéro de la minute
seconde --> int (0-59)  | numéri de la seconde

Id      --> str         | Id du capteur
Data    --> float       | Valeurs du capteur
Type    --> str         | Type de donnée

[OUTPUT]
tab     --> list        | Tableau contenant les données
"""
def add(array, date, hour, Id, value, type):
    array.append([checkDate(date), checkHeure(hour), Id, value, type])

# Fonction qui affiche le tableau
def viewTab(array):
    i = 0
    string = 'Date\t\t\tHeure\t\t\tCapteur\t\t\tValeur\t\t\tType\n'
    while i < len(array):
        j = 0
        if i != 0:
            if array[i][0] != array[i-1][0]:
                string = string + '\nDate\t\t\tHeure\t\t\tCapteur\t\t\tValeur\t\t\tType\n'
        while j < len(array[i]):
            string = string + f'{array[i][j]}\t\t'
            j = j + 1
        i = i + 1
        string = string + '\n'
    print(string)



# Fonction qui vérifie le format de la date
def checkDate(date):
    a, m, j = date
    if (31 >= j >= 0) and (12 >= m >= 0):
        data = (int(a), int(m), int(j))
        return data
    print("Format de date invalide")
    return -1

# Fonction qui vérifie le format de l'heure
def checkHeure(heure):
    h, m, s = heure
    if (23 >= h >= 0) and (60 >= m >= 0) and (60 >= s >= 0):
        data = (int(h), int(m), int(s))
        return data
    print("Format de d'heure invalide")
    return -1

def sortDate(date1, date2):
    if date1 < date2:
        return True
    return False

def sortDateDESC(date1, date2):
    if date1 > date2:
        return True
    return False


# Fonction qui renvoie les données collectées entre deux dates
def getBetweenDate(array, date1, date2):
    i = 0
    tab = []
    while i < len(array):
        if sortDate(date1, array[i][0]) and sortDateDESC(array[i][0], date2):
            tab.append(array[i])
        i = i + 1
    return tab

# Fonction qui renvoie la valeur minimale d'un type de donnée
def getMin(array, type):
    tmparray = []
    i = 0
    while i < len(array):
        if array[i][4] == type:
            tmparray.append(array[i][3])
        i = i + 1
    return min([tmparray])

# Fonction qui renvoie la valeur maximale d'un type de donnée
def getMax(array, type):
    tmparray = []
    i = 0
    while i < len(array):
        if array[i][4] == type:
            tmparray.append(array[i])
        i = i + 1
    return max([tmparray])

# Fonction qui renvoie la valeur maximale d'un type de donnée
def getMoy(array, type):
    tmparray = []
    moy = 0
    i = 0
    while i < len(array):
        if array[i][4] == type:
            tmparray.append(array[i])
            moy = moy + array[i][3]
        i = i + 1
        moy = moy/len(tmparray)
    return moy

# fonction qui trie le tableau par date
def sortByDate(array):
    i = 0
    while i < len(array):
        j = 0
        while j < len(array):
            if sortDateDESC(array[i][0], array[j][0]):
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
            j = j+1
        i=i+1
    return array









add(array, (2020, 10, 5), (11, 27, 40), 5, 22.1, 'TEMP')
add(array, (2019, 3, 9), (11, 27, 40), 5, 22.1, 'TEMP')
add(array, (2021, 1, 10), (11, 27, 40), 5, 22.1, 'TEMP')
add(array, (2028, 10, 3), (11, 27, 40), 5, 22.1, 'TEMP')



# main #

while True:
    print("Bonjour, Quel action souhaitez vous faire ?\n1) Ajouter de nouvelles valeurs dans le tableau\n2) Trier les valeurs du tableau par la date la plus récente\n3) Afficher le tabelau\n4) Afficher la valeur max\n5) Afficher la valeur min\n6) Afficher la valeur moyenne\n0) Quitter\n >> ")
    value = int(input())
    if value == 1:
        test = 0
        while test == 0:
            date = (int(input("Merci d'indiquer les valeurs suivantes :\nAnnée : ")), int(input("Mois : ")), int(input('Jour : ')))
            date = checkDate(date)
            if date != -1:
                test = 1
        test = 0
        while test == 0:
            heure = (int(input("Heure : ")), int(input("Minute : ")), int(input('Seconde : ')))
            heure = checkHeure(heure)
            if date != -1:
                test = 1

        capteur = int(input("Id du capteur : "))
        type = str(input("Type de donnée :"))
        data = float(input("Valeur :"))

        add(array, date, heure, capteur, data, type)
    elif value == 2:
        viewTab(sortByDate(array))
    elif value == 3:
        viewTab(array)
    elif value == 4:
        viewTab(getMax(array, input("Type de donnée : ")))
    elif value == 5:
        viewTab(getMin(array, input("Type de donnée : ")))
    elif value == 6:
        print(f"Valeur moyenne :  {getMoy(array, input('Type de donnée : '))} ")


    elif value == 0:
        break


