from Estructuras import Lista as lis
import sys
sys.setrecursionlimit(1000000)


   
def greater(heap, element1, element2):
    """
    Indica si el elemento 1 es mayor que el elemento 2
    """
    cmp = heap['cmpfunction'](element1, element2)
    if cmp > 0:
            return True
    return False


def exchange(heap, posa, posb):
    """
    Intercambia los elementos en las posiciones posa y posb del heap
    """
  
    lis.exchange(heap['elements'], posa, posb)
    
def size(heap):
    """
    Retorna el número de elementos en el heap

    Args:
        heap: El arreglo con la informacion
    Returns:
       El tamaño del heap
    Raises:
        Exception
    """

    return (heap['size'])



def upHeap(heap, pos, end):
    """Mete el elemento en la posición correcta, compara los hijos y si hay uno mayor que el padre
    los intercambia

    Args:
        heap (ADT.HeapTree): Arbol en array
        pos (Int): Posición del padre
        end (Int): Hasta donde se evalúa del arbol
    Raises:
        Exception
    """
 
    while ((2*pos <= end)):
            j = 2*pos
            if (j < end):
                if not greater(heap, lis.getElement(heap['elements'], j),
                           lis.getElement(heap['elements'], (j+1))):
                    j += 1
            if (greater(heap, lis.getElement(heap['elements'], pos),
                            lis.getElement(heap['elements'], j))):
                break
            exchange(heap, pos, j)
            pos = j
   


def maxPQ(heap, n):
    """Se asegura de que la raíz es el elemento más grande en el Heap

    Args:
        heap (ADT.HeapTree):  Arbol en array
        n (Int): Elemento a colocar en la posición correcta
    Raises:
        Exception
    """
 
    if n>0:
        upHeap(heap, n, size(heap))
        maxPQ(heap, n-1)          
 


def minPQ(heap, n):
    """Intercambiamos la raíz con la última posición del árbol y colocamos la nueva raíz en la posición correcta

    Args:
        heap (ADT.HeapTree):  Arbol en array
        n (Int): Elemento a colocar en la posición correcta
    Raises:
        Exception
    """
 
    if n>0:
        exchange(heap, 1 , n)
        upHeap(heap, 1, n-1)
        minPQ(heap, n-1)          
    
def sort(heap,sort_crit)->None:
    """Algoritmo de ordenamiento de Heapsort

    Args:
        heap (ADT.HeapTree): Arbol(ARRAY) a ordenar
    """
    
    middle=size(heap)//2
    maxPQ(heap, middle)
    minPQ(heap, size(heap))
        

