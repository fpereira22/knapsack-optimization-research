import random
import csv
import os

def generar_pisinger_strongly_correlated(n, R=1000):
    """
    Genera una instancia 'Strongly Correlated' de Pisinger.
    Peso w_i distribuido uniformemente en [1, R].
    Valor v_i = w_i + R/10.
    Capacidad W = (n * R / 2) * 0.8 (aprox media carga).
    """
    items = []
    # R es el rango de los pesos
    for i in range(1, n + 1):
        peso = random.randint(1, R)
        # La clave de Pisinger: El valor está fuertemente atado al peso
        valor = peso + int(R / 10)
        items.append({'id': i, 'peso': peso, 'valor': valor})
    
    capacidad = int((n * R / 2) * 0.5) # Capacidad ajustada para forzar decisiones
    return items, capacidad

def guardar_ampl_dat(items, capacidad, filename="pisinger_hard.dat"):
    """Genera el archivo .dat formateado para tu modelo AMPL"""
    with open(filename, 'w') as f:
        f.write(f"param PESOMAX := {capacidad};\n")
        f.write("param : ELEMENTOS : VALOR PESO :=\n")
        for item in items:
            f.write(f"{item['id']} {item['valor']} {item['peso']}\n")
        f.write(";\n")
    print(f"Archivo AMPL generado: {filename}")

def guardar_csv(items, capacidad, filename="pisinger_hard.csv"):
    """Genera un CSV para leer desde Julia/Python"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['capacidad_mochila', capacidad, '','']) # Header especial con capacidad
        writer.writerow(['id', 'valor', 'peso'])
        for item in items:
            writer.writerow([item['id'], item['valor'], item['peso']])
    print(f"Archivo CSV generado: {filename}")

# --- CONFIGURACIÓN DE LA PRUEBA ---
# Aquí definimos los tamaños (N) para encontrar el "Quiebre"
cantidades_a_probar = [100, 1000, 5000, 10000, 20000] 

for N in cantidades_a_probar:
    items, capacidad = generar_pisinger_strongly_correlated(N)
    
    # Nombres de archivo indicando el tamaño
    nombre_ampl = f"pisinger_n{N}.dat"
    nombre_csv = f"pisinger_n{N}.csv"
    
    guardar_ampl_dat(items, capacidad, nombre_ampl)
    guardar_csv(items, capacidad, nombre_csv)

print("\n¡Generación lista! Ahora tienes instancias difíciles para probar.")