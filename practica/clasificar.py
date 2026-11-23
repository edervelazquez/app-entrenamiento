while True:
    ejercicio = input("\nNombre del ejercicio (o 'fin' para salir): ")
    if ejercicio.lower() == "fin":
        print("Sesión terminada")
        break

    carga = float(input("Peso en lbs: "))
    reps = int(input("Repeticiones: "))

    if reps <= 0:
        print("Repeticiones inválidas")
    elif reps <= 5:
        print("Rango de fuerza")
    elif reps <= 12:
        print("Rango de hipertrofia")
    else:
        print("Rango de resistencia")

    if 1 <= reps <= 10:
        rm = carga * (1 + reps / 30)
        print(f"1RM estimado: {rm:.1f} lbs")
    elif reps > 10:
        print("1RM no confiable con tantas repeticiones")
    

    
 

