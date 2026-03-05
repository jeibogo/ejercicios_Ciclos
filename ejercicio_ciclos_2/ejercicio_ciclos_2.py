import random

nivel_alerta = 8.5

max_lecturas = 12
lectura_actual = 0

alerta_inundacion = False

while lectura_actual < max_lecturas:
    medicion = random.uniform(5.0, 9.0)
    print(medicion)
    lectura_actual += 1
    if medicion >= nivel_alerta:
        alerta_inundacion = True
        print("¡ALERTA ROJA!")
        break
if alerta_inundacion == False:
    print("Monitoreo finalizado. Niveles estables.")
