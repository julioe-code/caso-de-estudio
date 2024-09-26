# Definimos una clase abstracta "Vehiculo" con métodos especiales
from abc import ABC, abstractmethod
#cosa

#unir dos ramas
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def velocidad_maxima(self):
        pass

# Creamos una clase concreta "Coche" que hereda de "Vehiculo"
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas, cilindrada):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Coche {self.marca} {self.modelo} del {self.año} con {self.num_puertas} puertas y {self.cilindrada} cc"

    def velocidad_maxima(self):
        return 180  # km/h

# Creamos otra clase concreta "Moto" que hereda de "Vehiculo"
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Moto {self.marca} {self.modelo} del {self.año} con {self.cilindrada} cc"

    def velocidad_maxima(self):
        return 120  # km/h

# Creamos objetos de las clases concretas
coche = Coche("Ford", "Focus", 2015, 5, 1600)
moto = Moto("Honda", "CBR", 2018, 600)

# Mostramos la descripción y velocidad máxima de cada vehículo
print(coche.descripcion())
print(f"Velocidad máxima: {coche.velocidad_maxima()} km/h")
print(moto.descripcion())
print(f"Velocidad máxima: {moto.velocidad_maxima()} km/h")
