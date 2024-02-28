from Estructuras import Lista as lis

def sort(lst,sort_crit):
 
    n = lis.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(
                                lis.getElement(lst, j+1),
                                lis.getElement(lst, j-h+1)):
                lis.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst