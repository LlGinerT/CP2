class Persona:
    # Definimos la clase persona con su constructor , los getter y setter de sus parámetros.
    def __init__(self) -> None:
        self._nombre = "X"
        self._edad = 0

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    """ Usamos el método __str__ por conveniencia del ejercicio para imprimir todos los parámetros del objeto
    con solo una instrucción, los getter definidos, aunque no se usan, creo que serian mejor opción por si 
    necesitáramos acceder a los parámetros por separado. """

    def __str__(self) -> str:
        return f"Persona generada:\nNombre:{self._nombre}\nEdad:{self._edad}"
