#Python calculator
oprator=input("Enter oprator(+ - * /):--")
num1=float(input("Enter number 1:---"))
num2=float(input("Enter number 2:---"))
if oprator=="+":
    print(f"Sum={num1+num2}")
elif oprator=="-":
    print(f"Subtract={num1-num2}")
elif oprator=="*":
    print(f"Multiply={num1*num2}")
elif oprator=="/":
    print(f"Divide={num1/num2}")
else:
    print("!Invalid Oprator")