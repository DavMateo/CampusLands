def findElementListPos(lst, elem):
    # Función que busca un elemento en la lista.
    # Si lo encuentra, devuelve la posición
    # Sino lo encuentra devuelve -1
    for p in range(len(lst)):
        if elem == lst[p]:
            return p
    return -1

def existElementList(lst, elem):
    # Función que busca un elemento en la lista
    # Si lo encuentra devuelve True
    # Sino lo encuentra devuelve False
    
    for e in lst:
        if e == elem:
            return True
    return False