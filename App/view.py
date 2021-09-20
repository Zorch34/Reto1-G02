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
import sys
import controller
from DISClib.ADT import list as lt

assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar el tipo de algoritmo de ordenamiento iterativo")
    print("3- Req. 1. Listar cronológicamente los artistas")
    print("4- Req. 2. Listar cronológicamente las adquisiciones")
    print("5- Req. 3. Clasificar las obras de un artista por técnica")
    print("6- Req. 4. Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Req. 5. Transportar obras de un departamento")
    print("8- Req. 6. Proponer una nueva exposición en el museo")
    print("9- Salir del Menu")


def initCatalog(Tipo_Arreglo):
    return controller.initCatalog(Tipo_Arreglo)


def loadData(catalog):
    controller.loadData(catalog)


catalog = None


def primerosYUltimos(lista, tam_lista):
    print(lt.getElement(lista, 1))
    print(lt.getElement(lista, 2))
    print(lt.getElement(lista, 3))
    print(lt.getElement(lista, tam_lista - 2))
    print(lt.getElement(lista, tam_lista - 1))
    print(lt.getElement(lista, tam_lista))


def resp_req1():
    fecha_inicial = input("Ingresa el año inicial: ")
    fecha_final = input("Ingresa el año final: ")
    lista_artistas = controller.listarCronoArtistas(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_artistas)
    print("============ Respuesta Requerimiento 1 ============")
    print("La cantidad de artistas nacidos entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    print("Los primeros 3 y los ultimos 3 artistas en este rango son: ")
    primerosYUltimos(lista_artistas, tam_lista)


def resp_req2():
    fecha_inicial = input("Ingresa la fecha inicial (AAAA-MM-DD): ")
    fecha_final = input("Ingresa la fecha final (AAAA-MM-DD): ")
    lista_obras, cont = controller.listarCronoObras(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_obras)
    print("Lista cronologica de adquisiciones: ")
    print("============ Respuesta Requerimiento 2 ============")
    print("Obras adquiridas entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    print("La cantidad de obras adquiridas mediante compras es de " + str(cont))
    print("Las primeras 3 y los ultimas 3 obras en este rango son: ")
    primerosYUltimos(lista_obras, tam_lista)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        tipo_Arreglo = input("Elige la opción ARRAY_LIST ó SINGLE_LINKED: ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo_Arreglo)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs) == 2:
        tipo_Algoritmo = input("Elige la opción Insertion, Shell, Merge o Quick Sorts: ")
        ordenado = controller.AlgoritmoIterativo(tipo_Algoritmo, catalog)
        print("Para el catálogo con el tipo de ordenamiento:", tipo_Algoritmo, "el tiempo de procesamiento es:",
              ordenado, " milisegundos")

    elif int(inputs) == 3:
        resp_req1()

    elif int(inputs) == 4:
        resp_req2()

    elif int(inputs) == 5:
        Name = input("Ingresa el nombre del artista: ")
        print("Obras de un artista por técnica: ")

    elif int(inputs) == 6:
        print("Obras por la nacionalidad de sus creadores: ")

    elif int(inputs) == 7:
        DEP = input("Ingresa el departamento a consultar: ")
        print("Costo de transporte: ")

    elif int(inputs) == 8:
        A_IO = input("Ingresa el año inicial de las obras: ")
        A_FO = input("Ingresa el año final de las obras: ")
        Area_D = input("Ingresa el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    else:
        sys.exit(9)