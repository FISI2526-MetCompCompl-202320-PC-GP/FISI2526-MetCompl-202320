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