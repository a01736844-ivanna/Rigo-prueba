print("hola")

a = 89
b = 60
c = 10

def suma(x, y, z):
    return x + y + z

print("suma:", suma(a, b, c))

def generar_datos_ventas():
    dias = ["L", "M", "Mi", "J", "V"]
    ventas = [12, 13, 14, 15, 16]
    return dias, ventas

def resumen_analitica(): 
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total / len(ventas) if ventas else 0
    return {
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }

datos = resumen_analitica()
print("total ventas", datos["total"])
print("promedio", datos["promedio"])


import matplotlib.pyplot as plt

def graficar_ventas(dias, ventas):
    plt.figure(figsize=(8,4))
    plt.plot(dias, ventas, marker="o", linestyle="-", color="blue")
    plt.title("Ventas diarias")
    plt.xlabel("Día")
    plt.ylabel("ventas")
    plt.grid(True)
    plt.show()

def main_frontend():
    dias= ["L", "M", "Mi", "J", "V"]
    ventas = [12, 13, 14, 15, 16]
    graficar_ventas(dias, ventas)

main_frontend()