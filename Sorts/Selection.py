from Estructuras import Lista as lis

def sort(lst, sort_crit):
    size = lis.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (sort_crit(lis.getElement(lst, pos2),
               (lis.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lis.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst