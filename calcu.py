def sumarNum(num1, num2):
    return num1 + num2

def restarNum(num1, num2):
    return num1 - num2

def multiplicarNum(num1, num2):
    return num1 * num2

def dividirNum(num1, num2):
    return num1 / num2

def menu_calcu():
    print ("1. SUMAR")
    print ("2. RESTAR")
    print ("3. MULTIPLICAR")
    print ("1. DIVIDIR")
    opcion = input("--> ")
    return opcion


num1 = float(input("Ingresa un numero: "))
while True:
    opc = menu_calcu()
    num2 = float(input("Ingresa un numero: "))
    if opc == "1":
        ress = sumarNum(num1,num2)
    elif opc == "2":
        ress = restarNum(num1,num2)
    elif opc == "3":
        ress = multiplicarNum(num1,num2)
    elif opc == "4":
        ress = dividirNum(num1,numnum2)

    print ("===============================")
    print("El resultado es : ", ress)
    num1 = ress
    nueva_Operacion = input("¿Desea realizar otra operación? (s/n): ")
    if nueva_Operacion == "n":
        break
    

    