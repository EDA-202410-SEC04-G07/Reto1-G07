from Estructuras import Lista as lis


def partition(lst, lo, hi, sort_crit):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           lis.getElement(lst, leader), lis.getElement(lst, hi)):
            lis.exchange(lst, follower, leader)
            follower += 1
        leader += 1
    lis.exchange(lst, follower, hi)
    return follower


def quicksort(lst, lo, hi, sort_crit):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, sort_crit)
    quicksort(lst, lo, pivot-1, sort_crit)
    quicksort(lst, pivot+1, hi, sort_crit)


def sort(lst, sort_crit):
    quicksort(lst, 1, lis.size(lst), sort_crit)
    return lst
