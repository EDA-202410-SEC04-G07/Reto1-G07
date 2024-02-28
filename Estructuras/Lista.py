def new_list(tipo):
    if tipo == 0:
       lista = {
        "elements": [],#{value:None, next:None}
        "size": 0,
        'type': 'ARRAY_LIST',
         }
    else:
         lista = {
        "first": None,
        "last" : None,
        "size": 0,
        'type': 'SINGLE_LINKED',
         }
       
    return lista

def newSingleNode(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    node = {'info': element, 'next': None}
    return(node)


def add_last(lista, elem,tipo):
 if tipo==0:
    lista["elements"].append(elem)
    lista["size"]+= 1
 else: 
    new_node = newSingleNode(elem)

    if lista['size'] == 0:
        lista['first'] = new_node
    else:
        lista['last']['next'] = new_node
    lista['last'] = new_node
    lista['size'] += 1
    return lista


def compareElements(lst, element, info):
    if(lst['key'] is not None):
            return lst['cmpfunction'](element[lst['key']], info[lst['key']])
    else:
            return lst['cmpfunction'](element, info)
    

def isPresent(lista, elem,tipo):
  if tipo == 0:
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
  else: 
      size = size(lista)
      if size > 0:
            node = lista['size']
            keyexist = False
            for keypos in range(1, size+1):
                if (node is not None):
                    if (compareElements(lista, elem, node['info']) == 0):
                        keyexist = True
                        break
                    node = node['next']
            if keyexist:
                return keypos
      return 0



def sub_list(lista, pos, numelem, tipo):
  if tipo == 0:
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
  else: 
      sublst = {'first': None,
                  'last': None,
                  'size': 0,
                  'type': 'SINGLE_LINKED',
                  }
      cont = 1
      loc = pos
      while cont <= numelem:
            elem = getElement(lista, loc, tipo)
            add_last(sublst, elem,tipo)
            loc += 1
            cont += 1
      return sublst

def getElement(lista,pos,tipo):
  if tipo ==0: 
    return lista['elements'][pos-1]
  else: 
    searchpos = 1
    node = lista['first']
    while searchpos < pos:
            searchpos += 1
            node = node['next']
    return node['info']

def changeInfo(lista, pos, newinfo, tipo):
  if tipo == 0:
     lista['elements'][pos-1] = newinfo
  else:
        current = lista['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lista

def size(lista):
    return lista['size']

def isEmpty(lista):
    return lista['size'] == 0

def exchange(lista, pos1, pos2, tipo):
     elem1= getElement(lista,pos1,tipo)
     elem2= getElement(lista,pos2,tipo)
     changeInfo(lista, pos1,elem2,tipo)
     changeInfo(lista, pos2,elem1,tipo)
     return lista
