from random import *
import pandas as pd

sexo = ['HOMBRE', 'MUJER']

nombreHombre = ["ANTONIO",
                "MANUEL",
                "JOSE",
                "FRANCISCO",
                "DAVID",
                "JUAN",
                "JAVIER",
                "JOSE ANTONIO",
                "DANIEL",
                "JOSE LUIS",
                "FRANCISCO JAVIER",
                "CARLOS",
                "JESUS",
                "ALEJANDRO",
                "MIGUEL",
                "JOSE MANUEL",
                "RAFAEL",
                "MIGUEL ANGEL",
                "PABLO",
                "PEDRO",
                "ANGEL",
                "SERGIO",
                "JOSE MARIA",
                "FERNANDO",
                "JORGE",
                "LUIS",
                "ALBERTO",
                "ALVARO",
                "JUAN CARLOS",
                "ADRIAN",
                "DIEGO",
                "JUAN JOSE",
                "RAUL",
                "IVAN",
                "JUAN ANTONIO",
                "RUBEN",
                "ENRIQUE",
                "OSCAR",
                "RAMON",
                "ANDRES",
                "VICENTE",
                "JUAN MANUEL",
                "SANTIAGO",
                "JOAQUIN",
                "VICTOR",
                "MARIO",
                "EDUARDO",
                "ROBERTO",
                "JAIME",
                "FRANCISCO JOSE",
                "MARCOS",
                "IGNACIO",
                "HUGO",
                "ALFONSO",
                "JORDI",
                "RICARDO",
                "SALVADOR",
                "GUILLERMO",
                "GABRIEL",
                "MARC",
                "EMILIO",
                "MOHAMED",
                "GONZALO",
                "JULIO",
                "JULIAN",
                "MARTIN",
                "JOSE MIGUEL",
                "TOMAS",
                "AGUSTIN",
                "NICOLAS",
                "JOSE RAMON",
                "SAMUEL",
                "ISMAEL",
                "JOAN",
                "CRISTIAN",
                "FELIX",
                "LUCAS",
                "AITOR",
                "HECTOR",
                "JUAN FRANCISCO",
                "IKER",
                "ALEX",
                "JOSE CARLOS",
                "JOSEP",
                "SEBASTIAN",
                "MARIANO",
                "CESAR",
                "ALFREDO",
                "DOMINGO",
                "JOSE ANGEL",
                "FELIPE",
                "VICTOR MANUEL",
                "RODRIGO",
                "JOSE IGNACIO",
                "MATEO",
                "LUIS MIGUEL",
                "JOSE FRANCISCO",
                "JUAN LUIS",
                "XAVIER",
                "ALBERT"]

nombreMujer = ["MARIA CARMEN",
               "MARIA",
               "CARMEN",
               "ANA MARIA",
               "JOSEFA",
               "MARIA PILAR",
               "ISABEL",
               "LAURA",
               "MARIA DOLORES",
               "MARIA TERESA",
               "ANA",
               "CRISTINA",
               "MARTA",
               "MARIA ANGELES",
               "LUCIA",
               "FRANCISCA",
               "MARIA ISABEL",
               "MARIA JOSE",
               "ANTONIA",
               "DOLORES",
               "SARA",
               "PAULA",
               "ELENA",
               "MARIA LUISA",
               "RAQUEL",
               "ROSA MARIA",
               "PILAR",
               "MANUELA",
               "CONCEPCION",
               "MARIA JESUS",
               "MERCEDES",
               "JULIA",
               "BEATRIZ",
               "NURIA",
               "SILVIA",
               "ALBA",
               "IRENE",
               "ROSARIO",
               "JUANA",
               "TERESA",
               "PATRICIA",
               "ENCARNACION",
               "MONTSERRAT",
               "ANDREA",
               "ROCIO",
               "MONICA",
               "ALICIA",
               "MARIA MAR",
               "ROSA",
               "SONIA",
               "SANDRA",
               "MARINA",
               "ANGELA",
               "SUSANA",
               "NATALIA",
               "YOLANDA",
               "MARGARITA",
               "MARIA JOSEFA",
               "CLAUDIA",
               "SOFIA",
               "EVA",
               "CARLA",
               "MARIA ROSARIO",
               "INMACULADA",
               "MARIA MERCEDES",
               "ANA ISABEL",
               "ESTHER",
               "NOELIA",
               "VERONICA",
               "NEREA",
               "CAROLINA",
               "ANGELES",
               "DANIELA",
               "MARIA VICTORIA",
               "EVA MARIA",
               "INES",
               "MIRIAM",
               "LORENA",
               "MARIA ROSA",
               "MARIA ELENA",
               "ANA BELEN",
               "VICTORIA",
               "MARIA CONCEPCION",
               "AMPARO",
               "MARTINA",
               "MARIA ANTONIA",
               "ALEJANDRA",
               "LIDIA",
               "CATALINA",
               "CELIA",
               "MARIA NIEVES",
               "CONSUELO",
               "FATIMA",
               "OLGA",
               "AINHOA",
               "GLORIA",
               "CLARA",
               "MARIA CRISTINA",
               "MARIA SOLEDAD",
               "EMILIA"]

