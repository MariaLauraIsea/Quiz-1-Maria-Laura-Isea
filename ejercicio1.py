#================================
# Nombre: Maria Laura Isea
# Carnet: 20221110255
#================================

from turtle import pen


penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]

numeros_penta=[]

pentagonales=[]

nro_pentagonal0=((3*(0**2)-0)/(2))
pentagonales.append(nro_pentagonal0)

nro_pentagonal1=((3*(1**2)-1)/(2))
pentagonales.append(nro_pentagonal1)

nro_pentagonal2=((3*(2**2)-2)/(2))
pentagonales.append(nro_pentagonal2)

nro_pentagonal3=((3*(3**2)-3)/(2))
pentagonales.append(nro_pentagonal3)

nro_pentagonal4=((3*(4**2)-4)/(2))
pentagonales.append(nro_pentagonal4)

nro_pentagonal5=((3*(5**2)-5)/(2))
pentagonales.append(nro_pentagonal5)

nro_pentagonal6=((3*(6**2)-6)/(2))
pentagonales.append(nro_pentagonal6)

nro_pentagonal7=((3*(7**2)-7)/(2))
pentagonales.append(nro_pentagonal7)

nro_pentagonal8=((3*(8**2)-8)/(2))
pentagonales.append(nro_pentagonal8)

nro_pentagonal9=((3*(9**2)-9)/(2))
pentagonales.append(nro_pentagonal9)


print(pentagonales)

for grupo_nros in penta:
    for number in grupo_nros:
        for pentag in pentagonales:
            if number==pentag:
                numeros_penta.append(number)
        
print('los numeros pentagonales presentes en la estructura son: ')
print(numeros_penta)
