from Estructuras import Lista as lis

def sort(lst, sort_crit,tipo):
    size = lis.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (sort_crit(
               lis.getElement(lst, pos2, tipo), lis.getElement(lst, pos2-1, tipo))):
            lis.exchange(lst, pos2, pos2-1, tipo)
            pos2 -= 1
        pos1 += 1
    return lst
