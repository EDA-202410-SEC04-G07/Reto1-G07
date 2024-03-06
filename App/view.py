"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import config as cf
import model
import sys
import controller
assert cf
#from tabulate import tabulate
import traceback
from Estructuras import Lista as lis

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo)
    return control
    


def print_menu():
    print()
    print("Bienvenido")
    print("1- Cargar información y elegir tipo de lista")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Seleccionar algoritmo de ordenamiento")
    print("11- Seleccionar muestra de jobs")
    print("12- Ordenar jobs alfabeticamente y por fecha de publicación")
    print("0- Salir")


def carga_de_datos_reto_1(control,tamaño, tipo):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    jobs,skills,multilocations, employments = controller.load_data(control,tamaño,tipo)                                                          
    datos = {"jobs":jobs, "skills": skills, "multilocations": multilocations, "employments": employments}                                                     
    return datos
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    
    pass

def print_req_1(control, tipo):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("Ordenando las Ofertas ...")
    cod_pais =   input("Ingrese el codigo de pais para filtrar la informacion:")
    niv_experticia =  input("Ingrese el nivel de experticia para filtrar la informacion:")
    num_ofertas = int(input("Ingrese el numero de ofertas que quiere mostrar:"))
    respuesta, tamaño = controller.req_1(control, num_ofertas, cod_pais, niv_experticia, tipo)
    
    print("El total de ofertas de trabajo ofrecidas según la condicion " + niv_experticia + " es de " + str(tamaño))
    i = 1
    while i <= tamaño and i <= num_ofertas:
            oferta = respuesta[i-1]
            print( str(i) + " . " + 'Fecha Publicacion: ' + oferta["published_at"] + " , " + 'Titulo oferta: ' +  oferta["title"] + " , " + 'Nombre Empresa: ' + oferta["company_name"]+ " , "  + 'Nivel experiencia: ' + oferta["experience_level"] + " , " + 'Pais empresa: ' + oferta["country_code"] + " , " + 'Ciudad Empresa: ' + oferta["city"] + " , " + 'Tamaño Empresa: ' + oferta["company_size"]+ " , "  + 'Tipo de Ubicación: ' + oferta["workplace_type"]+ " , "  + 'Disponible contratar ucranianos: ' + oferta["open_to_hire_ukrainians"])
            i += 1



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass



def print_req_3(control):

    empresa = input("Ingrese el nombre de la empresa: ")
    fecha_inicial = input("Ingrese la fecha inicial del periodo a consultar (formato %Y-%m-%d): ")
    fecha_final =  input("Ingrese la fecha final del periodo a consultar (formato %Y-%m-%d): ")

    ofertas_total, ofertas_junior, ofertas_mid, ofertas_senior, ofertas_empresa = controller.req_3(control)

    print()
    print("El total de ofertas de trabajo publicadas en el periodo buscado es de: " + str(ofertas_total))
    print("El numero de ofertas junior es de: " + str(ofertas_junior))
    print("El numero de ofertas mid es de: " + str(ofertas_mid))
    print("El numero de ofertas senior es de: " + str(ofertas_senior))

    print()
    print("Listado de ofertas de la empresa:")
    for oferta in ofertas_empresa:
        print(f"{oferta['fecha']} - {oferta['titulo']} - {oferta['nivel_experiencia']} - {oferta['ciudad']} - {oferta['pais']} - {oferta['tamaño_empresa']} - {oferta['lugar_trabajo']} - {oferta['contratar_ucranianos']}")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control, tipo):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    city = input("Ingrese una ciudad de busqueda:")
    fecha_inicial = input("Ingrese la fecha inicial de busqueda (formato %Y-%m-%d):")
    fecha_final =  input("Ingrese la fecha final de busqueda (formato %Y-%m-%d):")
    total_ofertas, dato_empresas, conteo_empresa, max_empresa, conteo_min, min_empresa, lista_ordenada = controller.req_5(control,city, fecha_inicial, fecha_final, tipo)
    print()
    print("El total de ofertas de trabajo publicadas en el periodo buscado es de: " + str(total_ofertas) + " ofertas")
    print("El total de empresas que publicaron por lo menos una oferta en la ciudad de consulta es de: " + str(dato_empresas) + " empresas")
    print("La empresa con el mayor numero de ofertas en el periodo fue: " + str(max_empresa) + " con " + str(conteo_empresa) + " ofertas")
    print("La empresa con el menor numero de ofertas en el periodo fue: " + str(min_empresa) + " con " + str(conteo_min) + " oferta/s")
    print()
    print("Listado de ofertas:")
    i = 1
    while i <= total_ofertas:
            oferta = lista_ordenada["elements"][i-1]
            print( str(i) + " . " + 'Fecha Publicacion: ' + oferta["published_at"] + " , " + 'Titulo oferta: ' +  oferta["title"] + " , " + 'Nombre Empresa: ' + oferta["company_name"]+  " , " +'Tipo de Ubicación: ' + oferta["workplace_type"] + " , " +'Tamaño Empresa: ' + oferta["company_size"])
            i += 1


