from poblacion import *

def test_lee_poblaciones(ruta_fichero):
    poblacion = lee_poblaciones(ruta_fichero)
    print('Muestra las tres primeras')
    print(poblacion[:4])


def test_calcula_paises(poblaciones):
    poblaciones = lee_poblaciones(ruta_fichero)
    paises = calcula_paises(poblaciones)
    for i in paises[:3]:
        print(i)


def test_filta_por_pais(poblaciones):
    nombre_o_codigo = 'Albania'
    paises = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(paises)

def test_filtra_por_paises_y_anyo(poblaciones):
    anyo = 2001
    paises ='Albania'
    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    print(datos)

def test_muestra_evolucion_poblacion(poblaciones):
    nombre_o_codigo = 'ESP'
    datos = muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)
    print(datos)


def test_muestra_comparativa_paises_anyo(poblaciones):
    anyo = 2016
    paises = {'China', 'France', 'Mexico', 'Portugal', 'Spain'}
    datos = muestra_comparativa_paises_anyo(poblaciones, anyo, paises)
    print(datos)


if __name__ == '__main__':
    ruta_fichero = 'data\population.csv'
    poblaciones = lee_poblaciones(ruta_fichero)

    #test_lee_poblaciones(ruta_fichero)
    #test_calcula_paises(poblaciones)
    #test_filta_por_pais(poblaciones)
    #test_filtra_por_paises_y_anyo(poblaciones)
    #test_muestra_evolucion_poblacion(poblaciones)
    test_muestra_comparativa_paises_anyo(poblaciones)