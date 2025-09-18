

class vehiculo:
    def __init__(self, patente, marca, anio, mensaje_desplazamiento,posicion_inicial=0):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.posicion_inicial = posicion_inicial
        self.mensaje_desplazamiento = mensaje_desplazamiento
    
    def trasladarse(self, desplazamiento):
        self.posicion_inicial += desplazamiento
        return f"El vehiculo se desplazo {self.posicion_inicial} por {self.mensaje_desplazamiento}"


class Auto(vehiculo):
    def __init__(self, patente, marca, anio, mensaje_desplazamiento="tierra",posicion_inicial=0):  # Completa con los atributos necesarios
        super().__init__(patente, marca, anio, mensaje_desplazamiento,posicion_inicial)




class Lancha(vehiculo):
    def __init__(self, patente, marca, anio, marca_motor,mensaje_desplazamiento="Agua a motor",posicion_inicial=0):  # Completa con los atributos necesarios
        super().__init__(patente, marca, anio, mensaje_desplazamiento,posicion_inicial)
        self.marca_motor = marca_motor



class Velero(vehiculo):
    def __init__(self, patente, marca, anio, cantidad_velas, mensaje_desplazamiento="Agua a vela",posicion_inicial=0):  # Completa con los atributos necesarios
        super().__init__(patente, marca, anio, mensaje_desplazamiento,posicion_inicial)
        self.cantidad_velas = cantidad_velas





class Anfibio(vehiculo):
    def __init__(self, patente, marca, anio, mensaje_desplazamiento="Tierra",posicion_inicial=0):  # Completa con los atributos necesarios
        super().__init__(patente, marca, anio, mensaje_desplazamiento,posicion_inicial)

    def trasladarse_por_agua(self, desplazamiento):
        self.posicion_inicial += desplazamiento
        self.mensaje_desplazamiento = "Agua a motor"
        return f"El vehiculo se desplazo {self.posicion_inicial} por {self.mensaje_desplazamiento}"



A4 = Auto("AE192BDC", "AUDI", 2020)
lanchita = Lancha("AE192BDC", "AUDI", 2020,"yamaha")
velero = Velero("AE192BDC", "AUDI", 2020,10)
anfibio = Anfibio("AE192BDC", "AUDI", 2020)

print(A4.trasladarse(10))
print(lanchita.trasladarse(10))
print(velero.trasladarse(10))
print(anfibio.trasladarse(10))
print(anfibio.trasladarse_por_agua(10))

