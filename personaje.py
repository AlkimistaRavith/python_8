
class Personaje:
    
    def __init__(self, nombre ="orco",):
        #atributos de instancia
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f"""
NOMBRE: {self.nombre}
NIVEL: {self.nivel}
EXPERIENCIA: {self.experiencia}"""

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




    #retornando variable como texto    
    def __str__(self):
        return f"{self.nombre}"



orco = Personaje("orco")
jugador = Personaje("guts")

jugador.estado = 120
print(jugador.estado)
