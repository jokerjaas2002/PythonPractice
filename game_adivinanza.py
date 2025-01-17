import random

def juego_adivinanzas():
    while True:
        # Elegir el nivel de dificultad
        nivel = input("Elige un nivel de dificultad (facil, medio, dificil): ").lower()
        if nivel == 'facil':
            numero_secreto = random.randint(1, 10)
        elif nivel == 'medio':
            numero_secreto = random.randint(1, 50)
        elif nivel == 'dificil':
            numero_secreto = random.randint(1, 100)
        else:
            print("Nivel no válido. Por favor, elige facil, medio o dificil.")
            continue

        intentos = 0
        adivinado = False

        print(f"He elegido un número entre 1 y {numero_secreto}. ¿Puedes adivinar cuál es?")

        while not adivinado:
            try:
                intento = int(input("Introduce tu número: "))
                intentos += 1

                if intento < numero_secreto:
                    print("El número secreto es mayor. ¡Intenta de nuevo!")
                elif intento > numero_secreto:
                    print("El número secreto es menor. ¡Intenta de nuevo!")
                else:
                    adivinado = True
                    print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            except ValueError:
                print("Por favor, introduce un número válido.")

        # Preguntar si el jugador quiere jugar de nuevo
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_nuevamente != 'si':
            print("¡Gracias por jugar! Hasta luego.")
            break

if __name__ == "__main__":
    juego_adivinanzas()