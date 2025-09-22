class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre_gato(self):
        return self.nombre

    def set_nombre_gato(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_edad_gato(self):
        return self.edad

    def set_edad_gato(self, nueva_edad):
        self.edad = nueva_edad

    def __str__(self):
        return f"Gato(nombre={self.nombre}, edad={self.edad})"
