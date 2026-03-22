# app.py

import calculator

def main():
    print("Calculadora")

    while True:
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "5":
            print("Saliendo...")
            break

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Ingresa solo números.")
            continue

        if opcion == "1":
            resultado = calculator.add(num1, num2)
        elif opcion == "2":
            resultado = calculator.subtract(num1, num2)
        elif opcion == "3":
            resultado = calculator.multiply(num1, num2)
        elif opcion == "4":
            resultado = calculator.divide(num1, num2)
        else:
            print("Opción inválida.")
            continue

        print("Resultado:", resultado)


if __name__ == "__main__":
    main()
