# Verificar si un número es par y divisible por 4.

dato = int(input('Ingrese un número: '))

if dato % 2 == 0:
    print('El número es par.')
    if dato % 4 == 0:
        print('El número es divisible por 4.')
    else:
        print('No es divisible por 4.')
else:
    print('El número es impar.')