def print_req_6(control,tipo
                ):
    def get_max_count(city_count_tuple):
        city, data = city_count_tuple
        return data["count"]

    def get_min_count(city_count_tuple):
        city, data = city_count_tuple
        return data["count"]

    def get_count(city_count_tuple):
        city, data = city_count_tuple
        return data["count"]

    N = int(input("Ingrese el número (N) de ciudades para consulta (ej.: 3, 5, 10 o 20): "))
    country = input("Ingrese el código del país para la consulta (ej.: PL, CO o ES). Este dato es opcional: ")
    experience = input("Ingrese el nivel de experticia de las ofertas de interés (junior, mid o senior): ")
    start_date = input("Ingrese la fecha inicial del periodo a consultar (con formato \"%Y-%m-%d\"): ")
    end_date = input("Ingrese la fecha final del periodo a consultar (con formato \"%Y-%m-%d\"): ")

    control = {"model": None}
    control["model"] = controller.req_6(control, country, start_date, end_date, experience)
    ofertas_con_skill = control["model"][0]
    empresas_con_skill = control["model"][1]
    promedio_ofertas_empresa = control["model"][2]

    city_counts = model.count_jobs_by_city(ofertas_con_skill)
    city_counts = model.mejor_peor_oferta_por_ciudad(city_counts)
    city_counts = model.promedio_salario_por_ciudad(city_counts)

    ciudad_filtrada = country if country else None

    resultado = {}
    num_cities = 0
    for city, data in city_counts.items():
        if data["count"] <= N and city == ciudad_filtrada:
            num_cities += 1
    resultado["num_cities"] = num_cities

    num_companies = len(set([offer["company_name"] for offer in ofertas_con_skill]))
    resultado["num_companies"] = num_companies

    num_offers = len(ofertas_con_skill)
    resultado["num_offers"] = num_offers

    avg_salary = 0
    if num_offers > 0:
        avg_salary = sum([data["salary_sum"] for data in city_counts.values()]) / num_offers
    resultado["avg_salary"] = avg_salary

    max_city_data = max(city_counts.items(), key=get_max_count)
    max_city = max_city_data[0]
    max_count = max_city_data[1]["count"]
    resultado["max_city"] = max_city
    resultado["max_count"] = max_count

    min_city_data = min(city_counts.items(), key=get_min_count)
    min_city = min_city_data[0]
    min_count = min_city_data[1]["count"]
    resultado["min_city"] = min_city
    resultado["min_count"] = min_count

    city_counts_tuples = [(city, data) for city, data in city_counts.items()]
    city_counts_tuples = sorted(city_counts_tuples, key=get_count, reverse=True)
    resultado["cities"] = city_counts_tuples

    return resultado
   


def print_req_7(control, tipo):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    num_paises = int(input("Ingrese la cantidad de paises en los que quiere ver ofertas: "))
    fecha_inicial = input("Ingrese la fecha inicial de busqueda (formato %Y-%m-%d): ")
    fecha_final =  input("Ingrese la fecha final de busqueda (formato %Y-%m-%d): ")
    total_ofertas, total_ciudades, max_pais, cont_pais, max_ciudad, cont_ciudad, habilidades, max_habilidad, max_conteo, min_habilidad, min_conteo, niv_min_promedio, empresas_niv,  max_empresas, max_conteoo,min_empresas, min_conteoo, empresas_multilocations = controller.req_7(control,num_paises, fecha_inicial, fecha_final, tipo)
    print()
    print("El total de ofertas de trabajo publicadas en el periodo buscado es de: " + str(total_ofertas) + " ofertas para " + str(num_paises) + " paises")
    print("El numero de ciudades donde se oferto trabajo es de: " + str(total_ciudades) + " ciudades")
    print("El país con mayor cantidad de ofertas es " +  str(max_pais)  + " con " + str(cont_pais) + " ofertas")
    print("La ciudad con mayor cantidad de ofertas es " +  str(max_ciudad)  + " con " + str(cont_ciudad) + " ofertas")
    print("El conteo de habilidades diferentes solicitadas en ofertas de trabajo es de " + str(habilidades) + " habilidades dado el nivel de experticia requerido")
    print("La habilidad más solicitada es " + str(max_habilidad)+ " y su conteo en ofertas de trabajo es de " + str(max_conteo) + " ofertas dado el nivel de experticia requerido") 
    print("La habilidad menos solicitada es " + str(min_habilidad) +   " y su conteo en ofertas de trabajo es de "+ str(min_conteo)+" ofertas dado el nivel de experticia requerido")
    print("EL nivel mínimo promedio (redondeado hacia abajo) de las habilidades es de " + str(niv_min_promedio) + " dado el nivel de experticia requerido")
    print("El conteo de empresas que publicaron una oferta con este nivel promedio es de " + str(empresas_niv)+ " empresas distintas dado el nivel de experticia requerido")
    print("La empresa con mayor número de ofertas con este nivel promedio es " + str(max_empresas) + " y su conteo es de " + str(max_conteoo) + " ofertas dado el nivel de experticia requerido")
    print("La empresa con menor número de ofertas (al menos una) con este nivel promedio es " + str(min_empresas) + " y su conteo es de "+ str(min_conteoo)+ " ofertas dado el nivel de experticia requerido")
    print("El número de empresas que publicaron una oferta en este nivel promedio que tienen una o más sedes es de " + str(empresas_multilocations) + " empresas dado el nivel de experticia requerido")


