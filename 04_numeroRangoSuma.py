# rango_min = 1
# rango_max = 2147483647

# numero = int(input("Ingresa un número: "))
# b = 0

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        return ultimo_digito + suma_digitos(resto)
numero = int(input("Ingrese un número: "))
while numero < -2147483648 or numero > 2147483647:
    numero = int(input("Número fuera de rango. Ingrese otro número: "))
resultado = suma_digitos(abs(numero))
print("La suma de los dígitos de", numero, "es", resultado)
