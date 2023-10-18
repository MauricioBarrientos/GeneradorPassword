import random
import string

print("Bienvenido al generador de contraseñas.")
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = int(input("Ingrese la longitud deseada para la contraseña: "))
contrasena_generada = generar_contrasena(longitud_contrasena)
print("Contraseña generada:", contrasena_generada)