series = int (input ("Cuantas series se realizaron?: "))
registro = []

for i in range (series):
    reps = int (input(f"Serie {i + 1} reps: "))
    peso = float (input(f"Serie {i + 1} Peso en lbs: "))
    
    registro.append ({"reps": reps , "peso": peso})
    
for serie in registro:
    print (f"{serie ['reps']} REPS X {serie ['peso']} LBS")
    
    
