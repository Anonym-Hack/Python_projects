#Temprature conversion
select=int(input("Select 1 OR 2 To Enter\n1 to convert in Fahrenheit|\n2 to convert in Celcius|\n:----------"))
Temprature=int(input("Enter the Temprature to convert:----"))
if select==1:
    print("Converting to Fahrenheit.......")
    print(f"In Fahrenheit:- {round((Temprature*(9/5))+32,1)}°F")
elif select==2:
    print("Converting to Celcius.......")
    print(f"In Celcius:- {round(((5*Temprature)-160)/9,1)}°C")
else:
    print("Invalid input")