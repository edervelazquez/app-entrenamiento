#Bitacora 
## 22 nov 2026
- Aprendí: Que python va de dentro hacia fuera, tambien recorde que las variables se escriben en snake_case, recorde f-string, como almacenar una variable para que el usuario introduzca la informacion y colocar el tipo de dato que tiene que convertir (float, int, string).

tambien aprendi a usar FOR es un ciclo que nos permite iterar en cada elemento de una lista, tambien mire condicionales: if, elif y else. 
con el ciclo while nos permite crear un ciclo siempre y cuando la condicion del ciclo se cumpla. 

- Me trabé en: el espacio entre f y las comillas, no recordaba en donde iba el tipo de dato. 
tambien me costo entender el ciclo for pero una vez haciendo ejercicios pude entenderlo mejor 

## 23 nov 2026
- listas y diccionarios: registro.append({...})
- Dentro del ciclo, leer de serie, no de variables viejas, cuando se termina un ciclo y abrimos otro debo de especificar de que parte de la lista estoy tomando. 
- En f-strings: {serie['clave']} 

## 24 nov 2026 (martes)
- Horario: 17:32–18:16 / 21:58–22:31
- Minutos efectivos: ~75
- Tema: repaso de listas y diccionarios

### De memoria
- Estructura de 4 pasos (cuántas series → lista vacía → llenar → recorrer): salió en orden
- `for i in range(series)`: al principio puse `for i in series` y `for i in lista`
- `append({...})`: necesité ver un ejemplo (Gemini)
- Ciclo 2: confundí `series` con `registro`, y no recordé `{serie['clave']}` en el print

### Errores que se repiten
- Usar variables viejas o equivocadas en el ciclo 2 en lugar de `serie[...]`
- Estilo: `int (`, `print (`, espacio en `serie ['reps']`

### Reglas para recordar
- Repetir N veces = `range(N)`
- `append(lo que guardo)`
- `range` → llenar · lista → recorrer
- Dentro del ciclo 2, todo sale de `serie`
- En f-strings: `{serie['clave']}`

### Otros
- Decisiones: crear DECISIONES.md (unidad única, 1RM ≤10 reps, 3 métricas de "mejor serie")
- Cafeína a las 5:30 pm afectó el sueño → regla: nada de cafeína después de la 1–2 pm

### Mañana
- Repaso de listas completo de memoria (sin ayuda)
- Si sale limpio → funciones

## 25 nov 2026 (miércoles)
- Horario: 14:05–14:41
- Minutos efectivos: ~35
- Tema: repaso de listas

### De memoria
- Primer intento: estructura de 4 pasos y `range(series)` bien; ciclo 2 recorre `registro` (ayer lo confundí con `series`)
- Fallaron igual que ayer: `append` (puse corchetes) y el `print` con `serie['...']` (además, sin indentar)
- Después de micro-práctica (solo esas 2 líneas, 3 rondas): el programa completo salió limpio

### Reglas para recordar
- Las acciones llevan paréntesis: `print()`, `input()`, `len()`, `append()`
- Corchetes: crear lista `[]` o sacar un dato `serie['reps']`
- Después de `:`

## 26 nov 2026 (jueves)
- Horario: 20:00–20:36
- Minutos efectivos: ~35
- Tema: repaso de listas en frío + Black + introducción a funciones

### De memoria (24 h sin verlo)
- append({...}) con paréntesis: ✅ consolidado
- Ciclo 2 recorre registro e indentado: ✅
- print: puse {serie: ['reps']} → el ":" en f-string es formato → ValueError

### Funciones (nuevo)
- def nombre(parámetros): ... return resultado
- Sin return, la función regresa None (calcula pero no entrega)
- Los argumentos se asignan por posición: si cambio el orden, no truena pero da mal
- Redondear al MOSTRAR, no dentro de la función

### Decisiones de diseño
- En todo el proyecto, siempre (peso, reps)

### Reglas para recordar
- En f-strings, ":" solo para formato ({rm:.1f}, {vol:.0f})
- Dato de diccionario: {serie['reps']} pegado

### Otros
- Black configurado: formatea al guardar (no toca el interior de las f-strings)

### Mañana (vie 2–3 pm)
- Repaso en frío: programa de listas + las 2 funciones
- Parte 2: usar calcular_volumen dentro del ciclo de listas