apellidos = ["MARTINEZ",
             "GARCIA",
             "FERNANDEZ",
             "PEREZ",
             "JIMENEZ",
             "GONZALEZ",
             "RUIZ",
             "LOPEZ",
             "SAENZ",
             "RODRIGUEZ",
             "GOMEZ",
             "MORENO",
             "HERNANDEZ",
             "SANCHEZ",
             "ALONSO",
             "PASCUAL",
             "GIL",
             "MARIN",
             "DIEZ",
             "ALVAREZ",
             "GUTIERREZ",
             "MARTIN",
             "CALVO",
             "BLANCO",
             "EZQUERRO",
             "RUBIO",
             "IBAÑEZ",
             "MUÑOZ",
             "GARRIDO",
             "SAEZ",
             "DIAZ",
             "RAMIREZ",
             "PALACIOS",
             "ORTEGA",
             "BENITO",
             "SANTAMARIA",
             "ROMERO",
             "OCHOA",
             "LEON",
             "DOMINGUEZ",
             "HERCE",
             "PEÑA",
             "GABARRI",
             "MERINO",
             "TORRES",
             "SAINZ",
             "SANZ",
             "CASTILLO",
             "ORTIZ",
             "CORDON"]

departamentos = ["AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLÁNTICO", "BOGOTÁ", "BOLÍVAR", "BOLÍVAR", "BOYACÁ", "CALDAS", "CAQUETÁ", "CASANARE", "CAUCA", "CESAR", "CHOCÓ", "CÓRDOBA", "CUNDINAMARCA", "GUANÍA", "GUAVIARE", "HUILA", "LA GUAJIRA", "MAGDALENA", "META", "NARIÑO", "NORTE DE SANTANDER", "PUTUMAYO", "QUINDÍO", "RISARALDA", "SAN ANDRÉS Y PROVIDENCIA", "SANTANDER", "SUCRE", "TOLIMA", "VALLE DEL CAUCA", "CAUPÉS", "VICHADA"]

grado_escolar = ["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO", "SEPTIMO", "OCTAVO", "NOVENO", "DECIMO", "ONCE"]

exito, reanudar = [True, False], [True, False]

def reanuda(año_actual):
    año_reanuda = año_actual + randrange(2, 10)
    if reanudar[randrange(len(reanudar))] and año_reanuda < 2022:
        return año_reanuda
    return año_actual

def nombreCompleto():
    apellido1 = apellidos[randrange(len(apellidos))]
    apellido2 = apellidos[randrange(len(apellidos))]
    sexoPersona = sexo[randrange(len(sexo))]
    if sexoPersona.__eq__('HOMBRE'):
        nombre = nombreHombre[randrange(len(nombreHombre))] + " " + apellido1 + " " + apellido2
    else:
        nombre = nombreMujer[randrange(len(nombreMujer))] + " " + apellido1 + " " + apellido2
    return nombre, sexoPersona

def grado(gradoEscolar, nuevo, pasa):
    if nuevo:
        gradoEscolar = grado_escolar[0]
    if pasa and not nuevo:
        gradoEscolar = grado_escolar[grado_escolar.index(gradoEscolar) + 1]
    return gradoEscolar

