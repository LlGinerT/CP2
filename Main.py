from faker import Faker
from random import randint
from Persona import Persona
from Input import Input_Check


def main():
    # Iniciamos con la variable continuar en True para crear un bucle donde el menu se muestre
    # hasta que decidamos cerrar el programa, saltándonos el mensaje de bienvenida.
    continuar = True
    print("Bienvenido, escoja una opción:")
    while continuar:
        print("1.Test rápido, generar persona aleatoria")
        print("2.Generar persona manualmente")
        # Continuamos con un segundo bucle que se ejecutara hasta que no se capture
        # ningún error en el input del usuario.
        while True:
            match Input_Check.numeros():
                # El primer case, generara una instancia de persona con nombre y edad aleatorio
                # cada vez que se ejecute el test rápido se obtendrá uno diferente.
                case 1:
                    fake = Faker()
                    nombre_aleatorio = fake.name()
                    edad_aleatoria = randint(1, 100)
                    persona_aleatoria = Persona()
                    persona_aleatoria.nombre = nombre_aleatorio
                    persona_aleatoria.edad = edad_aleatoria
                    print(persona_aleatoria)
                    break

                # El segundo case, generara una instancia de Persona donde los parámetros los deberá
                # introducir el usuario
                case 2:
                    print("Introduzca el nombre:")
                    nombre_comprobado = Input_Check.caracter()
                    print("Introduzca la edad:")
                    edad_comprobada = Input_Check.numeros()
                    persona_instanciada = Persona()
                    persona_instanciada.nombre = nombre_comprobado
                    persona_instanciada.edad = edad_comprobada
                    print(persona_instanciada)
                    break

                # Devuelve un error si se introduce una opción no valida y volverá al inicio del bucle.
                case _:
                    print(
                        "No existe esa opción\nPor favor, vuelva a seleccionar una opción correcta:"
                    )

        print("Desea realizar otra acción?(S/N)")
        # En este tercer bucle, según la opción elegida se reiniciara o se finalizara el programa.
        while True:
            respuesta = Input_Check.caracter()
            match respuesta.upper():
                case "S":
                    break
                case "N":
                    continuar = False
                    break
                case _:
                    print(
                        "No existe esa opción\nPor favor, vuelva a seleccionar una opción correcta:"
                    )


if __name__ == "__main__":
    main()
