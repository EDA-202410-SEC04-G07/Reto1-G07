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
 """

from Estructuras import Lista as lis
import config as cf
import model
import time
import csv
import os
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tipo):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(tipo)
    return control



# Funciones para la carga de datos

def load_data(control,tamaño,tipo):
    jobs = load_jobs(control,tamaño,tipo)
    skills = load_skills(control,tamaño,tipo)
    multilocations= load_multilocations(control,tamaño,tipo)
    employments = load_employments(control,tamaño,tipo)
    return jobs, skills, multilocations, employments

def load_jobs(control,tamaño,tipo):

    data_structs = control["model"]
    if tamaño == 1:
       file = os.path.join(cf.data_dir, "10-por-jobs.csv")
    elif tamaño == 2:
       file = os.path.join(cf.data_dir, "20-por-jobs.csv")
    elif tamaño == 3:
       file = os.path.join(cf.data_dir, "30-por-jobs.csv")
    elif tamaño == 4:
       file = os.path.join(cf.data_dir, "40-por-jobs.csv")
    elif tamaño == 5:
       file = os.path.join(cf.data_dir, "50-por-jobs.csv")
    elif tamaño == 6:
       file = os.path.join(cf.data_dir, "60-por-jobs.csv")
    elif tamaño == 7:
       file = os.path.join(cf.data_dir, "70-por-jobs.csv")
    elif tamaño == 8:
       file = os.path.join(cf.data_dir, "80-por-jobs.csv")
    elif tamaño == 9:
       file = os.path.join(cf.data_dir, "90-por-jobs.csv")
    elif tamaño == 10:
       file = os.path.join(cf.data_dir, "small-jobs.csv")
    elif tamaño == 11:
       file = os.path.join(cf.data_dir, "medium-jobs.csv")
    elif tamaño == 12:
       file = os.path.join(cf.data_dir, "large-jobs.csv")

    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for job in input_file:
        model.add_job(data_structs, job,tipo)
    return model.jobs_size(data_structs)

def load_skills(control, tamaño,tipo):

    data_structs = control["model"]

    if tamaño == 1:
       file = os.path.join(cf.data_dir, "10-por-skills.csv")
    elif tamaño == 2:
       file = os.path.join(cf.data_dir, "20-por-skills.csv")
    elif tamaño == 3:
       file = os.path.join(cf.data_dir, "30-por-skills.csv")
    elif tamaño == 4:
       file = os.path.join(cf.data_dir, "40-por-skills.csv")
    elif tamaño == 5:
       file = os.path.join(cf.data_dir, "50-por-skills.csv")
    elif tamaño == 6:
       file = os.path.join(cf.data_dir, "60-por-skills.csv")
    elif tamaño == 7:
       file = os.path.join(cf.data_dir, "70-por-skills.csv")
    elif tamaño == 8:
       file = os.path.join(cf.data_dir, "80-por-skills.csv")
    elif tamaño == 9:
       file = os.path.join(cf.data_dir, "90-por-skills.csv")
    elif tamaño == 10:
       file = os.path.join(cf.data_dir, "small-skills.csv")
    elif tamaño == 11:
       file = os.path.join(cf.data_dir, "medium-skills.csv")
    elif tamaño == 12:
       file = os.path.join(cf.data_dir, "large-skills.csv")

    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for skills in input_file:
        model.add_skills(data_structs, skills,tipo)
    return model.skills_size(data_structs)

def load_multilocations(control,tamaño,tipo):
    

    data_structs = control["model"]
    if tamaño == 1:
       file = os.path.join(cf.data_dir, "10-por-multilocations.csv")
    elif tamaño == 2:
       file = os.path.join(cf.data_dir, "20-por-multilocations.csv")
    elif tamaño == 3:
       file = os.path.join(cf.data_dir, "30-por-multilocations.csv")
    elif tamaño == 4:
       file = os.path.join(cf.data_dir, "40-por-multilocations.csv")
    elif tamaño == 5:
       file = os.path.join(cf.data_dir, "50-por-multilocations.csv")
    elif tamaño == 6:
       file = os.path.join(cf.data_dir, "60-por-multilocations.csv")
    elif tamaño == 7:
       file = os.path.join(cf.data_dir, "70-por-multilocations.csv")
    elif tamaño == 8:
       file = os.path.join(cf.data_dir, "80-por-multilocations.csv")
    elif tamaño == 9:
       file = os.path.join(cf.data_dir, "90-por-multilocations.csv")
    elif tamaño == 10:
       file = os.path.join(cf.data_dir, "small-multilocations.csv")
    elif tamaño == 11:
       file = os.path.join(cf.data_dir, "medium-multilocations.csv")
    elif tamaño == 12:
       file = os.path.join(cf.data_dir, "large-multilocations.csv")

    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for multilocations in input_file:
        model.add_multilocations(data_structs, multilocations,tipo)
    return model.multilocations_size(data_structs)


def load_employments(control,tamaño,tipo):
    
    data_structs = control["model"]
    if tamaño == 1:
       file = os.path.join(cf.data_dir, "10-poremployments_types.csv")
    elif tamaño == 2:
       file = os.path.join(cf.data_dir, "20-poremployments_types.csv")
    elif tamaño == 3:
       file = os.path.join(cf.data_dir, "30-poremployments_types.csv")
    elif tamaño == 4:
       file = os.path.join(cf.data_dir, "40-poremployments_types.csv")
    elif tamaño == 5:
       file = os.path.join(cf.data_dir, "50-poremployments_types.csv")
    elif tamaño == 6:
       file = os.path.join(cf.data_dir, "60-poremployments_types.csv")
    elif tamaño == 7:
       file = os.path.join(cf.data_dir, "70-poremployments_types.csv")
    elif tamaño == 8:
       file = os.path.join(cf.data_dir, "80-poremployments_types.csv")
    elif tamaño == 9:
       file = os.path.join(cf.data_dir, "90-poremployments_types.csv")
    elif tamaño == 10:
       file = os.path.join(cf.data_dir, "small-employments_types.csv")
    elif tamaño == 11:
       file = os.path.join(cf.data_dir, "medium-employments_types.csv")
    elif tamaño == 12:
       file = os.path.join(cf.data_dir, "large-employments_types.csv")

    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for employments in input_file:
        model.add_employments(data_structs,employments, tipo)
    return model.employments_size(data_structs)


def setSortAlgorithm(algo_opt):
    """
    Configura el algoritmo de ordenamiento que se va a utilizar en el
    modelo y retorna un mensaje que informa al usuario.
    """
    
    ans = model.selectSortAlgorithm(algo_opt)
    
    algorithm = ans[0]
    model.sort_algorithm = algorithm
    algoritm_msg = ans[1]
    return algoritm_msg


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def sortJobs(control, tipo):
    """
    Ordena los libros por average_rating y toma el los tiempos en los
    que se inició la ejecución del requerimiento y cuando finalizó
    con getTime(). Finalmente calcula el tiempo que demoró la ejecución
    de la función con deltaTime()
    """
    # TODO incluir resutlado en la toma de tiempos (Parte 1).
    start_time = getTime()
    sorted_jobs = model.sortOfertas(control["model"], tipo)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_jobs, delta_time


def setJobsSublist(control, size, tipo):
    """
    Retorna una sublista de libros
    """
    # TODO nuevo del lab 5 (Parte 2)
    data_structs = control["model"]
    control["model"] = model.setJobsSublist(data_structs, size,tipo)
    return control
# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

##### REQUERIMIENTO 1 #####

def controller_jobs_by_fecha(data_structs):
    
    sorted_jobs = model.sort_jobs_fecha(data_structs)
    if sorted_jobs:
        print_jobs(sorted_jobs)

def controller_jobs_pais_nivel_experiencia(data_structs, country_code, expertise_level):
    
    filtered_jobs = model.jobs_pais_nivel_experiencia(data_structs, country_code, expertise_level)
    print_jobs(filtered_jobs)

def req_1(control, num_ofertas, cod_pais, niv_experticia, tipo):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    sorted_jobs = model.req_1(control["model"],num_ofertas, cod_pais, niv_experticia, tipo)
    return sorted_jobs
   


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


##### REQUERIMIENTO 3 #####
def req_3(control):
   
    # TODO: Modificar el requerimiento 3
    ofertas_con_skill, empresas_con_skill, promedio_ofertas_empresa = model.req_3(control["model"])
    return ofertas_con_skill, empresas_con_skill, promedio_ofertas_empresa


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control,city, fecha_inicial, fecha_final, tipo):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = getTime()
    total_ofertas, dato_empresas, conteo_empresa, max_empresa,conteo_min, min_empresa, lista_ordenada = model.req_5(control["model"],city, fecha_inicial, fecha_final, tipo)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    
    return total_ofertas, dato_empresas, conteo_empresa, max_empresa, conteo_min, min_empresa, lista_ordenada, delta_time
    

def req_6(control, ciudad, fecha_inicial, fecha_final, skill):

    # TODO: Modificar el requerimiento 6
    ofertas_con_skill, empresas_con_skill, promedio_ofertas_empresa = model.req_6(control["model"], ciudad, fecha_inicial, fecha_final, skill)
    return ofertas_con_skill, empresas_con_skill, promedio_ofertas_empresa
    


def req_7(control, num_paises, fecha_inicial, fecha_final, tipo):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    total_ofertas, total_ciudades, max_pais, cont_pais,max_ciudad, cont_ciudad, habilidades, max_habilidad, max_conteo, min_habilidad, min_conteo,niv_min_promedio, empresas_niv,  max_empresas, max_conteoo,min_empresas, min_conteoo, empresas_multilocations = model.req_7(control["model"],num_paises, fecha_inicial, fecha_final, tipo)
    return total_ofertas, total_ciudades, max_pais, cont_pais, max_ciudad, cont_ciudad, habilidades, max_habilidad, max_conteo, min_habilidad, min_conteo,niv_min_promedio, empresas_niv,  max_empresas, max_conteoo,min_empresas, min_conteoo, empresas_multilocations


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass




##### LABORATORIO 5 #####