def sigue():
    exito_ = exito[randrange(len(exito))]
    return exito_

def añoComienzo():
    return randint(1985, 2005)

def departamento_vive():
    return departamentos[randrange(len(departamentos))]

def generarDatos(cantidad):
    # Se inicializan variables
    nuevo = True
    datos = dict()
    arreglo_de_datos = []
    arreglo_de_datos_especificos = []
    datosModelo = []

    for i in range(cantidad):
        # 2: Continuar el historial de la persona creada
        if not nuevo and contador_años_perdidos < 3:
            gradoEscolar = grado(gradoEscolar, nuevo, exito_)
            exito_ = sigue()
            año_actual += 1
            arreglo_de_datos.append([nombre, departamento, año_actual, gradoEscolar, exito_])

        # 1: Crear personas nuevas
        if nuevo:
            veces_reanuda = 0
            años_receso = 0
            añosPerdidosTotales = 0
            contador_años_perdidos = 0
            exito_ = sigue()
            persona = nombreCompleto()
            nombre = persona[0]
            sexoPersona = persona[1]
            gradoEscolar = grado(grado_escolar[0], nuevo, exito_)
            departamento = departamento_vive()
            año_comienzo = añoComienzo()
            año_actual = año_comienzo
            nuevo = False

            # Agregar datos al arreglo de datos generales para la tabla
            arreglo_de_datos.append([nombre, departamento, año_comienzo, gradoEscolar, exito_])

        # 3: Validar si aprobó o no el curso actual para contabilizar datos de años perdidos
        if not exito_ and contador_años_perdidos < 3:
            contador_años_perdidos += 1
            añosPerdidosTotales += 1
        else:
            contador_años_perdidos = 0

        # Parar el historial de la persona si se gradua, si pierde más de 2 años o si se acaba el ciclo
        if (gradoEscolar.__eq__('ONCE') and exito_) or (contador_años_perdidos > 2 and not exito_) or (i+1 == cantidad) or (año_actual == 2022):
            graduado = True
            nuevo = True

            # Si la persona no es graduada se valida si despues de un periodo retome los estudios
            sireanuda = reanuda(año_actual)
            if (gradoEscolar != 'ONCE' and not exito_ and sireanuda > año_actual and año_actual < 2022) or (gradoEscolar != 'ONCE' and i+1 == cantidad):
                nuevo = False
                graduado = False
                contador_años_perdidos = 0
                años_receso += sireanuda - año_actual
                año_actual = sireanuda
                veces_reanuda += 1
            # Si la persona no graduada no retoma sus estudios queda como no graduado
            elif (gradoEscolar != 'ONCE') or (gradoEscolar.__eq__('ONCE') and (contador_años_perdidos > 2 or i+1 == cantidad or año_actual == 2022) and not exito_):
                graduado = False

            años_totales_estudio = ((año_actual - año_comienzo) + 1) - años_receso

            if nuevo or i+1 == cantidad:
                # Agregar datos al arreglo de datos generales para la tabla
                arreglo_de_datos_especificos.append([nombre, sexoPersona, departamento, años_totales_estudio, añosPerdidosTotales, año_actual, graduado])
                # Se ingresan los datos de entrada para el modelo de probabilidad en un arreglo
                datosModelo.append([añosPerdidosTotales/23, veces_reanuda/5, años_totales_estudio/33, 1 if graduado else 0])
            
            datos[nombre] = [añosPerdidosTotales, veces_reanuda, años_totales_estudio, graduado]
            

    # Se crean los dataframes con los arreglos de datos creados para relizar la estadística
    dfDatosGenerales = pd.DataFrame(arreglo_de_datos, columns=('Nombre', 'Departamento', 'Año curso', 'Grado escolar', 'Aprueba?'))
    dfDatosEspecificos = pd.DataFrame(arreglo_de_datos_especificos, columns=('Nombre', 'Sexo', 'Departamento', 'Años totales de estudio', 'Años totales perdidos', 'Ultimo Año Estudiado', 'Graduado?'))

    return datos, dfDatosGenerales, datosModelo, dfDatosEspecificos
