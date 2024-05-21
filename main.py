import re

operadores_aritmeticos = {'w+' : 'suma', 'w-' : 'resta', 'w*' : 'multiplicacion', 'w/' : 'division'}
llave_operadores_aritmeticos = operadores_aritmeticos.keys()

operadores_relacionesles = {'w=':'igual','w!':'distinto'}
llave_operadores_relacionesles = operadores_relacionesles.keys()

operadores_logicos = {'wii' : 'comparacion y', 'woo' : 'comparacion o'}
llave_operadores_logicos = operadores_logicos.keys()

dataFlag = False

count=0

a= '''\
w+ w-
w= w!
'''

program= a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in llave_operadores_aritmeticos:
            print(token," Es un operador aritmetico ", operadores_aritmeticos[token])
        if token in llave_operadores_relacionesles:
            print(token, " Es un operador logico ", operadores_relacionesles[token])
           
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")