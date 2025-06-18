from personaje import Personaje
import random

print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique el nombre de su personaje: ")


personaje = Personaje(nombre)

print(personaje.estado)

orco = Personaje("Orco")
#contador de ganadas
count_w = 0
#contador de perdidas
count_l = 0
#condicionante para ciclo while:
opcion = 0

while opcion == 0:
    try:
        #calcula probabilidad de ganar
        prob = personaje.probabilidad(orco)
        #pregunta si se desea pelear o huir.
        opcion = Personaje.mostrar_dialogo(prob)

        if opcion == 1:
            resultado = "win" if random.uniform(0,100) < prob else "lose"
            if resultado == "win":
                print("""
    ¡Le has ganado al orco, felicidades!
    ¡Recibirás 50 puntos de experiencia!
    """)
                personaje.estado = 50
                orco.estado = -30
                count_w += 1
            else:
                print("""
    ¡Oh no! ¡El orco te ha ganado!
    ¡Has perdido 30 puntos de experiencia!
    """)
                personaje.estado = -30
                orco.estado = 50
                count_l += 1
            
            print(personaje.estado)
            print(orco.estado)
            #Se retoma valor 0, para mantener dentro de while.
            opcion = 0

        elif opcion == 2:
            break
        else:
            #Se retoma valor 0, para mantener dentro de while.
            print("¡Esa acción no es válida!")
            opcion = 0
    except ValueError:
        print("Esa acción no existe, inténtalo de nuevo.")
        opcion = 0

print("Has huido con éxito.\nTus estádisticas finales son:")
print(personaje.estado)
print(f"Batallas ganadas: {count_w} | Batallas perdidas: {count_l}.")