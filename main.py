import os
from Division import division
from multiplicacion import multiplicacion
from resta import resta
from suma import suma

def Menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema

        print("Qué operación deseas realizar?\n1) suma\n2) resta\n3) multiplicación\n4) división")
        
        try:
            accion = input()
        except EOFError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa terminado")
            break

        if accion == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa terminado")
            break

        # Resto del código como antes
        # ...

if __name__ == "__main__":
    Menu()
