class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    # def __str__(self):
    #     return f"Nombre: {self.nombre}, Edad: {self.edad}" //__Str__ sirve para imprimir el objeto directamente