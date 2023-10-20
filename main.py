
import os
from Division import division

from multiplicacion import multiplicacion
from resta import resta
from suma import suma


def Menu():
    while True:
        os.system('cls')

        print("Que operacion deseas realizar?\n1) suma\n2) resta\n3) multiplicacion\n4) divicion")
        accion = input("<< ")

        if accion =='':
            os.system('cls')
            print("Programa terminado")
            break;        

        if accion == '1':
            os.system('cls')
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))

            res = suma(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            
            input()
        elif accion =='2':
            os.system('cls')
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))

            res = resta(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            
            input()
        elif accion =='3':
            os.system('cls')
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))

            res = multiplicacion(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            
            input()

        elif accion =='4':
            os.system('cls')
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))

            res = division(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            
            input()
        else:
            os.system('cls')

            print("Opcion no valida")
            input()
            



if __name__ == "__main__":
    Menu()