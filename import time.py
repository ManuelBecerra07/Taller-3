import time

inicio = time.time()

# Cuenta regresiva sin pausas
for i in range(10, -1, -1):
    print(f"Tiempo restante: {i}")

fin = time.time()
tiempo_total = fin - inicio

print(f"Tiempo total de ejecución: {tiempo_total:.6f} segundos")