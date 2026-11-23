series = int (input("Cuantas series se realizo: "))

volumen_total= 0
carga_maxima= 0 

for i in range (series): 
    reps= int (input("Numero de reps: "))
    peso = float (input("Cuanto peso en lbs: "))
    
    volumen_total += reps * peso 
    
    if peso > carga_maxima: 
        carga_maxima = peso 

print (f"El volumen total es de: {volumen_total} lbs")
print (f"el peso maximo fue de: {carga_maxima} lbs")
