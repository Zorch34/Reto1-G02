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


from typing import BinaryIO
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qcks
from DISClib.Algorithms.Sorting import mergesort as mrgs


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos

def newCatalog(Tipo_Arreglo):
    catalog = {'artist': lt.newList(Tipo_Arreglo), 'artworks': lt.newList(Tipo_Arreglo)}
    return catalog


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    art = newArtist(artist['ConstituentID'], artist['DisplayName'],
                    artist['ArtistBio'], artist['Nationality'],
                    artist['Gender'], artist['BeginDate'],
                    artist['EndDate'], artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artist'], art)


def addArtworks(catalog, artworks):
    artw = newArtwork(artworks['ObjectID'], artworks['Title'], artworks['ConstituentID'],
                      artworks['Date'], artworks['Medium'], artworks['Dimensions'],
                      artworks['CreditLine'], artworks['AccessionNumber'], artworks['Classification'],
                      artworks['Department'], artworks['DateAcquired'], artworks['Cataloged'],
                      artworks['URL'], artworks['Circumference (cm)'], artworks['Depth (cm)'],
                      artworks['Diameter (cm)'], artworks['Height (cm)'], artworks['Length (cm)'],
                      artworks['Weight (kg)'], artworks['Width (cm)'], artworks['Seat Height (cm)'],
                      artworks['Duration (sec.)'])
    lt.addLast(catalog['artworks'], artw)


# Funciones para creacion de datos

def newArtist(ConstituentID, DisplayName, ArtistBio, Nationality, Gender, BeginDate, EndDate, WikiQID, ULAN):
    artist = {'ConstituentID': ConstituentID, 'DisplayName': DisplayName, 'ArtistBio': ArtistBio, 'Nacionality': '',
              'Gender': Gender, 'BeginDate': BeginDate, 'EndDate': EndDate, 'WikiQID': WikiQID, 'ULAN': ULAN,
              'Nationality': Nationality}

    return artist


def newArtwork(ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine, AccessionNumber, Classification,
               Department, DateAcquired, Cataloged, URL, Circumference, Depth, Diameter, Height, Length, Weight, Width,
               SeatHeight, Duration):
    artwork = {'ObjectID': ObjectID, 'Title': Title, 'ConstituentID': ConstituentID, 'Date': Date, 'Medium': Medium,
               'Dimensions': Dimensions, 'CreditLine': CreditLine, 'AccessionNumber': AccessionNumber,
               'Classification': Classification, 'Department': Department, 'DateAcquired': DateAcquired,
               'Cataloged': Cataloged, 'URL': URL, 'Circumference': Circumference, 'Depth': Depth,
               'Diameter': Diameter, 'Height': Height, 'Length': Length, 'Weight': Weight, 'Width': Width,
               'SeatHeight': SeatHeight, 'Duration': Duration}

    return artwork


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] < artwork2["DateAcquired"]:
        r = True
    else:
        r = False
    return r


def cmpArtistByBornDate(artist1, artist2):
    if artist1["BeginDate"] < artist2["BeginDate"]:
        r = True
    else:
        r = False
    return r


# Ordenar y clasificar artistas
def cronologicoArtistas(fecha_inicial, fecha_final, catalog):
    lista_ordenada = ins.sort(catalog['artist'], cmpArtistByBornDate)['elements']
    lista_final = lt.newList()
    for artista in lista_ordenada:
        if fecha_final >= artista['BeginDate'] >= fecha_inicial:
            lt.addLast(lista_final, artista)

    return lista_final


def cronologicoObras(fecha_inicial, fecha_final, catalog):
    lista_ordenada = ins.sort(catalog['artworks'], cmpArtworkByDateAcquired)['elements']
    lista_final = lt.newList()
    cont = 0
    for artwork in lista_ordenada:
        if fecha_final >= artwork['DateAcquired'] >= fecha_inicial:
            lt.addLast(lista_final, artwork)
            if 'Purchase' in artwork['CreditLine'] or 'purchase' in artwork['CreditLine']:
                cont += 1

    return lista_final, cont


# Funciones de ordenamiento

def AlgoritmoIterativo(Tipo_Algoritmo, catalog):
    elapsed_time_mseg = 0
    if Tipo_Algoritmo == 'Insertion':
        start_time = time.process_time()
        sorted_list = ins.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Shell':
        start_time = time.process_time()
        sorted_list = sa.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Merge':
        start_time = time.process_time()
        sorted_list = mrgs.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Quick Sorts':
        start_time = time.process_time()
        sorted_list = qcks.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    return elapsed_time_mseg