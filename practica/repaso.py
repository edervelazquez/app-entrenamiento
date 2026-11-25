series = int (input ("Cuantas series se realizaron?: "))
registro = []

for i in range (series):
    reps = int (input (f"Serie {i + 1} REPS: "))
    peso = float (input(f"Serie {i + 1} PESO EN LBS: "))
    
    registro.append ({"reps": reps, "carga": peso})
    
for serie in registro: 
    print (f"{serie ['reps']} REPS X {serie ['carga']} LBS")
    