import re

operadores_aritmeticos = {'w+' : 'suma', 'w-' : 'resta', 'w*' : 'multiplicacion', 'w/' : 'division'}
llave_operadores_aritmeticos = operadores_aritmeticos.keys()

operadores_relacionesles = {'w=':'igual','w!':'distinto'}
llave_operadores_relacionesles = operadores_relacionesles.keys()

operadores_logicos = {'wii' : 'comparacion y', 'woo' : 'comparacion o'}
llave_operadores_logicos = operadores_logicos.keys()

simbolos = {'-w-':'asignacion', 'w': 'abrir', 'o': 'cerrar', '.w.':'terminal', ';': 'separador'}
llave_simbolos=simbolos.keys()

palabras_reservadas = {'wor':'ciclo for','whole':'ciclo while', 'wof':'if', 'wolse':'else', 'woclass': 'clase', 'wo':'funcion'}
llave_palabras_reservadas = palabras_reservadas.keys()

identificadores = re.compile(r'\w+')

nuemero_entero = re.compile(r'\d+')

numero_real = re.compile(r'\d+\.\d+')

tipo_dato = {'wong32': 'long', 'woat32': 'float', 'wotring': 'string', 'woar':'char'}
llave_tipo_dato = tipo_dato.keys()

dataFlag = False

conteo=0

a= '''\
w+ w-
w= w!
wo clase
9.6
'''

program= a.split("\n")
for line in program:
    conteo = conteo + 1
    print("linea#" , conteo, "\n" , line)

    tokens=line.split()
    print("Los tokens son: " , tokens, "\n")
    for i in range(len(tokens)):
        token = tokens[i]
        if token in llave_operadores_aritmeticos:
            print(token," Es un operador aritmetico ", operadores_aritmeticos[token])
        elif token in llave_operadores_relacionesles:
            print(token, " Es un operador aritmetico ", operadores_relacionesles[token])
        elif token in llave_operadores_logicos:
            print(token, " Es un operador logico ", operadores_logicos[token])
        elif token in llave_simbolos:
            print(token, " Es un simbolo para ", simbolos[token])
        elif token in llave_palabras_reservadas:
            print(token, " Es una palabra reservada para ", palabras_reservadas[token])
        elif identificadores.fullmatch(token):
            anterior = tokens[i-1] if i-1 >= 0 else None
            if anterior in palabras_reservadas:
                print(token, " Es un identificador de ", palabras_reservadas[anterior])
            else:
                print(token, " Es un identificador de variable")
        elif numero_real.fullmatch(token):
            print(token, " Es un nuemero real")
        elif nuemero_entero.fullmatch(token):
            print(token, " Es un nuemero entero")
        elif token in llave_tipo_dato:
            print(token, " Es una palabra reservada para ", tipo_dato[token])
        else:
            print("No existe")
           
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")