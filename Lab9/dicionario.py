from pathlib import Path
# questao 01

def contagem_caracteres(x):
    return {x: len(x)}

frase = 'catapimbas'
resultado = contagem_caracteres(frase)
print(resultado)

# questao 02

arquivo = open('C:/Users/Admin/OneDrive/Documentos/GitHub/atividades_individuais_poo/Lab9/estomago.txt', 'r', encoding='utf-8')   
texto = arquivo.read()
alfabeto = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4, 
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}
quant = {}
for i in alfabeto:
    quant[i] = texto.count(i)

sorted(quant.values(), reverse=True)
print(quant)

# questao 03

def mesclar_dicionarios(d1, d2):
    if len(d1) > len(d2):
        for i in d1:
            
    
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)