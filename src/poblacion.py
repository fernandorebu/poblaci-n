from collections import namedtuple
from matplotlib import pyplot as plt
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero): 
    lista = []
    with open(ruta_fichero, encoding="utf-8")as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            Registropoblacion = RegistroPoblacion(pais, codigo, año, censo)
            lista.append(Registropoblacion)
        return lista
    


def calcula_paises(poblaciones):
    conjunto = set()
    for poblacion in poblaciones:
        conjunto.add(poblacion.pais)
    return sorted(conjunto, reverse=False)


def filtra_por_pais(poblaciones, nombre_o_codigo):
    lista = []
    for poblacion in poblaciones:
        if poblacion.pais == nombre_o_codigo or poblacion.codigo == nombre_o_codigo:
            lista.append(
                (poblacion.año, poblacion.censo)
                )
    return lista

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    lista = []
    for poblacion in poblaciones:
        if (poblacion.año == anyo) and (poblacion.pais in paises):
            lista.append((poblacion.pais, poblacion.censo))
    return lista


def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    titulo = 'Tabla'
    lista_años = []
    lista_habitantes = []
    datosl = filtra_por_pais(poblaciones, nombre_o_codigo)
    # Te devuelve una lista con tuplas (año, censo) entonces tengo que recorerrer la lista con un for
    for año, habitantes in datosl:
        lista_años.append(año)
        lista_habitantes.append(habitantes)
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = []
    lista_habitantes = []
    titulo = ' Na'
    datosl = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    for pais, censo in datosl:
        lista_paises.append(pais)
        lista_habitantes.append(censo)
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()