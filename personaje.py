
class Personaje:
    
    def __init__(self, nombre ="orco",):
        #atributos de instancia
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} | NIVEL: {self.nivel} | EXPERIENCIA: {self.experiencia}"
    
    #Para modificar el estado
    @estado.setter
    def estado(self, exp):
        tmp_exp = self.experiencia + exp

        while tmp_exp > 99:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0:
            if self.nivel == 1:
                self.experiencia = 0
                tmp_exp = 0
            else:
                self.nivel -= 1
                tmp_exp += 100
        
        self.experiencia = tmp_exp


    def __lt__(self, oponente):
        #sobrecarga para metodo de menor que
        return self.nivel < oponente.nivel
    
    def __gt__(self, oponente):
        #sobrecarga para metodo de mayor que
        return self.nivel > oponente.nivel

    def __eq__(self, oponente):
        #sobrecarga para metodo de igual
        return self.nivel == oponente.nivel

    def probabilidad(self, oponente):
        #Si el jugador es menor al orco, tiene un 33% de probabilidades de ganar.
        if self < oponente:
            return 33
        #Si el jugador es mayor al orco, tiene un 66% de probabilidades de ganar.
        elif self > oponente:
            return 66
        #Si el jugador es igual al orco, tiene un 50% de probabilidades de ganar.
        else:
            return 50
        
    @staticmethod   
    def mostrar_dialogo(prob):
        return int(input(f"""
¡Oh no!, ¡Ha aparecido un Orco!
Con tu nivel actual, tienes {prob}% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
1. Atacar
2. Huir
Ingresa tu opción: 
"""))

