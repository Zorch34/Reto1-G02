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
    print("3- Listar cronológicamente los artistas")
    print("4- Listar cronológicamente las adquisiciones")
    print("5- Clasificar las obras de un artista por técnica")
    print("6- Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Transportar obras de un departamento")
    print("8- Proponer una nueva exposición en el museo")
    print("9- Salir del Menu")

def initCatalog(Tipo_Arreglo):
    return controller.initCatalog(Tipo_Arreglo)

def loadData(catalog):
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        Tipo_Arreglo = input("Elige la opción ARRAY_LIST ó SINGLE_LINKED: ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog (Tipo_Arreglo)
        loadData (catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs[0]) == 2:
        Tipo_Algoritmo = input("Elige la opción Insertion, Shell, Merge o Quick Sorts: ")
        ordenado = controller.AlgoritmoIterativo(Tipo_Algoritmo, catalog)
        print("Para el catálogo con el tipo de ordenamiento:", Tipo_Algoritmo, "el tiempo de procesamiento es:", ordenado, "mseg")

    elif int(inputs[0]) == 3:
        A_I = input ("Ingresa el año inicial: ")
        A_FN = input ("Ingresa el año final: ")
        print("Lista cronologica de artistas: ")

    elif int(inputs[0]) == 4:
        F_I = input ("Ingresa la fecha inicial (AAAA-MM-DD): ")
        F_FN = input ("Ingresa la fecha final (AAAA-MM-DD): ")
        print("Lista cronologica de adquisiciones: ")

    elif int(inputs[0]) == 5:
        Name = input ("Ingresa el nombre del artista: ")
        print("Obras de un artista por técnica: ")

    elif int(inputs[0]) == 6:
        print("Obras por la nacionalidad de sus creadores: ")

    elif int(inputs[0]) == 7:
        DEP = input("Ingresa el departamento a consultar: ")
        print("Costo de transporte: ")

    elif int(inputs[0]) == 8:
        A_IO = input("Ingresa el año inicial de las obras: ")
        A_FO = input("Ingresa el año final de las obras: ")
        Area_D = input("Ingresa el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    else:
        sys.exit(9)
sys.exit(8)



