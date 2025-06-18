from personaje import Personaje
import random

print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique el nombre de su personaje: ")


personaje = Personaje(nombre)

print(personaje.estado)

orco = Personaje("Orco")
prob = personaje.probabilidad(orco)
opcion = Personaje.mostrar_dialogo(prob)
count_w = 0
count_l = 0

while opcion == 1:
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

    prob = personaje.probabilidad(orco)
    opcion = Personaje.mostrar_dialogo(prob)

print("Has huido con éxito.\nTus estádisticas finales son:")
print(personaje.estado)
print(f"Batallas ganadas: {count_w} | Batallas perdidas: {count_l}.")