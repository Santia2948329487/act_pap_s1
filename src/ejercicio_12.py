n = int(input("Ingrese un número para calcular su factorial: "))
resultado = 1
i = 1
while i <= n:
    resultado *= i
    i += 1
print(f"El factorial de {n} es {resultado}")
