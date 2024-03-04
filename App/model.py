﻿"""
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
from datetime import datetime
from Estructuras import Lista as lis
from Sorts import Shell as shs
from Sorts import Heap as hes
from Sorts import Tim as cus
from Sorts import Merge as mes
from Sorts import Bogo as bos
from Sorts import Selection as ses
from Sorts import Quick as qus
from Sorts import Insertion as ins

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

sort_algorithm = None

def new_data_structs(tipo):
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
    
    data_structs["jobs"] = lis.new_list(tipo)
    data_structs["skills"] = lis.new_list(tipo)    
    data_structs["multilocations"] = lis.new_list(tipo)
    data_structs["employments"] = lis.new_list(tipo)                        
    return data_structs



# Funciones para agregar informacion al modelo

def add_job(data_structs, job, tipo):
    lis.add_last(data_structs["jobs"], job, tipo)

def jobs_size(data_structs):
    return lis.size(data_structs["jobs"])

def add_skills(data_structs, skills,tipo):
    lis.add_last(data_structs["skills"], skills,tipo)

def skills_size(data_structs):
    return lis.size(data_structs["skills"])

def add_multilocations(data_structs, multilocations,tipo):
    lis.add_last(data_structs["multilocations"], multilocations,tipo)

def multilocations_size(data_structs):
    return lis.size(data_structs["multilocations"])

def add_employments(data_structs, employments,tipo):
    lis.add_last(data_structs["employments"], employments,tipo)

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

##### REQUERIMIENTO 1 #####

def req_1(data_structs, num_ofertas, cod_pais, niv_experticia, tipo):
    """
    Función que soluciona el requerimiento 1
    """
    data_structs = sort_jobs_fecha(data_structs, tipo)
    lista = lis.new_list(tipo)

    for i in range(lis.size(data_structs)):
        if (data_structs["elements"][i]["experience_level"] == niv_experticia) and (data_structs["elements"][i]["country_code"] == cod_pais):
                 lis.add_last(lista, data_structs["elements"][i],tipo)

    tamaño = lis.size(lista)
    respuesta = lista["elements"][:num_ofertas]
    return respuesta, tamaño

def cmp_ofertas_by_fecha(oferta1, oferta2):
    if str(oferta1["published_at"]) < str(oferta2["published_at"]):
            booleano = True
    elif str(oferta1["published_at"]) == str(oferta2["published_at"]):
         if str(oferta1["company_name"]) < str(oferta2["company_name"]):
              booleano = True
         else:
              booleano = False     
    else: 
            booleano = False
    return booleano

def sort_jobs_fecha(data_structs, tipo):
    sorted_ofertas = data_structs["jobssublist"]
    sorted_ofertas = sort_algorithm.sort(sorted_ofertas, cmp_ofertas_by_fecha, tipo)
    return sorted_ofertas



def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


##### REQUERIMIENTO 3 #####

def jobs_compania_fecha(data_structs, company_name, start_date, end_date):
    
    jobs_req3 = [job for job in data_structs["jobs"] if job["company_name"] == company_name and
                     start_date <= datetime.strptime(job["published_at"], "%Y-%m-%d") <= end_date]
    return jobs_req3

def contar_jobs_experiencia(jobs):
    
    junior = sum(1 for job in jobs if job["expertise_level"] == "junior")
    mid = sum(1 for job in jobs if job["expertise_level"] == "mid")
    senior = sum(1 for job in jobs if job["expertise_level"] == "senior")

    return junior, mid, senior


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs, city, fecha_inicial, fecha_final, tipo):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    data_structs = sort_jobs_fecha(data_structs, tipo)
    lista = lis.new_list(tipo)

    for i in range(lis.size(data_structs)):
        if (data_structs["elements"][i]["city"] == city) and (fecha_inicial<=data_structs["elements"][i]["published_at"] <= fecha_final):
                 lis.add_last(lista, data_structs["elements"][i],tipo)

    lista_ordenada = lista 
    total_ofertas = lis.size(lista)
    
    empresas = lis.new_list(tipo)
    total_empresas = lis.new_list(tipo)
    for m in range(lis.size(lista)):
        if lista["elements"][m]["company_name"] not in empresas["elements"]:
                 lis.add_last(empresas, lista["elements"][m]["company_name"],tipo)
        lis.add_last(total_empresas, lista["elements"][m]["company_name"],tipo)
    dato_empresas = lis.size(empresas)
    
    frecuencia = {} 
    mayor = lis.new_list(tipo)
    for l in total_empresas["elements"]:
        if l in mayor["elements"]:
            frecuencia[l] += 1
        else: 
            frecuencia[l] = 1
            lis.add_last(mayor, l ,tipo)
    
    max_empresa = None
    conteo_empresa = 0
    min_empresa = None 
    conteo_min = 10000000000000000
    for l, frecuencia in frecuencia.items():
      if frecuencia > conteo_empresa:
        conteo_empresa = frecuencia
        max_empresa = l 
      if frecuencia < conteo_min:
           conteo_min = frecuencia 
           min_empresa = l
    
    return total_ofertas, dato_empresas, conteo_empresa, max_empresa, conteo_min, min_empresa, lista_ordenada



#def total_empresas(data_structs, city, fecha_inicial, fecha_final, tipo):
   

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

def selectSortAlgorithm(algo_opt):
    """selectSortAlgorithm permite seleccionar el algoritmo de ordenamiento
    para la lista de pokemon.

    Args:
        algo_opt (int): opcion de algoritmo de ordenamiento, las opciones son:
            1: Selection Sort
            2: Insertion Sort
            3: Shell Sort
            4: Merge Sort
            5: Quick Sort
            6: Heap Sort
            7: Bogo Sort
            8: Custom Sort (timsort o bucketsort)

    Returns:
        list: sort_algorithm (sort) la instancia del ordenamiento y
        algo_msg (str) el texto que describe la configuracion del ordenamiento
    """
    # TODO completar el ordenamiento personalizado para el lab 5
    # TODO nuevo del lab 5
    # respuestas por defecto
    sort_algorithm = None
    algo_msg = None

    # selecciona el algoritmo de ordenamiento
    # opcion 1: Selection Sort
    if algo_opt == 1:
        sort_algorithm = ses
        algo_msg = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    elif algo_opt == 2:
        sort_algorithm = ins
        algo_msg = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    elif algo_opt == 3:
        sort_algorithm = shs
        algo_msg = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    elif algo_opt == 4:
        sort_algorithm = mes
        algo_msg = "Seleccionó la configuración - Merge Sort"

    # opcion 5: Quick Sort
    elif algo_opt == 5:
        sort_algorithm = qus
        algo_msg = "Seleccionó la configuración - Quick Sort"

    # opcion 6: Heap Sort
    elif algo_opt == 6:
        sort_algorithm = hes
        algo_msg = "Seleccionó la configuración - Heap Sort"

    # opcion 7: Bogo Sort
    elif algo_opt == 7:
        sort_algorithm = bos
        algo_msg = "Seleccionó la configuración - Bogo Sort"

    # opcion 6: Custom Sort: timsort o bucketsort
    # TODO completar el ordenamiento personalizado para el lab 5
    elif algo_opt == 8:
        sort_algorithm = cus
        algo_msg = "Seleccionó la configuración - Custom Sort (Tim, Patience)"
    # respuesta final: algoritmo de ordenamiento y texto de configuracion
    return sort_algorithm, algo_msg

def setJobsSublist(data_structs, size, tipo):
    """
    Crea una sublista de libros de tamaño size
    """
    # TODO nuevo del lab 5
    jobs = data_structs["jobs"]
    data_structs["jobssublist"] = lis.sub_list(jobs, 1, size, tipo)
    return data_structs

# Funciones utilizadas para comparar elementos dentro de una lista


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
        if str(oferta1["published_at"]) < str(oferta2["published_at"]):
            booleano = True
        else: 
            booleano = False

    else: 
        booleano = False 
    return booleano 

def sortOfertas(data_structs, tipo):
    sorted_ofertas = data_structs["jobssublist"]
    sorted_ofertas = sort_algorithm.sort(sorted_ofertas, cmp_ofertas_by_empresa_y_fecha, tipo )
    return sorted_ofertas




##### LABORATORIO 5 #####



    





