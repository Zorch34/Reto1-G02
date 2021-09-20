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
from controller import loadData
from controller import initCatalog


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1-Ejecutar requerimiento 1")
    print("2-Ejecutar requerimiento 2")
    print("3-Ejecutar requerimiento 3")
    print("4-Ejecutar requerimiento 4")
    print("5-Ejecutar requerimiento 5")
    print("6-Ejecutar requerimiento 6")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
    elif int(inputs[1]) == 1:
        print("Ejecutando requerimiento 1 ...")
    elif int(inputs[2]) == 2:
        print("Ejecutando requerimiento 2 ...")
    elif int(inputs[3]) == 3:
        print("Ejecutando requerimiento 3 ...")
    elif int(inputs[4]) == 4:
        print("Ejecutando requerimiento 4 ...")
    elif int(inputs[5]) == 5:
        print("Ejecutando requerimiento 5 ...")
    elif int(inputs[6]) == 6:
        print("Ejecutando requerimiento 6 ...")
    else:
        sys.exit(0)
    if int(inputs[0]) == 1:
        Tipo_Arreglo = input("Elige una opción ARRAY_LIST ó SINGLE_LINKED: ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog (Tipo_Arreglo)
        loadData (catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs[0]) == 2:
        Tipo_Algoritmo = input("Elige una  opción Insertion, Shell, Merge o Quick Sorts: ")
        ordenado = controller.AlgoritmoIterativo(Tipo_Algoritmo, catalog)
        print("Para el catálogo con el tipo de ordenamiento:", Tipo_Algoritmo, "el tiempo de procesamiento es:", ordenado, "mseg")
sys.exit(0)
