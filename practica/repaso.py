series = int (input("Numero de series: "))
registro = []

for i in range (series):
    reps = int (input(f"Serie {i + 1 } numero de reps: "))
    peso = float (input(f" Serie {i + 1} peso en LBS: "))
    
    registro.append ({"reps": reps, "peso": peso})
    
for serie in registro:
    print (f"{serie ['reps']} REPS X {serie ['peso']} LBS")
    
    