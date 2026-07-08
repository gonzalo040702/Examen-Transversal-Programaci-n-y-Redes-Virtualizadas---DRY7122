from tabulate import tabulate

integrantes = [
    ["1", "Gonzalo", "Núñez"],
    ["2", "Daniel", "Burgos"]
]

print("\n===== INTEGRANTES DEL GRUPO =====")
print(tabulate(integrantes, headers=["N°", "Nombre", "Apellido"], tablefmt="grid"))
