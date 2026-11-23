series = int (input("Cuantas series se realizo: "))
registro = []
volumen_total = 0 

for i in range (series): 
    reps= int (input(f"Serie {i + 1} - reps "))
    peso = float (input(f"Serie {i + 1} - peso"))
    
    registro.append ({"reps": reps, "peso": peso})
    
    volumen_total += reps * peso 

for i, serie in enumerate(registro, start=1):
    volumen_serie = serie["reps"] * serie["peso"]
    print (f"Serie {i}: {serie['reps']} reps X {serie['peso']} lbs = {volumen_serie} lbs ")

print (f"El volumen total es de: {volumen_total} lbs") 
        
    
