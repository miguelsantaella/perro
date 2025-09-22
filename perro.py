class Perro:
    def __init__(self, nombre: str, raza: str, color: str):
        self._nombre = nombre
        self._raza = raza
        self._color = color

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_raza(self) -> str:
        return self._raza

    def get_color(self) -> str:
        return self._color

    # Setters
    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_raza(self, raza: str):
        self._raza = raza

    def set_color(self, color: str):
        self._color = color

    # Comportamientos
    def menear(self) -> str:
        return f"{self._nombre} está meneando la cola."

    def ladrar(self) -> str:
        return f"{self._nombre} está ladrando."

    def comer(self) -> str:
        return f"{self._nombre} está comiendo."

    def __str__(self) -> str:
        return f"Perro(nombre={self._nombre}, raza={self._raza}, color={self._color})"
