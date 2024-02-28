from Estructuras import Lista as lis


def partition(lst, lo, hi, sort_crit, tipo):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           lis.getElement(lst, leader, tipo), lis.getElement(lst, hi, tipo)):
            lis.exchange(lst, follower, leader, tipo)
            follower += 1
        leader += 1
    lis.exchange(lst, follower, hi, tipo)
    return follower


def quicksort(lst, lo, hi, sort_crit, tipo):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, sort_crit, tipo)
    quicksort(lst, lo, pivot-1, sort_crit, tipo)
    quicksort(lst, pivot+1, hi, sort_crit, tipo)


def sort(lst, sort_crit, tipo):
    quicksort(lst, 1, lis.size(lst), sort_crit, tipo)
    return lst
