def leap_year():
    año =int(input("Ingrese un año: "))
    bisiesto= (año%4==0)
    if(bisiesto and not año%100==0) or (año%400==0):
    print(f"El {año} es bisiesto")
    else:
    print(f"El {año} no es bisiesto")