def print_req_8(control):
    """
    Función que imprime la solución del Requerimiento 8 en consola
    """
    pass

##### LABORATORIO 5 #####
    

def print_tipo_de_lista():
    tipo_lista = input("Si desea guardar la informacion en Array_list oprima 0. Si la quiere guardar en un linked_list oprima 1:")
    return tipo_lista

def printSortResults(sort_jobs, sample=3):

    size = lis.size(sort_jobs) 
    if size <= sample*2:
       print("Las", size, "ofertas ordenadas son:")
       for oferta in lis.iterator(sort_jobs): 
           print('Nombre Compañia: ' + oferta["company_name"] +'Ciudad: ' +  oferta["city"] + 'Fecha publicación oferta: ' + oferta["published_at"])
       print("Los", sample, "primeros libros ordenados son:")
       i=1
       while i <= sample:
           oferta = lis.getElement(sort_jobs, i)
           print('Nombre Compañia: ' + oferta["company_name"] + 'Ciudad: ' +  oferta["city"] + 'Fecha publicación oferta: ' + oferta["published_at"])
           i += 1

       print("Los", sample, "últimos libros ordenados son:")
       i = size - sample + 1
       while i <= size:
            oferta = lis.getElement(sort_jobs, i) 
            print('Nombre Compañia: ' + oferta["company_name"] + 'Ciudad: ' +  oferta["city"] + 'Fecha publicación oferta: ' + oferta["published_at"])
            i += 1
    




algo_str = """Seleccione un porcentaje o tamaño de archivo:
                1. 10%
                 2. 20%
                 3. 30%
                 4. 40%
                 5. 50%
                 6. 60%
                 7. 70%
                 8. 80%:
                 9. 90%
                 10. small
                 11. medium 
                 12. large: """
# main del reto

algo_st = """Seleccione el algoritmo de ordenamiento:
                1. Selection Sort ||
                 2. Insertion Sort ||
                 3. Shell Sort ||
                 4. Merge Sort ||
                 5. Quick Sort ||
                 6. Heap Sort ||
                 7. Bogo Sort ||
                 8. Custom Sort (Tim Sort o Patience Sort)):"""

if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            tamaño = input(algo_str)
            tamaño = int(tamaño)

            tipo = int(print_tipo_de_lista())
            control = new_controller(tipo)      
            print("Cargando información de los archivos ....\n")
            data = carga_de_datos_reto_1(control, tamaño, tipo)
            print(data)

        elif int(inputs) == 2:
            print_req_1(control, tipo)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control, tipo)

        elif int(inputs, tipo) == 7:
            print_req_6(control,tipo)

        elif int(inputs) == 8:
            print_req_7(control, tipo)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 10:
            algo_opt = input(algo_st)
            algo_opt = int(algo_opt)
            algo_msg = controller.setSortAlgorithm(algo_opt)
            print(algo_msg)

        elif int(inputs) == 11:
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            control = controller.setJobsSublist(control, size,tipo)

        elif int(inputs) == 12:
            # TODO completar modificaciones para el lab 5
            print("Ordenando las Ofertas ...")
            result = controller.sortJobs(control, tipo)
            sortedJobs = result[0]
            DeltaTime = f"{result[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",str(DeltaTime), "[ms]")
            

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


