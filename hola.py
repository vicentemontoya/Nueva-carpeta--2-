num1 = int(input("agrega un nunero entero: "))
num2 = int(input("agrega un numero entero: "))
operador = input("operadores (+, -, *, /):  ")

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("ERROR: no se puede dividir por cero")
    else:
        print( "resultado", num1 / num2)
else:
    print("operador no valido")