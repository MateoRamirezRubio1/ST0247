from estadistica import *
from datosGenerador import *
from prediccion import *

if __name__ == "__main__":
    print('BIENVENIDO!!')
    numeroRegistros = int(input('Cuantos registros desea?: '))

    if numeroRegistros > 0:
        # Especificar dataframes
        datos = generarDatos(numeroRegistros)
        dfDatosGenerales = datos[1]
        datosModelo = datos[2]
        dfDatosEspecificos = datos[3]

        #------------------------------------------------------------
        print('Escriba separado por comas(sin espacios ni puntos) el número de opcion u opciones que desea observar:\n'
            '   - 1: Ver tabla de todos los datos generales.\n'
            '   - 2: Ver tabla de datos especificos.\n'
            '   - 3: Ver tabla de datos especificos con la probabilidad de cada persona de graduarse.\n'
            '   - 4: Ver la estadistica en gráficas de los anteriores enunciados.')
        opcionUsuario = input().split(',')

        simodelo = False
        for i in opcionUsuario:
            if i.__eq__('1'):
                print('\nDatos generales:-----------------------------------------------------------------------')
                print(dfDatosGenerales.sort_values('Nombre'))
            elif i.__eq__('2'):
                print('\nDatos especificos:---------------------------------------------------------------------')
                print(dfDatosEspecificos.sort_values('Nombre'))
            elif i.__eq__('3'):
                simodelo = True
                # Modelo de Predicción probabilidad de graduarse o no graduarse
                dfModeloDatosEspecificos = predict(datosModelo, dfDatosEspecificos)
                print('\nDatos especificos con la probabilidad de graduarse por cada estudiante:----------------')
                print(dfModeloDatosEspecificos.sort_values('Nombre'))
            elif i.__eq__('4'):
                if simodelo:
                    # Estadistica
                    estadistica = descriptiva(dfDatosGenerales, dfDatosEspecificos, dfModeloDatosEspecificos)
                else:
                    estadistica = descriptiva(dfDatosGenerales, dfDatosEspecificos, predict(datosModelo, dfDatosEspecificos))
                print('\nEstadisticas con gráficas de los datos:------------------------------------------------')
                print(estadistica)
            else:
                print('\n--Opción no encontrada--')
    else:
        print('No es posible un número de registro igual o mayor a 0.\nVuelva a intentarlo.')
