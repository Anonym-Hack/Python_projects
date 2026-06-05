#Temprature conversion
select=int(input("Select 1 OR 2 To Enter\n1 for Calcius|\n2 for Fahrenheit|\n:----------"))
Temprature=int(input("Enter the Temprature to convert:----"))
if select==1:
    print("Converting to Fahrenheit.......")
    print(f"In Fahrenheit:- {(Temprature*(9/5))+32}F")
elif select==2:
    print("Converting to Celcius.......")
    print(f"In Celcius:- {((5*Temprature)-160)/9}")
else:
    print("Invalid input")