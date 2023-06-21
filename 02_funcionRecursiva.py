def esPalindromo(palabra):
    if len(palabra) < 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return esPalindromo(palabra[1: -1])
        else:
            return False

print('La palabra OSO es un palindromo: ', esPalindromo('oso'))
print('La palabra ana es un palindromo: ', esPalindromo('ana'))
print('La palabra palabra es un palindromo: ', esPalindromo('palabra'))
