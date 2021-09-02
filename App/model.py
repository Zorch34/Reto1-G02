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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
   
    catalog = {'artworks': None,
               'artists': None,
               }

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartists)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addartwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    artists = artwork['artists'].split(",")
    for artist in artists:
        addartworkartist(catalog, artist.strip(), artwork)

def addartworkartist(catalog, authorname, artwork):
    artists = catalog['artists']
    posartist = lt.isPresent(artists, authorname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newartist(authorname)
        lt.addLast(artists, artist)
    lt.addLast(artist['artworks'], artwork)

# Funciones para creacion de datos

def newartist(name):
    artists = {'name': "", "artworks": None}
    artists['name'] = name
    artists['artworks'] = lt.newList('SINGLE_LINKED')
    return artists
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareartists(authorname1, artists):
    if (authorname1.lower() in artists['name'].lower()):
        return 0
    return -1
# Funciones de ordenamiento
