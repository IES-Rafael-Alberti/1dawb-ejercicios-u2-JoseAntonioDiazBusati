"""
Ejercicio 2.1.2

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""

def PedirPassword(password:str):
    contrasena="contraseña"
    if password.replace(" ","").lower()==contrasena:
        return True
    else:
        return False
   
def ComprobarPassword():
    return input("Introduce una contraseña: ")

def main():
    contrasena=ComprobarPassword()
    if PedirPassword(contrasena):
        print("Acertaste mamawebo.")
    else:
        print("Kagaste")

if __name__ == "__main__":
    main()
