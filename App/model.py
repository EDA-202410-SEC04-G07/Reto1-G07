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
   

def req_6(data_structs, start_date, end_date, country=None, experience=None):
 
    filtered_jobs = [job for job in data_structs["jobs"] if start_date <= datetime.strptime(job["published_at"], "%Y-%m-%d") <= end_date]
    if country:
        filtered_jobs = [job for job in filtered_jobs if job["country_code"] == country]
    if experience:
        filtered_jobs = [job for job in filtered_jobs if job["expertise_level"] == experience]
    return filtered_jobs

def count_jobs_by_city(jobs):
    city_counts = {}
    for job in jobs:
        city_name = job["city"]
        if city_name not in city_counts:
            city_counts[city_name] = {"count": 0, "salary_sum": 0, "companies": {}, "best_offer": None, "worst_offer": None}
        city_counts[city_name]["count"] += 1
        city_counts[city_name]["salary_sum"] += job["salary"] if "salary" in job else 0
        if job["company_name"] not in city_counts[city_name]["companies"]:
            city_counts[city_name]["companies"][job["company_name"]] = 0
        city_counts[city_name]["companies"][job["company_name"]] += 1
        if not city_counts[city_name]["best_offer"] or city_counts[city_name]["best_offer"]["salary"] <  job["salary"]:
            city_counts[city_name]["best_offer"] = job
        if not city_counts[city_name]["worst_offer"] or city_counts[city_name]["worst_offer"]["salary"] > job["salary"]:
            city_counts[city_name]["worst_offer"] = job
    return city_counts

def promedio_salario_por_ciudad(city_counts):

    for city, data in city_counts.items():
        city_counts[city]["avg_salary"] = data["salary_sum"] / data["count"] if data["count"] > 0 else 0
    return city_counts

def mejor_peor_oferta_por_ciudad(city_counts):

    for city, data in city_counts.items():
        if not data["best_offer"]["salary"]:
            del data["best_offer"]
        if not data["worst_offer"]["salary"]:
            del data["worst_offer"]
    return city_counts

def ordenar_ciudades_count(city_counts):
    def get_count(city_count):
        return city_count[1]["count"]

    def get_name(city_count):
        return city_count[0]

    def compare_city_counts(x, y):
        count_diff = get_count(x) - get_count(y)
        if count_diff != 0:
            return count_diff
        else:
            return (get_name(x) > get_name(y)) - (get_name(x) < get_name(y))

    sorted_city_counts = sorted(city_counts.items(), key=cmp_to_key(compare_city_counts))

    return sorted_city_counts


