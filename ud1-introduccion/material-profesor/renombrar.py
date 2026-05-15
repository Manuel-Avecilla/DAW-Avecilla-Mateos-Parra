import os
import re
import unicodedata

def aplicar_reglas_profesor(nombre_archivo):
    # Separamos el nombre de la extensión (ej: .pdf, .docx)
    nombre, extension = os.path.splitext(nombre_archivo)
    
    # 1. Quitamos las tildes y caracteres extraños
    nombre = ''.join(c for c in unicodedata.normalize('NFD', nombre) 
                     if unicodedata.category(c) != 'Mn')
    
    # 2. Pasamos todo a minúsculas
    nombre = nombre.lower()
    
    # 3. Sustituimos cualquier cosa que no sea una letra o número por un guion medio
    nombre = re.sub(r'[^a-z0-9]+', '-', nombre)
    
    # 4. Limpiamos guiones sueltos al principio o al final
    nombre = nombre.strip('-')
    
    # Volvemos a pegar la extensión original
    return nombre + extension

# --- Caso Práctico de Ejecución ---
carpeta_actual = '.'

for archivo in os.listdir(carpeta_actual):
    # Solo procesamos archivos (ignoramos carpetas y al propio script)
    if os.path.isfile(archivo) and archivo != 'renombrar.py':
        nuevo_nombre = aplicar_reglas_profesor(archivo)
        
        # Renombramos el archivo físicamente
        os.rename(archivo, nuevo_nombre)
        print(f"✅ Renombrado: '{archivo}' -> '{nuevo_nombre}'")
