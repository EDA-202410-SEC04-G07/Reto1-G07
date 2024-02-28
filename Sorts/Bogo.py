from Estructuras import Lista as lis
import random

def bogosort(lst,size):
    
    for pos in range(1,size):
        random_pos = random.randint(1,size)
        lis.exchange(lst,pos,random_pos)
        
    return lst

def is_sorted(lst,sort_crit,size):
    
    for pos in range(1,size):
        if sort_crit(lis.getElement(lst,pos),lis.getElement(lst,pos+1)) != True:
            return False
        
    return True

def sort(lst,sort_crit):

    size = lis.size(lst)
    while is_sorted(lst,sort_crit,size) != True:
        lst = bogosort(lst,size)
    return lst