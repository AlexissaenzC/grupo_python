# De una ecuación cuadrática hallar las raices o ceros. x^2+2x+1

a = float(input('Ingrese el coeficiente cuadrático: '))
b = float(input('Ingrese el coeficiente lineal: '))
c = float(input('Ingrese el termino independiente: '))

discriminate = b**2 - 4*a*c

if a != 0:
    print(discriminate)
    if discriminate < 0:
        print('Las raices son complejas.')
    elif discriminate > 0:
        print('Las raices son reales.')
        cuadrática_1 = (-b + (discriminate)**0.5)/2*a
        cuadrática_2 = (-b - (discriminate)**0.5)/2*a
        print(f'La primera raiz es {cuadrática_1} y la segunda raiz es {cuadrática_2}')
    else:
        print('Las raices son iguales.')
        cuadrática = (-b + (discriminate)**0.5)/2*a
        print(f'La riaz de la ecuación cuadrática es {cuadrática}')
else:
    print('El coeficiente cuadrático tiene que ser diferente que 0.')