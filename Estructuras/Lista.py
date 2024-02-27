def new_list():
    lista = {
        "elements": [],#{value:None, next:None}
        "size": 0,
    }
    
    return lista

def newList_linked():
    lista = {'first': None,
               'last': None,
               'size': 0,
               'type': 'SINGLE_LINKED',
               }
    return lista
     
def add_last(lista, elem):
    lista["elements"].append(elem)
    lista["size"]+= 1
    return lista
     
def isPresent(lista, elem):
    size = lista['size']
    respuesta = False
    if size > 0:
            
            for keypos in range(1, size+1):
                info = lista['elements'][keypos-1]
                if info == elem:
                    respuesta = True
                    info_respuesta = keypos-1
                    break
            if respuesta == True:
                return info_respuesta
    return 0



def sub_list(lista, pos, numelem):
    sublista = {
        "elements": [],
        "size": 0,
    }
    elem = pos-1
    cont = 1
    while cont <= numelem:
            sublista['elements'].append(lista['elements'][elem])
            sublista['size'] += 1
            elem += 1
            cont += 1
    return sublista 

def getElement(lista,pos):
    return lista['elements'][pos-1]

def changeInfo(lista, pos, newinfo):
     lista['elements'][pos-1] = newinfo

def size(lista):
    return lista['size']

def isEmpty(lista):
    return lista['size'] == 0

def exchange(lista, pos1, pos2):
     elem1= getElement(lista,pos1)
     elem2= getElement(lista,pos2)
     changeInfo(lista, pos1,elem2)
     changeInfo(lista, pos2,elem1)
     
