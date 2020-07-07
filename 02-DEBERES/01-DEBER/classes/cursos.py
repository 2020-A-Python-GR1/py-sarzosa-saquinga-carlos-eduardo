class Cursos:

    # ---------------------------------#
    #        Método Constructor        #
    # ---------------------------------#
    def __init__(self, id_curso, nombre, categoria, duracion, calificacion, anio):
        self._id_curso = id_curso
        self._nombre = nombre
        self._categoria = categoria
        self._duracion = duracion
        self._calificacion = calificacion
        self._anio = anio

    # ---------------------------------#
    #  Getters Setters Clase Curso     #
    # ---------------------------------#
    @property
    def id_curso(self):
        return self._id_curso

    @id_curso.setter
    def id_curso(self, id_curso):
        self._id_curso = id_curso

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        self._calificacion = calificacion

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio