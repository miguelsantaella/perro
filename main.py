from perro import Perro
def main():
    perro1 = Perro("Max", "Labrador", "Marrón")
    perro2 = Perro("Luna", "Bulldog", "Blanco")
    perro3 = Perro("Rocky", "Pastor Alemán", "Negro")
    perro4 = Perro("Bella", "Poodle", "Gris")

    print(perro1._nombre, perro1._raza, perro1._color)
    print(perro2._nombre, perro2._raza, perro2._color)
    print(perro3._nombre, perro3._raza, perro3._color)
    print(perro4._nombre, perro4._raza, perro4._color)

if __name__ == "__main__":
    main()