
# Pass-Generator
# Importación de librerías necesarias
import string
import random

def generar_contrasena():
    """Función para generar una contraseña segura según la longitud definida por el usuario."""
    try:
        # Pedir al usuario la longitud de la contraseña
        longitud = int(input("Ingrese el tamaño de la contraseña: "))
        
        # Asegurar que la longitud de la contraseña sea al menos de 4 caracteres
        if longitud < 4:
            print("La longitud de la contraseña debe ser de al menos 4 caracteres por seguridad.")
            return
        
        # Definir caracteres disponibles: letras, números y signos de puntuación
        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        # Generar la contraseña utilizando elecciones aleatorias y el método join
        contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
        
        # Imprimir la contraseña generada
        print("La contraseña generada es: " + contrasena)
    except ValueError:
        print("¡Entrada no válida! Por favor, ingrese un valor numérico.")

# Ejecutar la función
generar_contrasena()