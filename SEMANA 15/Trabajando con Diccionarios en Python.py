#Deber Semana #15 Trabajando con Diccionarios en Python
# Paso 1: Crear el diccionario inicial con las claves solicitadas
informacion_personal = {
    "nombre": "John Jara",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Gerente en el Grupo KFC"
}
print("Paso 1 - Diccionario inicial:")
print(informacion_personal)
print("-" * 50)

# Paso 2: Acceder al valor de 'ciudad' y modificarlo
ciudad_anterior = informacion_personal["ciudad"]
informacion_personal["ciudad"] = "Santo Domingo"  # nueva ciudad
print("Paso 2 - Ciudad modificada:")
print("Ciudad anterior:", ciudad_anterior)
print("Ciudad nueva:", informacion_personal["ciudad"])
print("-" * 50)

# Paso 3: Agregar o actualizar la clave 'profesion'
# Si ya existe, la actualizamos; si no, la agregamos.

profesion_anterior = informacion_personal.get("profesion")
informacion_personal["profesion"] = "Tecnico en Celulares y Laptos"
print("Paso 3 - Profesión agregada/actualizada:")
print("Profesión anterior:", profesion_anterior)
print("Profesión nueva:", informacion_personal["profesion"])
print("-" * 50)

# Paso 4: Verificar si 'telefono' existe; si no, agregarla con un número ficticio

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 980090708"
    print("Paso 4 - 'telefono' no existía y se agregó:", informacion_personal["telefono"])
else:
    print("Paso 4 - 'telefono' ya existe:", informacion_personal["telefono"])
print("-" * 50)

# Paso 5: Eliminar la clave 'edad' (si existe)

edad_eliminada = informacion_personal.pop("edad", None)
print("Paso 5 - Se eliminó 'edad' con valor:", edad_eliminada)
print("-" * 50)

# Paso 6: Imprimir diccionario final con todos los cambios

print("Paso 6 - Diccionario final:")
print(informacion_personal)
