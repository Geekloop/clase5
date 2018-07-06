#Realizar un programa que permita determinar el pago semanal (5d) de un trabajador 
#considerando los siguientes aspectos: 
#las horas trabajadas
#la tarifa por hora
#los descuentos
#Si la cantidad de horas trabajadas es
#mayor a 40 se le debe pagar un bono del 50% adicional
print "Determinando pago semanal"
hor = int(input(("Ingrese horas trabajadas: ")))
tar = int(input(("Ingrese tarifa hora: ")))
desc = int(input(("Ingrese descuentos: ")))

pago = hor * tar
pagot = (pago * 5) - desc

if (hor > 40):
    add = pagot / 2
else:
    add = 0

print "Su bono adicional es de: ",add
print "Su pago semanal total es de: ", pagot + add
    

