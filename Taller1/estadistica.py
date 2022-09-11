import matplotlib.pyplot as plt
import pandas as pd
from datosGenerador import *

def descriptiva(n):
    numeroRegistros = n
    datos = generarDatos(1000)

    # Especificar dataframes
    dfDatosGenerales = datos[1]
    dfDatosEspecificos = datos[3]

    # Creación de las tablas de Frecuencia necesitadas
    frecuenciaGraduados = (dfDatosEspecificos.groupby('Graduado?').agg(
        frequency=('Graduado?', 'count')) / numeroRegistros) * 100
    frecuenciaSexo = (dfDatosEspecificos.groupby('Sexo').agg(frequency=('Sexo', 'count')) / numeroRegistros) * 100
    frecuenciaMatriculados = (dfDatosGenerales.groupby('Año curso').agg(
        frequency=('Año curso', 'count')) / numeroRegistros) * 100

    # Creacion de tablas de frecuencia cruzadas
    graduadosPorDepartamentos = pd.crosstab(dfDatosEspecificos['Departamento'], dfDatosEspecificos['Graduado?'])
    graduadosPorSexo = pd.crosstab(dfDatosEspecificos['Sexo'], dfDatosEspecificos['Graduado?'])
    añosPerdidosDepartamentos = pd.crosstab(dfDatosGenerales['Departamento'], dfDatosGenerales['Aprueba?'])
    gradosAprobados = pd.crosstab(dfDatosGenerales['Grado escolar'], dfDatosGenerales['Aprueba?'])
    graduadosPorAño = pd.crosstab(dfDatosEspecificos['Ultimo Año Estudiado'], dfDatosEspecificos['Graduado?'])

    # Graficar los datos
    mediaMatriculados = dfDatosGenerales["Año curso"].mode()[0]
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(20, 25))
    frecuenciaGraduados.plot.pie(ax=axes[0, 0], y='frequency', autopct="%0.1f %%", ylabel='Estudiantes', title='Porcentaje De Estudiantes Graduados o No Graduados.')
    frecuenciaSexo.plot.pie(ax=axes[0, 1], y='frequency', autopct="%0.1f %%", ylabel='Estudiantes', title='Porcentaje De Estudiantes Según El Género.')
    graduadosPorSexo.plot(kind='bar', ax=axes[1, 0], title='Estudiantes Graduados Por Género.')
    frecuenciaMatriculados.plot(ax=axes[1, 1], grid=True, title=f'Porcentaje De Estudiantes Matriculados Por Año.\nEl {mediaMatriculados} fue el año en que más estudiantes matriculados hubieron.')
    añosPerdidosDepartamentos.plot(ax=axes[2, 0], kind='bar', grid=True, title='Años Totales De Estudio Perdidos Según El Departamento.')
    graduadosPorDepartamentos.plot(ax=axes[2, 1], kind='bar', grid=True, title='Estudiantes Graduados Por Departamento.')
    graduadosPorAño.plot(ax=axes[3, 0], kind='bar', grid=True, title='Graduación De Estudiantes Por Año')
    gradosAprobados.plot(ax=axes[3, 1], kind='bar', title='Años Perdidos De Estudio Según El Grado Escolar.')
    fig.tight_layout()
    plt.show()
