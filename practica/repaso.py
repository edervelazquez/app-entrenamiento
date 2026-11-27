series = int(input("Numero de series: "))

registro = []

for i in range(series):
    reps = int(input(f"Serie {i + 1} Reps:  "))
    carga = float(input(f"Serie {i + 1} Peso: "))

    registro.append({"reps": reps, "carga": carga})

for serie in registro:
    print(f"{serie ['reps']} REPS X {serie ['carga']} LBS")
