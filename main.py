from functools import cache
import os
from Division import division
from multiplicacion import multiplicacion
from resta import resta
from suma import suma

def Pedirdatos() :
    try:
        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))

        return (num1, num2)
    except ValueError:
        raise Exception("formato de entrada no valido\nIngresa datos numericos")


def Menu():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema

            print("Qué operación deseas realizar?\n1) suma\n2) resta\n3) multiplicación\n4) división")
            
            accion = input("<< ")
            

            if accion == '':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa terminado")
                break

            if accion == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                num1,num2=Pedirdatos()

                res = suma(num1=num1,num2=num2)
                print(f"El resultado es: {res}")            
                input()

            elif accion =='2':
                os.system('cls' if os.name == 'nt' else 'clear')
                num1,num2=Pedirdatos()

                res = resta(num1=num1,num2=num2)
                print(f"El resultado es: {res}")            
                input()

            elif accion =='3':
                os.system('cls' if os.name == 'nt' else 'clear')
                num1,num2=Pedirdatos()

                res = multiplicacion(num1=num1,num2=num2)
                print(f"El resultado es: {res}")            
                input()

            elif accion =='4':
                os.system('cls' if os.name == 'nt' else 'clear')
                num1,num2=Pedirdatos()

                res = division(num1=num1,num2=num2)
                print(f"El resultado es: {res}")            
                input()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')

                print("Opcion no valida")
                ()
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"Error: {e}")
            input()

        


if __name__ == "__main__":
    Menu()
