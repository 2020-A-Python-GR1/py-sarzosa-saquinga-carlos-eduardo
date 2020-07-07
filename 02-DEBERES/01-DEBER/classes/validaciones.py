import datetime


class Validaciones:

    def __init__(self):
        pass

    # ---------------------------------#
    #      Método Validar Nombre       #
    # ---------------------------------#
    def validarNombre(self, nombre):
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValueError(f'El nombre debe tener como mínimo 3 caractares y un máximo de 50 caracteres, tamaño actual: {len(nombre)}')
        return True

    # ---------------------------------#
    #      Método Validar Categoria    #
    # ---------------------------------#
    def validarCategoria(self, categoria):
        if len(categoria) < 5 or len(categoria) > 100:
            raise ValueError(f'Las categorias deben tener como mínimo 5 caractares y un máximo de 100 caracteres, tamaño actual: {len(categoria)}')
        return True

    # ---------------------------------#
    #      Método Validar Duracion     #
    # ---------------------------------#
    def validarDuracion(self, duracion):
        try:
            datetime.datetime.strptime(duracion, '%H:%M')
        except ValueError:
            raise ValueError('El formato de la duracion es incorrecta, debe ser h:mm')
        return True

    # ---------------------------------#
    #    Método Validar Calificacion   #
    # ---------------------------------#
    def validarCalificacion(self, calificacion):
        if int(calificacion) < 1 or int(calificacion) > 10:
            raise ValueError('El formato de calificación no es válido, debe ser un número entre 1-10')
        return True

    # ---------------------------------#
    #      Método Validar Anio         #
    # ---------------------------------#
    def validarAnio(self, anio):
        try:
            datetime.datetime.strptime(anio, '%Y')
        except ValueError:
            raise ValueError('El formato de la fecha es incorrecta, debe ser YYYY')
        return True