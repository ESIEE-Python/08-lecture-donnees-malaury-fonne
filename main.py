"""Lecture de données"""
#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,mode="r",encoding="utf-8") as file:
        reader=csv.reader(file, delimiter=";")
        return [list(map(int,ligne)) for ligne in reader ]

def get_list_k(data, k):
    """

    Args:
        data,k: liste de liste retourné par read_data() et un indice k
    
    Returns:
        list: retourne la k ème liste
    """
    if 0<=k<=len(data):
        return data[k]
    return None

def get_first(l):
    """
    retourne le 1er elt de l
    """
    return l[0] if l else None
def get_last(l):

    """Retourne le dernier element de la liste
    Args:liste
    Returns:dernier élément de l
    """
    if l:
        return l[-1]
    return None

def get_max(l):
    """
    retourne le plus grand elt de l
    """
    if l:
        return max(l)
    return None

def get_min(l):
    """
    retourne le plus petit element de l
    """
    if l:
        return min(l)
    return None

def get_sum(l):
    """retourne la somme des elements de l
    """
    if l:
        return sum(l)
    return None


#### Fonction principale


def main():
    """
    Execute les fonctions
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
