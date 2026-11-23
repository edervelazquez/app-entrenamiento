ejercicio = (input("Nombre del ejercicio: "))
carga =  float(input ("Peso en lbs: "))
reps = int(input ("Repeticiones: ")) 
series =int (input("Series: "))

volumen= carga * reps 
volumen_total= volumen * series
rm = carga * (1 + reps / 30)

print (f"{ejercicio}: {carga} lbs x {reps} = {volumen:.0f} lbs de volumen") 
print (f"El volumen total del Ejercicio fue de: {volumen_total}") 
print (f"Tu 1RM estimado es de {rm:.0f}")

