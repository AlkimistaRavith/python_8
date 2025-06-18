from personaje import Personaje
import random

print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique el nombre de su personaje: ")


personaje = Personaje(nombre)

print(personaje.estado)

orco = Personaje("Orco")
prob = personaje.probabilidad(orco)
opcion = Personaje.mostrar_dialogo(prob)

while opcion == 1:
    resultado = "win" if random.uniform(0,100) < prob else "lose"
    if resultado == "win":
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
""")
        personaje.estado = 50
        orco.estado = -30
    else:
        print("""
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!
""")
        personaje.estado = -30
        orco.estado = 50
    
    print(personaje.estado)
    print(orco.estado)

    prob = personaje.probabilidad(orco)
    opcion = Personaje.mostrar_dialogo(prob)

print("has huido con éxito.")