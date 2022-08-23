from random import *

sexo = ['Hombre', 'Mujer']

nombreHombre =["ANTONIO",
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

grado_escolar = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo", "once"]

exito = ['SI', 'NO']

n = 1000
edad = randrange(18)
temporal = None
nombre = nombreMujer[randrange(len(nombreMujer))] + ' ' + apellidos[randrange(len(apellidos))]
exito_ = exito[randrange(len(exito))]
gradoEscolar = grado_escolar[randrange(len(grado_escolar))]
año_inicio = randint(2004, 2021)

for i in range(n):
  if exito_.__eq__('NO'):
    temporal = False
  if exito_.__eq__('SI'):
    temporal = True
  if (temporal == True and gradoEscolar.__eq__('once')) or año_inicio > 2021:
    año_inicio = randint(2004, 2022)
    exito_ = exito[randrange(len(exito))]
    gradoEscolar = grado_escolar[randrange(len(grado_escolar))]
    if sexo[randrange(2)].__eq__('Hombre'):
      nombre = nombreHombre[randrange(len(nombreHombre))] + ' ' + apellidos[randrange(len(apellidos))]
    else:
      nombre = nombreMujer[randrange(len(nombreMujer))] + ' ' + apellidos[randrange(len(apellidos))]
  elif temporal == True:
    exito_ = exito[randrange(len(exito))]
    gradoEscolar = grado_escolar[grado_escolar.index(gradoEscolar)+1]
    print(f'Nombre: {nombre} | Grado escolar: {gradoEscolar} | Año de inicio: {año_inicio} | Exito: {exito_}')
  elif temporal == False:
    exito_ = exito[randrange(len(exito))]
    print(f'Nombre: {nombre} | Grado escolar: {gradoEscolar} | Año de inicio: {año_inicio} | Exito: {exito_}')
  año_inicio += 1
