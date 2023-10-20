def division(num1:float, num2:float)->float: #Operacion de division en Python
    if(num2==0):#Detectar error al dividir en 0
        return "ERROR EN OPERACION"#Notificar error
    else:
        return num1/num2#Mostrar resultado
    