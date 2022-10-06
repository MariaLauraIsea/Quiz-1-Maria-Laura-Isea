#================================
# Nombre: Maria Laura Isea
# Carnet: 20221110255
#================================

number=input('ingrese un numero: ')

while not number.isnumeric():
    number=input('ingreso invalido\ningrese un numero ')

comprobador=True
first_digit=number[0]


for digit in number:
    if digit != first_digit:
        comprobador=False
    
if comprobador:
    print(f'el numero {number} es un numero repunit')
else:
    print(f"el numero {number} no es un numero repunit")