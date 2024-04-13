 import math
def line():  
    A=float(input("Ingrese el coeficiente A: "))
    B=float(input("Ingrese el coeficiente B: "))
    X1=float(input("Ingrese el coeficiente X1: "))
    X2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}\n")
    print(f"Para la siguiente ecuación: \n \t Y= {A}X + {B}\n")
    print(f"Dados los siguientes puntos:\n")
    Y1 = A*X1 +B
    Y2 = A*X2 +B
    print(f"\t P1 ({X1}, {Y1})")
    print(f"\t P2 ({X2}, {Y2} \n)")

    eqn=math.sqrt(math.pow(X1-X2,2)+math.pow(Y1-Y2,2))
    print(f"La distancia entre ellos: {eqn}")
    
