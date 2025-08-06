import random
secreto = random.randint(1, 10)
adivina = int(input("Adivina el número (entre 1 y 10): "))
while adivina != secreto:
    adivina = int(input("Incorrecto, intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")
