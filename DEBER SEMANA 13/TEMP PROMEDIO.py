import numpy as np

# =======================================
# 1. Datos base
# =======================================
# Listas de ciudades, días y semanas
ciudades = ["Santo Domingo", "Quito", "Latacunga"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

# Crear matriz 3D de temperaturas aleatorias
# Dimensiones: [ciudad][día][semana]
# np.random.randint(15, 31) genera números aleatorios entre 15°C y 30°C
temperaturas = np.random.randint(15, 31, size=(len(ciudades), len(dias), len(semanas)))


# =======================================
# 2. Función para calcular promedios
# =======================================
def calcular_promedio_temperatura(temperaturas, ciudades, dias, semanas):
    """
    Calcula el promedio de temperaturas para cada ciudad en todas las semanas.

    Parámetros:
        temperaturas: np.ndarray
            Matriz 3D de temperaturas [ciudad][día][semana]
        ciudades: list
            Lista de nombres de ciudades
        dias: list
            Lista de días de la semana
        semanas: list
            Lista de semanas

    Retorna:
        dict: Diccionario con el promedio de temperaturas por ciudad.
    """
    promedios = {}
    for ciudad_idx, ciudad in enumerate(ciudades):
        # Extraer todas las temperaturas de esa ciudad
        temps_ciudad = temperaturas[ciudad_idx, :, :]
        # Calcular promedio de toda la matriz de esa ciudad
        promedio = np.mean(temps_ciudad)
        promedios[ciudad] = promedio
    return promedios


# =======================================
# 3. Pruebas de la función
# =======================================
# Mostrar temperaturas para comprobar visualmente
print("=== TEMPERATURAS REGISTRADAS ===")
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana_idx, semana in enumerate(semanas):
        print(f"  {semana}:")
        for dia_idx, dia in enumerate(dias):
            print(f"    {dia}: {temperaturas[ciudad_idx][dia_idx][semana_idx]}°C")

# Calcular y mostrar promedios
print("\n=== PROMEDIOS DE TEMPERATURA POR CIUDAD ===")
promedios = calcular_promedio_temperatura(temperaturas, ciudades, dias, semanas)
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")
