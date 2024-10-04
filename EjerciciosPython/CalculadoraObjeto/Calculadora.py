class CalculadoraAvanzada:
    def __init__(self):
        self.historial = []

    def suma(self, a, b):
        try:
            resultado = a + b
            self.historial.append(f"Suma: {a} + {b} = {resultado}")
            return resultado
        except TypeError:
            return "Error: Los operandos deben ser números"

    def resta(self, a, b):
        try:
            resultado = a - b
            self.historial.append(f"Resta: {a} - {b} = {resultado}")
            return resultado
        except TypeError:
            return "Error: Los operandos deben ser números"

    def multiplicacion(self, a, b):
        try:
            resultado = a * b
            self.historial.append(f"Multiplicación: {a} * {b} = {resultado}")
            return resultado
        except TypeError:
            return "Error: Los operandos deben ser números"

    def division(self, a, b):
        try:
            if b == 0:
                return "Error: No se puede dividir por cero"
            resultado = a / b
            self.historial.append(f"División: {a} / {b} = {resultado}")
            return resultado
        except TypeError:
            return "Error: Los operandos deben ser números"

    def potencia(self, a, b):
        try:
            resultado = a ** b
            self.historial.append(f"Potencia: {a} ^ {b} = {resultado}")
            return resultado
        except TypeError:
            return "Error: Los operandos deben ser números"
    def raiz_cuadrada(self, a):
        try:
            if a < 0:
                return "Error: No se puede calcular la raíz cuadrada de un número negativo"
            resultado = a ** 0.5
            
            self.historial.append(f"Raíz cuadrada: √{a} = {resultado}")
            return resultado
        except TypeError:
            return "Error: El operando debe ser un número"

    def mostrar_historial(self):
        return self.historial

calculadora = CalculadoraAvanzada()

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Mostrar historial")
    print("8. Salir")

    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(calculadora.suma(a, b))
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(calculadora.resta(a, b))
    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(calculadora.multiplicacion(a, b))
    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(calculadora.division(a, b))
    elif opcion == "5":
        a = float(input("Ingrese la base: "))
        b = float(input("Ingrese el exponente: "))
        print(calculadora.potencia(a, b))
    elif opcion == "6":
        a = float(input("Ingrese el número: "))
        print(calculadora.raiz_cuadrada(a))
    elif opcion == "7":
        print(calculadora.mostrar_historial())
    elif opcion == "8":
        break
    else:
        print("Opción inválida")