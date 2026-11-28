def calcular_volumen(peso, reps):
    return peso * reps


def estimar_rm(peso, reps):
    return peso * (1 + reps / 30)


series = int(input("Numero de series: "))
registro = []

for i in range(series):
    peso = float(input(f"Serie {i + 1} peso en LBS: "))
    reps = int(input(f"Serie {i + 1} Reps: "))

    registro.append({"peso": peso, "reps": reps})

for serie in registro:
    print(f"{serie ['peso']} LBS X {serie ['reps']} REPS")
