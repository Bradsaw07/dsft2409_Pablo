def mostrar_menu():
    print("Calculadora Avanzada")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                raise ValueError
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")

def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error al ingresar números. Por favor, ingrese números válidos.")