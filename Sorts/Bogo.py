from Estructuras import Lista as lis
import random

def bogosort(lst,size, tipo):
    
    for pos in range(1,size):
        random_pos = random.randint(1,size)
        lis.exchange(lst,pos,random_pos,tipo)
        
    return lst

def is_sorted(lst,sort_crit,size, tipo):
    
    for pos in range(1,size):
        if sort_crit(lis.getElement(lst,pos,tipo),lis.getElement(lst,pos+1, tipo)) != True:
            return False
        
    return True

def sort(lst,sort_crit, tipo):

    size = lis.size(lst)
    while is_sorted(lst,sort_crit,size, tipo) != True:
        lst = bogosort(lst,size, tipo)
    return lst