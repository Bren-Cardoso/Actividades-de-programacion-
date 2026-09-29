num1 = int(input("ingresa un num"))
ope = input("Elige una operacion (+, -, * or /)")
num2 = int(input("ingresa el otro num"))

if ope == "+":
    print(num1 + num2)
elif ope == "-":
    print(num1 - num2)
elif ope == "*":
    print(num1 * num2)
elif ope == "/":
    print(num1 / num2)
else:
    pass
