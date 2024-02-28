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

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs()
    return control



# Funciones para la carga de datos

def load_data(control):
    jobs = load_jobs(control)
    skills = load_skills(control)
    multilocations= load_multilocations(control)
    employments = load_employments(control)
    return jobs, skills, multilocations, employments

def load_jobs(control):

    data_structs = control["model"]
    file = os.path.join(cf.data_dir, "large-jobs.csv")
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for job in input_file:
        model.add_job(data_structs, job)
    return model.jobs_size(data_structs)

def load_skills(control):

    data_structs = control["model"]
    file = os.path.join(cf.data_dir, "large-skills.csv")
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for skills in input_file:
        model.add_skills(data_structs, skills)
    return model.skills_size(data_structs)

def load_multilocations(control):

    data_structs = control["model"]
    file = os.path.join(cf.data_dir, "large-multilocations.csv")
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for multilocations in input_file:
        model.add_multilocations(data_structs, multilocations)
    return model.multilocations_size(data_structs)


def load_employments(control):

    data_structs = control["model"]
    file = os.path.join(cf.data_dir, "large-employments_types.csv")
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=";")
    for employments in input_file:
        model.add_employments(data_structs,employments)
    return model.employments_size(data_structs)






def setJobsSublist(control, size):
    """
    Retorna una sublista de libros
    """
    # TODO nuevo del lab 5 (Parte 2)
    data_structs = control["model"]
    control["model"] = model.setJobsSublist(data_structs, size)
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


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed



##### LABORATORIO 5 #####


def iniciar_datos_lab(control, tipo_lista):
    catalogo = model.estructura_datos(tipo_lista)
    model.load_data(catalogo)
    model.sort(catalogo)
    return catalogo


def sublista(catalogo, muestra):
    """
    muestra dada por el usuario
    """
    for i in range(muestra):
        oferta = lis.get_at(catalogo, i)
        print(f"{i + 1}.- {oferta['company_name']} - {oferta['published_at']}")


