import pytest

class Calculadora:
    def __init__(self):
        pass
def setup():
    print("SETUP")
def test_suma(self, num_a, num_b):
        return num_a + num_b

def test_resta(self, num_a, num_b):
        return num_a - num_b

def test_multiplicacion(self, num_a, num_b):
        return num_a * num_b

def test_division(self, num_a, num_b):
        if b == 0:
            return "Error: no se puede dividir entre cero"
        else:
            return num_a / num_b
def teardown():
    print(teardown)

def ejecutar_operacion(self, operacion, num1, num2):
        if operacion == "+":
            resultado = self.suma("num_a", "num_b")
   elif operacion == "-":
            resultado = self.resta("num_a", "num_b")
   elif operacion == "*":
            resultado = self.multiplicacion("num_a", "num_b")
   elif operacion == "/":
            resultado = self.division("num_a", "num_b")
   else:
            resultado = "Error: operación no válida"

        return resultado


# Crear una instancia de la clase "Calculadora"
mi_calculadora = Calculadora()

# Crear casos de prueba usando la sentencia assert
 assert mi_calculadora.ejecutar_operacion("+", 2, 2) == 4
 assert mi_calculadora.ejecutar_operacion("-", 5, 3) == 2
 assert mi_calculadora.ejecutar_operacion("*", 3, 4) == 12
 assert mi_calculadora.ejecutar_operacion("/", 10, 2) == 5
 assert mi_calculadora.ejecutar_operacion("/", 10, 0) == "Error: no se puede dividir entre cero"
