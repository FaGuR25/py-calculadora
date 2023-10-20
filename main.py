
import os

from multiplicacion import multiplicacion
from resta import resta
from suma import suma


def Menu():
    while True:
        print("Que operacion deseas realizar?\n1) suma\n2) resta\n3) multiplicacion\n4) divicion")
        accion = input("<< ")

        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))

        if accion == '1':
            os.system('cls')
            suma(num1=num1,num2=num2)
        elif accion =='2':
            os.system('cls')
            resta(num1=num1,num2=num2)
        elif accion =='3':
            os.system('cls')
            multiplicacion(num1=num1,num2=num2)

        elif accion =='4':
            os.system('cls')

        else:
            os.system('cls')
            print("Programa terminado")
            break;


if __name__ == "__main__":
    pass