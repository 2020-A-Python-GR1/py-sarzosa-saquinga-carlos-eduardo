import os
import time

from classes.cursos import Cursos
from classes.dbcursos import DBCursos
from classes.validaciones import Validaciones


from prettytable import PrettyTable

validador = Validaciones()
db = DBCursos()

# ---------------------------------#
#    Método Iniciar Programa       #
# ---------------------------------#
def iniciar():

    imprimir_opciones()
    command = input()
    command = command.upper()

    if command == '1':
        crear_curso()
    elif command == '2':
        buscar_curso()
    elif command == '3':
        actualizar_curso()
    elif command == '4':
        eliminar_curso()
    elif command == '5':
        listar_curso()
    elif command == '6':
        os._exit(1)
    else:
        print('Comando inválido')

    time.sleep(1)
    iniciar()

# ---------------------------------#
#     Método Imprimir Opciones     #
# ---------------------------------#
def imprimir_opciones():
    print('CURSOS')
    print('-' * 30)
    print('Selecciona una opción:')
    print('1. Crear curso')
    print('2. Buscar cursos')
    print('3. Actualizar curso')
    print('4. Eliminar curso')
    print('5. Listar cursos')
    print('6. Salir')
    print('-' * 30)
    print('Ingresar Opción:')

# ---------------------------------#
# Método Revisar Datos de Curso    #
# ---------------------------------#
def revisar_datos_curso(message, data_name, force = True):
    print(message)
    input_data = input()
    if not force and not input_data:
        return
    try:
        getattr(validador, f'validar{data_name.capitalize()}')(input_data)
        return input_data
    except ValueError as err:
        print(err)
        revisar_datos_curso(message, data_name)


# ---------------------------------#
#       Método Crear Curso         #
# ---------------------------------#
def crear_curso():

    print('CREACIÓN DE CURSO')
    print('-' * 50)

    nombre = revisar_datos_curso('Inserta el Nombre:', 'nombre')
    categoria = revisar_datos_curso('Inserta la Categoria:', 'categoria')
    duracion = revisar_datos_curso('Inserta la Duracion (hh:mm) :', 'duracion')
    calificacion = revisar_datos_curso('Inserta el Calificacion (1-10):', 'calificacion')
    anio = revisar_datos_curso('Inserta el Año (AAAA):', 'anio')

    curso = Cursos(None, nombre, categoria, duracion, calificacion, anio)
    if db.crear_curso(curso):
        print('Curso creado con éxito')
    else:
        print('Error al guardar el curso')


# ---------------------------------#
#       Método Buscar Curso        #
# ---------------------------------#
def buscar_curso():

    filtros = {}

    print('Introduce el nombre del curso (vacío para usar otro filtro):')
    nombre = input()
    if nombre:
        filtros['NOMBRE'] = nombre

    print('Introduce una categoria (vacío para usar otro filtro):')
    categoria = input()
    if categoria:
        filtros['CATEGORIA'] = categoria

    print('Introduce una calificacion (1-10)(vacío para usar otro filtro):')
    calificacion = input()
    if calificacion:
        filtros['CALIFICACION'] = calificacion

    print('Introduce una año (AAAA) (vacío para usar otro filtro):')
    anio = input()
    if anio:
        filtros['ANIO'] = anio

    try:
        list_cursos = db.buscar_curso(filtros)
        if not list_cursos:
            return print('No hay ningún curso con esos criterios de búsqueda')

        _imprimir_tabla_curso(list_cursos)
    except ValueError as err:
        print(err)
        time.sleep(1)
        buscar_curso()

# ---------------------------------#
#      Método Actualizar Curso     #
# ---------------------------------#
def actualizar_curso():

    listar_curso()

    print('Introduce el id del curso que quieres actualizar:')
    id_object = input()

    data = {}

    nombre = revisar_datos_curso('Introduce un nombre:', 'nombre', False)
    if nombre:
        data['NOMBRE'] = nombre

    categoria = revisar_datos_curso('Introduce una categoría:', 'categoria', False)
    if categoria:
        data['CATEGORIA'] = categoria

    duracion = revisar_datos_curso('Introduce un duracion (hh:mm):', 'duracion', False)
    if duracion:
        data['DURACION'] = duracion

    calificacion = revisar_datos_curso('Introduce una calificacion (1-10):', 'calificacion', False)
    if calificacion:
        data['CALIFICACION'] = calificacion

    anio = revisar_datos_curso('Introduce un Año:', 'anio', False)
    if anio:
        data['ANIO'] = anio
    
    try:
        res = db.update(id_object, data)
        if res:
            print('Curso actualizado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        actualizar_curso()

# ---------------------------------#
#      Método Eliminar Curso       #
# ---------------------------------#
def eliminar_curso():
    listar_curso()

    print('Introduce el id del curso que quieres eliminar:')
    id_object = input()
    try:
        res = db.delete(id_object)
        if res:
            print('Curso eliminado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        eliminar_curso()

# ---------------------------------#
#       Método Listar Curso        #
# ---------------------------------#
def listar_curso():
    list_curso = db.listar_curso()

    if not list_curso:
        return print('Todavía no hay cursos guardados')

    _imprimir_tabla_curso(list_curso)

# ---------------------------------#
# Método Imprimir Tabla de Cursos  #
# ---------------------------------#
def _imprimir_tabla_curso(list_cursos):
    tabla = PrettyTable(db.get_esquema().keys())

    for curso in list_cursos:
        tabla.add_row([
            curso.id_curso,
            curso.nombre,
            curso.categoria,
            curso.duracion,
            curso.calificacion,
            curso.anio
        ])

    print(tabla)
    print('Pulsa cualquier letra para continuar')
    command = input()

if __name__ == "__main__":
    iniciar()