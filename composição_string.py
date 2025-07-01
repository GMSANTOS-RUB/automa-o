nome = "gustavo"
idade = 17
dinheiro = 10.4
print("%s tem %d anos e R$%f no bolso." % (nome, idade, dinheiro))    


import sys 
print("numeros de parametros; %d" %len(sys.argv))
for n,p in enumerate(sys.argv):
    print("parametro %d = %s" % (n,p))


import sys 
import os
print("numerode parametros: %d" % len(sys.argv))

for n, p in enumerate(sys.argv):
    print("parametro %d = %s" % (n,p))
    os.mkdir(p)

try:
    with open("modulo_sys.py", "rb") as fs1:
        dados = fs1.read()
        print(type(dados))
    with open("teste01.jpg", "wb") as fs1:
        fs1.write()

except FileNotFoundError as e:
    print('arquivo nao existe! -_-|||', e)
except IOError as e:
    print('deu algo errado @_@')
    print("OK! ~_~")

import os 

try:
    os.remove("teste02.jpg")
    print(f"excluido {"teste1.jpg"}")
except: 
    print("nao foi possivel")
