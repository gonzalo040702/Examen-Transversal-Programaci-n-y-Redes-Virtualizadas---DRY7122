def verificar_as(numero_as):
    # Rangos AS privados:
    # 64512 - 65534 (2 bytes privado)
    # 4200000000 - 4294967294 (4 bytes privado)
    
    if 64512 <= numero_as <= 65534:
        return "PRIVADO (rango 64512-65534)"
    elif 4200000000 <= numero_as <= 4294967294:
        return "PRIVADO (rango 4200000000-4294967294)"
    elif 1 <= numero_as <= 4294967294:
        return "PÚBLICO"
    else:
        return "INVÁLIDO (fuera de rango)"

while True:
    entrada = input("\nIngrese número de AS (o 's' para salir): ")
    
    if entrada.lower() == 's':
        print("Saliendo...")
        break
    
    try:
        numero_as = int(entrada)
        resultado = verificar_as(numero_as)
        print(f"El AS {numero_as} es: {resultado}")
    except ValueError:
        print("Por favor ingrese un número válido")
