"""
Ejercicio 2.1.3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

"""
def PedirDividendo():
    dividendo=int(input("Introduce un numero: "))
    return dividendo

def PedirDivisor():
    divisor=int(input("Introduce un numero para dividirlo entre el anterior: "))
    return divisor

def main():
    dividendo=PedirDividendo()
    divisor=PedirDivisor()
    if PedirDivisor(0):
        print("Error, no puede ser 0 el divisor")
    else:
        print(dividendo/divisor)

if __name__ == "__main__":
    main()