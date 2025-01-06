import random
import string

def generar_password(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debes incluir al menos un tipo de carácter para generar la contraseña.")

    return ''.join(random.choices(caracteres, k=longitud))

# Ejemplo de uso
if __name__ == "__main__":
    try:
        longitud = int(input("Ingresa la longitud del password: "))
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número positivo.")

        incluir_mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
        incluir_minusculas = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
        incluir_numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
        incluir_simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'

        password = generar_password(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
        print("Tu password generado es:", password)

    except ValueError as e:
        print("Error:", e)
