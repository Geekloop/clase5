#Escribir un programa que permita calcular la suma, la resta, el producto
#la division de dos numeros dados por el usuario e imprima el resultado.
#Tomando en cuenta cada caso, si el resultado es 
#menor que 20 es AZUL
#menor que 40 es ROJO
#menor que 60 es NEGRO.

def sum():
    print "Resutado Suma"
    suma = a + b
    if (suma > 0 and suma < 20):
        print "Azul"
    elif (suma >= 20 and suma < 40): 
        print "Rojo"
    elif (suma >= 40 and suma < 60):
        print "Negro"
    else:
        print "No Color"   
    return suma

def res():
    print "Resultado resta"
    resta = a - b
    if (resta > 0 and resta < 20):
        print "Azul"
    elif (resta >= 20 and resta < 40): 
        print "Rojo"
    elif (resta >= 40 and resta < 60):
        print "Negro"
    else:
        print "No Color" 
    return resta

def prod():
    print "Resultado Producto"
    produ = a * b
    if (produ > 0 and produ < 20):
        print "Azul"
    elif (produ >= 20 and produ < 40): 
        print "Rojo"
    elif (produ >= 40 and produ < 60):
        print "Negro"
    else:
        print "No Color" 
    return produ

def div():
    print "Resultado Division"
    divi = a / b
    if (divi > 0 and divi < 20):
        print "Azul"
    elif (divi >= 20 and divi < 40): 
        print "Rojo"
    elif (divi >= 40 and divi < 60):
        print "Negro"
    else:
        print "No Color" 
    return divi

a = int(input(("ingrese un numero: ")))
b = int(input(("ingrese un numero: ")))
print sum()
print res()
print prod()
print div()