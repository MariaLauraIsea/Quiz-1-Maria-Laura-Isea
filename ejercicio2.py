#================================
# Nombre: Maria Laura Isea
# Carnet: 20221110255
#================================

anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}

historial=[]

quit=False

while quit==False:
    option=input('\nseleccione una accion a realizar:\n1-seleccionar una serie a ver\n2-consultar historial de vistos\n3-salir\n=> ')
    while not option.isnumeric() or 0>int(option)>3:
        option=input('ingreso invalido. seleccione una accion a realizar:\n1-seleccionar una serie a ver\n2-consultar historial de vistos\n3-salir\n=> ')

    if int(option)==1:
        print('ANIMES DISPONIBLES')
        aux=1
        for serie,temporadas in anime.items():
            print(f'{aux}: {serie}')
           
            print('   Temporadas disponibles')

            for nro_temporada,info_capitulos in temporadas.items():
                print(f'     {nro_temporada}')
            
            aux+=1

        show=input('ingrese el nombre como muestra en pantalla del anime que desea ver: ')
        
        for serie,temporadas in anime.items():
            lista_series=[]
            lista_series.append(serie)
            #print(lista_series)
            for ashow in lista_series:
                if show==ashow:
                    for nro_temporada,info_capitulos in temporadas.items():
                        print(f'{nro_temporada}')
                    temporada_seleccionada=input('ingrese en el formato "temporada (nro temporada)" la temporada que desea ver: ')
        for serie,temporadas in anime.items():
            for nro_temporada, info_capitulos in temporadas.items():
                lista_temporadas=[]
                lista_temporadas.append(nro_temporada)
                for atemp in lista_temporadas:
                    if temporada_seleccionada==atemp:

                        for capitulo in info_capitulos:
                            print(capitulo)

                        capitulo_seleccionado=input('ingrese el numero del capitulo que deseea ver: ')



        

            
    #elif int(option)==2:

    else:
        quit=True