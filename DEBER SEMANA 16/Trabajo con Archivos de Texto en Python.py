# ---------------------------------------------------------
# Tarea: Trabajo con Archivos de Texto en Python
# Descripción:
# Crea un archivo llamado my_notes.txt,
# escribe tres líneas de notas personales en él,
# luego lo abre y lee su contenido línea por línea.
# ---------------------------------------------------------

# --- Escritura del archivo de texto ---
# Se crea o sobrescribe el archivo "my_notes.txt" y se escriben 3 líneas en él.
archivo = open("my_notes.txt", "w", encoding="utf-8")

# Escribir tres líneas de notas personales

archivo.write("Nota 1: Estudiar y practicar tema de archivos en Python.\n")
archivo.write("Nota 2: Practicar lectura y escritura de texto.\n")
archivo.write("Nota 3: El repositorio de GitHub, me enseña a respaldar mis texto en programacion. \n")

# Cerrar el archivo después de escribir

archivo.close()
print("✅ Archivo 'my_notes.txt' creado y escrito correctamente.\n")

# --- Lectura del archivo de texto ---
# Se abre el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r", encoding="utf-8")

print("📖 Contenido del archivo leído línea por línea:\n")

# Leer cada línea del archivo una por una

linea = archivo.readline()
contador = 1

while linea != "":
    print(f"Línea {contador}: {linea.strip()}")
    contador += 1
    linea = archivo.readline()

# Cerrar el archivo después de leer

archivo.close()
print("\n✅ Archivo cerrado correctamente.")
