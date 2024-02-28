from Estructuras import Lista as lis

def sort(lista, sort_crit, tipo):
    size = lista["size"]
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lis.sub_list(lista, 1, mid, tipo)
        rightlist = lis.sub_list(lista, mid+1, size - mid, tipo)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sort(leftlist, sort_crit, tipo)
        sort(rightlist, sort_crit, tipo)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = leftlist["size"]
        rightelements = rightlist["size"]

        while (i <= leftelements) and (j <= rightelements):
            elemi = lis.getElement(leftlist, i, tipo)
            elemj = lis.getElement(rightlist, j, tipo)
            """compara y ordena los elementos"""
            if sort_crit(elemj, elemi):   # caso estricto elemj < elemi
                lis.changeInfo(lista, k, elemj, tipo)
                j += 1
            else:                            # caso elemi <= elemj
                lis.changeInfo(lista, k, elemi, tipo)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lis.changeInfo(lista, k, lis.getElement(leftlist, i, tipo),tipo)
            i += 1
            k += 1

        while j <= rightelements:
            lis.changeInfo(lista, k, lis.getElement(rightlist, j,tipo), tipo)
            j += 1
            k += 1
    return lista
