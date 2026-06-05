#Python weight converter
select=int(input("Enter to select|\nInput (1) " \
"to convert lbs-->kg|\nInput (2) to convert kg-->lbs|\n:------------- "))

weight=int(input("Enter the Weight:-"))

if select==1:
    print(f"In Kilograms={int(weight/2.20)} kg")
elif select==2:
    print(f"In Pounds={int(weight*2.20)} lbs")
else:
    print(f"{select} is invalid oprator.")