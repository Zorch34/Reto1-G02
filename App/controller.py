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

import config as cf
import model
import csv
from DISClib.Utils import error as error
from DISClib.DataStructures import liststructure as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros
def initCatalog(Tipo_Arreglo):
    catalog = model.newCatalog(Tipo_Arreglo)
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)


def loadArtists(catalog):
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artworks in input_file:
        model.addArtworks(catalog, artworks)


# Funciones de ordenamiento

def AlgoritmoIterativo(Tipo_Algoritmo, catalog):
    Algoritmo = model.AlgoritmoIterativo(Tipo_Algoritmo, catalog)
    return Algoritmo


# Funciones de consulta sobre el catálogo
def subList(lst, pos, numelem):
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')


# Funciones listar cronologicamente
def listarCronoArtistas(fecha_inicial, fecha_final, catalog):
    return model.cronologicoArtistas(fecha_inicial, fecha_final, catalog)


def listarCronoObras(fecha_inicial, fecha_final, catalog):
    return model.cronologicoObras(fecha_inicial, fecha_final, catalog)