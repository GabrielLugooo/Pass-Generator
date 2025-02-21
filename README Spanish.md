<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# GENERADOR DE CONTRASEÑAS

<a href="https://github.com/GabrielLugooo/Pass-Generator/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Generador%20Contraseñas%20Español-000000" alt="Generador Español" /></a>
<a href="https://github.com/GabrielLugooo/Pass-Generator" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Generador%20Contraseñas%20Inglés-green" alt="Generador Inglés" /></a>

### Objetivos

Este proyecto, Pass-Generator, es un generador de contraseñas basado en Python diseñado para crear claves seguras y robustas con parámetros personalizables.

Permite a los usuarios definir la longitud de la contraseña y los tipos de caracteres, garantizando un equilibrio entre seguridad y facilidad de uso.

Esta herramienta es especialmente útil para mejorar la seguridad en línea al generar contraseñas complejas y difíciles de descifrar.

### Habilidades Aprendidas

- Programación en Python y uso de bibliotecas de aleatorización.
- Manejo eficiente de la entrada del usuario y opciones de personalización.
- Comprensión de buenas prácticas en ciberseguridad, especialmente en la fortaleza de contraseñas y principios de cifrado.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

### Proyecto

#### Explicación Paso a Paso

1. **Importar las Bibliotecas Necesarias** – El script utiliza las bibliotecas `string` y `random` para generar contraseñas seguras con diferentes caracteres.
2. **Validación de Entrada del Usuario** – El programa se asegura de que el usuario ingrese un número válido para la longitud de la contraseña.
3. **Definir los Caracteres Disponibles** – El script combina letras mayúsculas, minúsculas, números y caracteres especiales.
4. **Generar la Contraseña** – Utilizando un bucle, el programa selecciona aleatoriamente caracteres del conjunto disponible y los concatena para crear la contraseña final.
5. **Mostrar la Contraseña Generada** – Se imprime la contraseña para el usuario.

#### Código con Comentarios (Español)

```python
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
```

### Limitaciones

El Generador de Contraseñas es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="Last Edited" /></a>
