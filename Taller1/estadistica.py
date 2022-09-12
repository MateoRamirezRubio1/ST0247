import matplotlib.pyplot as plt
import pandas as pd
from datosGenerador import *

def descriptiva(dfDatosGenerales, dfDatosEspecificos, dfDatosModeloEspecificos):
    # Creación de las tablas de Frecuencia necesarias
    frecuenciaGraduados = (dfDatosEspecificos.groupby('Graduado?').agg(frequency=('Graduado?', 'count')) / len(dfDatosEspecificos['Graduado?'])) * 100
    frecuenciaSexo = (dfDatosEspecificos.groupby('Sexo').agg(frequency=('Sexo', 'count')) / len(dfDatosEspecificos['Sexo'])) * 100
    frecuenciaMatriculados = (dfDatosGenerales.groupby('Año curso').agg(frequency=('Año curso', 'count')) / len(dfDatosGenerales['Año curso'])) * 100
    frecuenciaProbabilidadGraduarse = dfDatosModeloEspecificos.groupby('Probabilidad Graduarse').agg(frequency=('Probabilidad Graduarse', 'count'))
    frecuenciaAcumuladaDepartamentos = dfDatosModeloEspecificos.groupby('Departamento').agg(frequency=('Departamento', 'count')).sort_values(by='frequency', ascending=False)

    # Creacion de tablas de frecuencia relativas cruzadas
    graduadosPorDepartamentos = pd.crosstab(dfDatosEspecificos['Departamento'], dfDatosEspecificos['Graduado?'], normalize=True)*100
    graduadosPorSexo = pd.crosstab(dfDatosEspecificos['Sexo'], dfDatosEspecificos['Graduado?'], normalize=True)*100
    añosPerdidosDepartamentos = pd.crosstab(dfDatosGenerales['Departamento'], dfDatosGenerales['Aprueba?'], normalize=True)*100
    gradosAprobados = pd.crosstab(dfDatosGenerales['Grado escolar'], dfDatosGenerales['Aprueba?'], normalize=True)*100
    graduadosPorAño = pd.crosstab(dfDatosEspecificos['Ultimo Año Estudiado'], dfDatosEspecificos['Graduado?'], normalize=True)*100
    relativasProbabilidadGraduarse = (frecuenciaProbabilidadGraduarse/len(dfDatosModeloEspecificos['Probabilidad Graduarse']))*100
    relativaAcumuladaDepartamentos = (frecuenciaAcumuladaDepartamentos/len(dfDatosModeloEspecificos['Departamento']))*100

    # Graficar los datos
    mediaMatriculados = dfDatosGenerales["Año curso"].mode()[0]
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(20, 30))
    frecuenciaGraduados.plot.pie(ax=axes[0, 0], y='frequency', autopct="%0.1f %%", ylabel='Estudiantes', title='Porcentaje De Estudiantes Graduados o No Graduados.')
    frecuenciaSexo.plot.pie(ax=axes[0, 1], y='frequency', autopct="%0.1f %%", ylabel='Estudiantes', title='Porcentaje De Estudiantes Según El Género.')
    graduadosPorSexo.plot(kind='bar', ax=axes[1, 0], title='porcentaje De Estudiantes Graduados Por Género.')
    frecuenciaMatriculados.plot(ax=axes[1, 1], grid=True, title=f'Porcentaje De Estudiantes Matriculados Por Año.\nEl {mediaMatriculados} fue el año en que más estudiantes matriculados hubieron.')
    añosPerdidosDepartamentos.plot(ax=axes[2, 0], kind='bar', grid=True, title='porcentaje Años Totales De Estudio Perdidos Según El Departamento.')
    graduadosPorDepartamentos.plot(ax=axes[2, 1], kind='bar', grid=True, title='Porcentaje Estudiantes Graduados Por Departamento.')
    graduadosPorAño.plot(ax=axes[3, 0], kind='bar', grid=True, title='Porcentaje Graduación De Estudiantes Por Año')
    gradosAprobados.plot(ax=axes[3, 1], kind='bar', grid=True, title='Porcentaje Años Perdidos De Estudio Según El Grado Escolar.')
    relativaAcumuladaDepartamentos.plot(ax=axes[4, 0], kind='bar', grid=True, title='Porcentaje De Estudiantes Por Departamento')
    relativasProbabilidadGraduarse.plot(ax=axes[4, 1], grid=True, title='Porcentaje De Estudiantes Según La Probabilidad De Graduarse', color='tab:orange')

    fig.tight_layout()
    plt.show()
