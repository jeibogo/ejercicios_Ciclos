altitudes_fincas = [1350, 1750, 1900, 2300, 1600, 2100]

conteo_especial = 0
conteo_tradicional = 0

fincas_especiales = []
fincas_tradicionales = []

for altitud in altitudes_fincas:

    if altitud >= 1700 and altitud <= 2200:

        fincas_especiales.append(altitud)
        conteo_especial += 1

    else:
        fincas_tradicionales.append(altitud)
        conteo_tradicional += 1

print(f"Fincas aptas para café de especialeidad: {conteo_especial} con valores {fincas_especiales} \nFincas tradicionales: {conteo_tradicional} con valores: {fincas_tradicionales} ")
