"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from Estructuras import Lista as lis

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"jobs": None,
                    "skills": None,
                    "multilocations": None,
                    "employments": None
               }
    
    data_structs["jobs"] = lis.new_list()
    data_structs["skills"] = lis.new_list()    
    data_structs["multilocations"] = lis.new_list()
    data_structs["employments"] = lis.new_list()                        
    return data_structs



# Funciones para agregar informacion al modelo

def add_job(data_structs, job):
    lis.add_last(data_structs["jobs"], job)

def jobs_size(data_structs):
    return lis.size(data_structs["jobs"])

def add_skills(data_structs, skills):
    lis.add_last(data_structs["skills"], skills)

def skills_size(data_structs):
    return lis.size(data_structs["skills"])

def add_multilocations(data_structs, multilocations):
    lis.add_last(data_structs["multilocations"], multilocations)

def multilocations_size(data_structs):
    return lis.size(data_structs["multilocations"])

def add_employments(data_structs, employments):
    lis.add_last(data_structs["employments"], employments)

def employments_size(data_structs):
    return lis.size(data_structs["employments"])
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


def setJobsSublist(data_structs, size):
    """
    Crea una sublista de libros de tamaño size
    """
    # TODO nuevo del lab 5
    jobs = data_structs["jobs"]
    data_structs["jobssublist"] = lis.sub_list(jobs, 1, size)
    return data_structs

# Funciones utilizadas para comparar elementos dentro de una lista
def tipo_de_lista(type):
    if type == 0:
        return new_data_structs()
        
    else: 
        return new_data_structs_linked()


def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def cmp_ofertas_by_empresa_y_fecha(oferta1,oferta2):
    
    if str(oferta1["company_name"]) < str(oferta2["company_name"]):
          booleano = True
    elif str(oferta1["company_name"]) == str(oferta2["company_name"]):
        if float(oferta1["published_at"]) < float(oferta2["published_at"]):
            booleano = True
        else: 
            booleano = False

    else: 
        booleano = False 
    return booleano 

def sortOfertas(data_structs):
    sorted_ofertas = data_structs["jobs"]
    sorted_ofertas = sort(sorted_ofertas, cmp_ofertas_by_empresa_y_fecha)
    return sorted_ofertas


def sort(lista, sort_crit):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    size = lista["size"]
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lis.sub_list(lista, 1, mid)
        rightlist = lis.sub_list(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sort(leftlist, sort_crit)
        sort(rightlist, sort_crit)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = leftlist["size"]
        rightelements = rightlist["size"]

        while (i <= leftelements) and (j <= rightelements):
            elemi = lis.getElement(leftlist, i)
            elemj = lis.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if sort_crit(elemj, elemi):   # caso estricto elemj < elemi
                lis.changeInfo(lista, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lis.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lis.changeInfo(lista, k, lis.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lis.changeInfo(lista, k, lis.getElement(rightlist, j))
            j += 1
            k += 1
    return lista





##### LABORATORIO 5 #####





def comparar_ofertas(job1, job2):
  if job1['company_name'] < job2['company_name']:
    return True
  elif job1['company_name'] == job2['company_name']:
    if job1['published_at'] < job2['published_at']:
      return True
  else:
    return False
  

def crear_lista_array():
  catalogo = {
    'jobs': lis.newList('ARRAY_LIST', cmpfunction=comparar_ofertas)
  }

def crear_lista_linked():
  catalogo = {
    'jobs': lis.newList('SINGLE_LINKED', cmpfunction=comparar_ofertas)
  }


def estructura_datos(tipo):
  if tipo == "array":
    return crear_lista_array()
  else:
    return crear_lista_linked()
