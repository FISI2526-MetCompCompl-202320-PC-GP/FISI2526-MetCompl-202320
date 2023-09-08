import matplotlib.pyplot as plt

class Mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_fractura, color, composicion, sistema_cristalino, specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_fractura = rompimiento_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def __str__(self):
        return f"Mineral: {self.nombre}\n" \
               f"Dureza: {self.dureza}\n" \
               f"Lustre: {self.lustre}\n" \
               f"Rompimiento por fractura: {self.rompimiento_fractura}\n" \
               f"Color: {self.color}\n" \
               f"Composición: {self.composicion}\n" \
               f"Sistema cristalino: {self.sistema_cristalino}\n" \
               f"Specific Gravity: {self.specific_gravity}"
              
    def es_silicato(self):
        # Verifica si "Si" y "O" están presentes en la composición química
        return "Si" in self.composicion and "O" in self.composicion

    def densidad_si(self):
        # Calcula la densidad en unidades SI (kg/m^3)
        return self.specific_gravity * 1000

    def visualizar_color(self):
        # Visualiza el color del mineral más común usando matplotlib
        plt.figure()
        plt.title(f"Color del Mineral: {self.nombre}")
        plt.imshow([[self.color]])
        plt.axis('off')
        plt.show()

    def imprimir_informacion(self):
        # Imprime la información de dureza, tipo de rompimiento y sistema de organización de átomos
        print(f"Dureza: {self.dureza}")
        print(f"Tipo de Rompimiento: {'Fractura' if self.rompimiento_fractura else 'Escisión'}")
        print(f"Sistema de Organización de Átomos: {self.sistema_cristalino}")



#2.3
def silicatos(listaminerales, self):
    silicatos=[]
    for k in listaminerales:
        mineralcomp=Mineral.init[6]
        if Mineral.es_silicato(self)==True:
            silicatos.append(self.nombre)
    return(silicatos)
