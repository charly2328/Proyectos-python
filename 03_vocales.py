cadena = input("Ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"
j = 0
for i in cadena:
    if i in vocales:
        j = j + 1
print(f"la cadena tiene {j} vocales")