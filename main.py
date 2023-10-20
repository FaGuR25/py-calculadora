
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

        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))

        if accion == '1':
            os.system('cls')
            res = suma(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            input()
        elif accion =='2':
            os.system('cls')
            res = resta(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            input()
        elif accion =='3':
            os.system('cls')
            res = multiplicacion(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            input()

        elif accion =='4':
            os.system('cls')
            res = division(num1=num1,num2=num2)
            print(f"El resultado es: {res}")
            input()

        else:
            os.system('cls')
            print("Programa terminado")
            break;


if __name__ == "__main__":
    Menu()