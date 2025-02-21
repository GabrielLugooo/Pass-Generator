# Importación de librerias necesarias
import string
import random

# Preguntamos al usuario por la longitud de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña: "))

# Queremos tener a disposición números y letras y signos de puntuación
# Utilizamos la libreria string
caracteres = string.ascii_letters + string.digits + string.punctuation

# Usar método join para concatenar caractéres
# El método choice se encarga de elegir dentro de la variable caractéres alguno de los dígitos aleatoriamente
# Creamos un bucle for para que se repita la cantidad de veces igual a el tamaño que seleccionó el usuario
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

# Imprimimos el resultado
print("la contraseña generada es: " + contrasena)