def req_7(data_structs, num_paises, fecha_inicial, fecha_final, tipo):
    """
    Función que soluciona el requerimiento 7
    """
    skills = data_structs["skills"]
    data_structs = sort_jobs_fecha(data_structs, tipo)
    lista = lis.new_list(tipo)
    paises = lis.new_list(tipo)
    contador = 0 
    for i in range(lis.size(data_structs)):
      if (fecha_inicial<=data_structs["elements"][i]["published_at"] <= fecha_final):
        if data_structs["elements"][i]["country_code"] not in paises["elements"]: 
             lis.add_last(paises, data_structs["elements"][i]["country_code"],tipo)
             contador += 1
        if (contador <= num_paises):
                 lis.add_last(lista, data_structs["elements"][i],tipo)
        
                 
    total_ofertas = lis.size(lista)
    ciudades = lis.new_list(tipo)
    for y in range(lis.size(lista)):
          if data_structs["elements"][y]["city"] not in ciudades["elements"]: 
             lis.add_last(ciudades, data_structs["elements"][y]["city"],tipo)
             
    total_ciudades = lis.size(ciudades)

    frecuencia = {} 
    frecuencia2 = {}
    mayor = lis.new_list(tipo)
    mayor_city = lis.new_list(tipo)
    for l in range(lis.size(lista)):
          if lista["elements"][l]["country_code"] in mayor["elements"]:
              frecuencia[lista["elements"][l]["country_code"]] += 1
          else: 
              frecuencia[lista["elements"][l]["country_code"]] = 1
              lis.add_last(mayor, lista["elements"][l]["country_code"] ,tipo)

          if lista["elements"][l]["city"] in mayor_city["elements"]:
              frecuencia2[lista["elements"][l]["city"]] += 1
          else: 
              frecuencia2[lista["elements"][l]["city"]] = 1
              lis.add_last(mayor_city, lista["elements"][l]["city"] ,tipo) 
    
    max_pais = None
    cont_pais = 0
    max_ciudad = None
    cont_ciudad= 0

    for l, frecuencia in frecuencia.items():
      if frecuencia > cont_pais:
        cont_pais = frecuencia
        max_pais = l 
    
    for l, frecuencia2 in frecuencia2.items():
      if frecuencia2 > cont_ciudad:
        cont_ciudad = frecuencia2
        max_ciudad = l

    
      
     #Habilidades diferentes
    
    habilidades = {"junior": 0 , "mid": 0, "senior": 0}
    junior = lis.new_list(tipo)
    mid = lis.new_list(tipo)
    senior = lis.new_list(tipo)

    for x in range(lis.size(lista)):
        if lista["elements"][x]["experience_level"] == "junior": 
             lis.add_last(junior, lista["elements"][x]["id"] ,tipo)
        if lista["elements"][x]["experience_level"] == "mid": 
             lis.add_last(mid, lista["elements"][x]["id"] ,tipo)
        if lista["elements"][x]["experience_level"] == "senior": 
             lis.add_last(senior, lista["elements"][x]["id"],tipo)
    
    diferente = lis.new_list(tipo)
    datos = lis.new_list(tipo)
    for k in range(lis.size(junior)):
         for g in range(lis.size(skills)):
             if skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == junior["elements"][k]:
                 lis.add_last(datos, skills["elements"][g]["PROOF POINT"],tipo)
             if (skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == junior["elements"][k]) and (skills["elements"][g]["PROOF POINT"] not in diferente["elements"]):
                 habilidades["junior"] += 1
                 lis.add_last(diferente, skills["elements"][g]["PROOF POINT"],tipo)

    diferente2 = lis.new_list(tipo)
    datos2 = lis.new_list(tipo)
    for k in range(lis.size(mid)):
         for g in range(lis.size(skills)):
             if skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == mid["elements"][k]:
                 lis.add_last(datos2, skills["elements"][g]["PROOF POINT"],tipo)
             if (skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == mid["elements"][k]) and (skills["elements"][g]["PROOF POINT"] not in diferente2["elements"]):
                 habilidades["mid"] += 1
                 lis.add_last(diferente2, skills["elements"][g]["PROOF POINT"],tipo)   

    diferente3 = lis.new_list(tipo)
    datos3 = lis.new_list(tipo)
    for k in range(lis.size(senior)):
         for g in range(lis.size(skills)):
             if skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == senior["elements"][k]:
                 lis.add_last(datos3, skills["elements"][g]["PROOF POINT"],tipo)
             if (skills["elements"][g]["intelligints-senior-cybersecurity-engineer"] == senior["elements"][k]) and (skills["elements"][g]["PROOF POINT"] not in diferente3["elements"]):
                 habilidades["senior"] += 1
                 lis.add_last(diferente3, skills["elements"][g]["PROOF POINT"],tipo)
    
    
    frec = {} 
    may = lis.new_list(tipo)
    for l in datos["elements"]:
        if l in may["elements"]:
            frec[l] += 1
        else: 
            frec[l] = 1
            lis.add_last(mayor, l ,tipo)
    
    max_junior = None
    cont_junior_max = 0
    min_junior = None 
    conteo_junior_min= 10000000000000000

    for l, frec in frec.items():
      if frec > cont_junior_max:
        cont_junior_max = frec
        max_junior = l 
      if frec < conteo_junior_min:
           conteo_junior_min = frecuencia 
           min_junior = l

    
    
    max_habilidad = {"junior": max_junior , "mid": None, "senior": None}
    max_conteo = {"junior": cont_junior_max, "mid": 0, "senior": 0}
    min_habilidad = {"junior": min_junior , "mid": None, "senior": None}
    min_conteo = {"junior": conteo_junior_min, "mid": 0, "senior": 0}

    # TODO: Realizar el requerimiento 7
    return total_ofertas, total_ciudades, max_pais, cont_pais, max_ciudad, cont_ciudad, habilidades, max_habilidad, max_conteo, min_habilidad, min_conteo


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



    





