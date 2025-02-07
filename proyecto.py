class Personaje:
    def __init__(self, nombre, salud=100):
        self.nombre = nombre
        self.salud = salud

    def atacar(self):
        print(f"El personaje {self.nombre} ataca")

    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            return False

class Guerrero(Personaje):
    def __init__(self, nombre, salud=120, fuerza=15):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, enemigo):
        enemigo.salud -= self.fuerza
        print(f"Guerrero {self.nombre} ataca con {self.fuerza} de fuerza")

class Mago(Personaje):
    def __init__(self, nombre, salud=90, poder_magico=20):
        super().__init__(nombre, salud)
        self.poder_magico = poder_magico

    def atacar(self, enemigo):
        enemigo.salud -= self.poder_magico
        print(f"Mago {self.nombre} ataca con {self.poder_magico} de poder mágico")

def combate():
    guerrero = Guerrero("Juan")
    mago = Mago("Ismael")
    turno = 0
    while mago.esta_vivo() and guerrero.esta_vivo():
        if turno % 2 == 0:
            guerrero.atacar(mago)
            print(f"Salud actual del mago: {mago.salud}")
            print(f"Salud actual del guerrero: {guerrero.salud}")
            turno += 1
        else:
            mago.atacar(guerrero)
            print(f"Salud actual del mago: {mago.salud}")
            print(f"Salud actual del guerrero: {guerrero.salud}")
            turno += 1
        if not mago.esta_vivo() or not guerrero.esta_vivo():
            break

    if mago.esta_vivo():
        print("El combate se ha terminado")
        print("El mago ha ganado el combate")
    else:
        print("El combate se ha terminado")
        print("El guerrero ha ganado el combate")

combate()
