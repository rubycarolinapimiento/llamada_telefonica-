
# Programa para calcular el costo de una llamada 

#input

dur_llam = int(input("Digite la duración de la llamada:"))

#processing
if dur_llam  <=3:
    print("El costo de la llamada es 300")
else:
     costo = 300 + (dur_llam - 3) * 50

#output

print("el costo de la llamada es: ", costo)