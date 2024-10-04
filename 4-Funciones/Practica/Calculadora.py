from menu import mostrar_menu, obtener_opcion, obtener_numeros
from operaciones import suma, resta, multiplicacion, division
from excepciones import ErrorOpcionInvalida, ErrorDivisionPorCero, ErrorOperacionInvalida

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        if opcion == 5:
            break
        num1, num2 = obtener_numeros()
        try:
            if opcion == 1:
                print(f"La suma es: {suma(num1, num2)}")
            elif opcion == 2:
                print(f"La resta es: {resta(num1, num2)}")
            elif opcion == 3:
                print(f"La multiplicación es: {multiplicacion(num1, num2)}")
            elif opcion == 4:
                print(f"La división es: {division(num1, num2)}")
            else:
                raise ErrorOperacionInvalida("Opción inválida")
        except ErrorDivisionPorCero as e:
            print(e)
        except ErrorOperacionInvalida as e:
            print(e)

if __name__ == "__main__":
    main()
