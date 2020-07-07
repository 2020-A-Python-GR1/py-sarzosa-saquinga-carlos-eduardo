from .cursos import Cursos
from .dbcsv import DBcsv

ESQUEMA = {
    'ID': {
        'type': 'autoincrement',
    }, 
    'NOMBRE': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'CATEGORIA': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'DURACION': {
        'type': 'string',
        'max_length': 254
    }, 
    'CALIFICACION': {
        'type': 'int'
    }, 
    'ANIO': {
        'type': 'date'
    }
}

class DBCursos(DBcsv):

    def __init__(self):
        super().__init__(ESQUEMA, 'cursos')


    def crear_curso(self, curso):
        data = [curso.nombre, curso.categoria, curso.duracion, curso.calificacion, curso.anio]
        return self.insert(data)


    def listar_curso(self):
        list_cursos = self.get_all()
        return self._create_object_cursos(list_cursos)


    def actualizar_curso(self, id_object, data):
        if not id_object:
            raise ValueError('Debes envíar el id del curso')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(id_object, data)


    def eliminar_curso(self, id_object):
        if not id_object:
            raise ValueError('Debes envíar el id del curso')
        self.delete(id_object)


    def buscar_curso(self, filters):
        if 'NOMBRE' not in filters and 'CATEGORIA' not in filters and 'CALIFICACION' not in filters and 'ANIO' not in filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_cursos = self.get_by_filters(filters)
        return self._create_object_cursos(list_cursos)


    def _create_object_cursos(self, list_cursos):

        if not list_cursos:
            return None

        object_cursos = []

        # Convertimos los datos a objetos de tipo curso
        for curso in list_cursos:
            c = Cursos(curso['ID'], curso['NOMBRE'], curso['CATEGORIA'], curso['DURACION'], curso['CALIFICACION'], curso['ANIO'])
            object_cursos.append(c)

        return object_cursos


    def get_esquema(self):
        return ESQUEMA