from Estructuras import Lista as lis

def sort(lst, sort_crit):
    size = lis.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (sort_crit(
               lis.getElement(lst, pos2), lis.getElement(lst, pos2-1))):
            lis.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst
