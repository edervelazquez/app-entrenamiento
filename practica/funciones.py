def calcular_volumen(peso, reps):
    return peso * reps


def estimar_1rm(peso, reps):
    return peso * (1 + reps / 30)


print(f"{calcular_volumen(135, 10):.1f}")
print(f"{estimar_1rm(100, 8):.1f}")
