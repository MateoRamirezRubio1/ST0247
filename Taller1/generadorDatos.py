from random import *

sexo = ['Hombre', 'Mujer']

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

grado_escolar = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo",
                 "once"]

exito = [True, False]

def nombreCompleto():
    apellido = apellidos[randrange(len(apellidos))]
    if sexo[randrange(len(sexo))].__eq__('Hombre'):
        nombre = nombreHombre[randrange(len(nombreHombre))] + " " + apellido + " " + apellido
    else:
        nombre = nombreMujer[randrange(len(nombreMujer))] + " " + apellido + " " + apellido
    return nombre

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
    return randint(1994, 2005)

n = 20
nuevo = True
datos = dict()

for i in range(n):
    if nuevo:
        añosPerdidosTotales = 0
        contador_años_perdidos = 0
        exito_ = sigue()
        nombre = nombreCompleto()
        gradoEscolar = grado(grado_escolar[0], nuevo, exito_)
        año_comienzo = añoComienzo()
        año_actual = año_comienzo
        print(f'{nombre} | {año_comienzo} | {gradoEscolar} | {exito_}')
        nuevo = False

    if exito_ == False:
        contador_años_perdidos += 1
        añosPerdidosTotales += 1
    else:
        contador_años_perdidos = 0

    if not nuevo and contador_años_perdidos < 3:
        gradoEscolar = grado(gradoEscolar, nuevo, exito_)
        exito_ = sigue()
        año_actual += 1
        print(f'{nombre} | {año_actual} | {gradoEscolar} | {exito_}')

    if (gradoEscolar.__eq__('once') and exito_) or (contador_años_perdidos == 2 and exito_ == False) or (i+1 == n):
        graduado = True
        if gradoEscolar != 'once':
          añosPerdidosTotales += 1
          graduado = False
        nuevo = True
        años_totales_estudio = (año_actual - año_comienzo)+1
        datos[nombre] = [añosPerdidosTotales, años_totales_estudio, graduado]

print(datos)
