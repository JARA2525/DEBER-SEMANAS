import numpy as np

# Ciodades a elegidas
ciudades = ["Santo Domingo", "Quito", "Latacunga"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2"]

# Matriz 3D con temperaturas aleatorias entre 15 y 30 grados
# Dimensiones: [ciudades][días][semanas] => (3, 7, 2)
temperaturas = np.random.randint(15, 31, size=(len(ciudades), len(dias), len(semanas)))

# Temperaturas por ciudad, semana y día
print("=== TEMPERATURAS REGISTRADAS ===")
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana_idx, semana in enumerate(semanas):
        print(f"  {semana}:")
        for dia_idx, dia in enumerate(dias):
            temp = temperaturas[ciudad_idx][dia_idx][semana_idx]
            print(f"    {dia}: {temp}°C")

# Calcular y mostrar promedios
print("\n=== PROMEDIOS SEMANALES POR CIUDAD ===")
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for semana_idx, semana in enumerate(semanas):
        suma = 0
        for dia_idx in range(len(dias)):
            suma += temperaturas[ciudad_idx][dia_idx][semana_idx]
        promedio = suma / len(dias)
        print(f"  {semana}: {promedio:.2f}°C")


