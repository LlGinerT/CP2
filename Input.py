import string

""" Se crea esta clase que nos permite manejar las excepciones de los datos introducidos por el usuario,
y en el caso de este ejercicio, la podemos reutilizar tanto para los parámetros necesarios para instanciar la clase Persona,
como para la selección de las opciones del menu """


class Input_Check:
    # Función que devolverá un error tanto si el valor introducido no es un numero entero o es negativo.
    def numeros():
        while True:
            try:
                numero = int(input())
                if numero <= 0:
                    print(
                        "Valor no valido\nPor favor, introduzca un valor numérico valido"
                    )
                else:
                    return numero
            except ValueError:
                print("Valor no valido\nPor favor, introduzca un valor numérico valido")

    # Función que devolverá un error si el valor introducido no es una cadena de caracteres alfabéticos
    def caracter():
        while True:
            try:
                cadena_comprobada = str(input())
                """  Comprueba si cualquier carácter no deseado (dígitos o caracteres especiales) 
                dentro de los métodos de python .punctuation y .digits 
                se encuentran dentro de la cadena introducida por el usuario, mediante los iterables any() y for """
                if any(
                    caracter in string.punctuation for caracter in cadena_comprobada
                ) or any(caracter in string.digits for caracter in cadena_comprobada):
                    print(
                        "Carácter no valido\nPor favor, introduzca un caracteres validos"
                    )
                else:
                    return cadena_comprobada
            except ValueError:
                print("Carácter no valido\nPor favor, introduzca un caracteres validos")
