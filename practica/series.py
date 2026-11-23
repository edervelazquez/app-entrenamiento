series = int(input("¿Cuántas series realizaste?: "))

volumen_total = 0
total_reps = 0
carga_maxima = 0
mayor_volumen_serie = 0
mejor_1rm = 0

for i in range(series):
    peso = float(input(f"Serie {i + 1} - peso (lbs): "))
    reps = int(input(f"Serie {i + 1} - reps: "))

    volumen_serie = peso * reps
    volumen_total += volumen_serie
    total_reps += reps

    if peso > carga_maxima:
        carga_maxima = peso

    if volumen_serie > mayor_volumen_serie:
        mayor_volumen_serie = volumen_serie

    if reps <= 10:
        rm = peso * (1 + reps / 30)
        if rm > mejor_1rm:
            mejor_1rm = rm

promedio_reps = total_reps / series

print(f"\nVolumen total: {volumen_total:.0f} lbs")
print(f"Carga máxima: {carga_maxima:g} lbs")
print(f"Serie con más volumen: {mayor_volumen_serie:.0f} lbs")
print(f"Promedio de reps: {promedio_reps:.1f}")
if mejor_1rm > 0:
    print(f"Mejor serie (1RM est.): {mejor_1rm:.1f} lbs")
    
    
    




