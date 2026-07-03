from pathlib import Path
# questao 01

def contagem_caracteres(x):
    return {x: len(x)}

frase = 'catapimbas'
resultado = contagem_caracteres(frase)
print(resultado)

# questao 02
#arquivo = open('C:/Users/Admin/OneDrive/Documentos/GitHub/atividades_individuais_poo/Lab9/estomago.txt', 'r', encoding='utf-8')   
#texto = arquivo.read()
#alfabeto = {
#    'a': 1,
#    'b': 2,
#    'c': 3,
#    'd': 4, 
#    'e': 5,
#    'f': 6,
#    'g': 7,
#    'h': 8,
#    'i': 9,
#    'j': 10,
#    'k': 11,
#    'l': 12,
#    'm': 13,
#    'n': 14,
#    'o': 15,
#    'p': 16,
#    'q': 17,
#    'r': 18,
#    's': 19,
#    't': 20,
#    'u': 21,
#    'v': 22,
#    'w': 23,
#    'x': 24,
#    'y': 25,
#    'z': 26
#}
#quant = {}
#for i in alfabeto:
#    quant[i] = texto.count(i)

#sorted(quant.values(), reverse=True)
#print(quant)

# questao 03

def mesclar_dicionarios(d1, d2):
    novo_dic = {}
    for chave, valor in d1.items():
        novo_dic[chave] = valor
    for chave, valor in d2.items():
        if chave in novo_dic:
            if valor > novo_dic[chave]:
                novo_dic[chave] = valor
        else:
            novo_dic[chave] = valor
    return novo_dic
    
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

# questao 04

def filtrar_dicionario(dic, lista):
    novo_dic = {}
    for chave, valor in dic.items():
        if chave in lista:
            novo_dic[chave] = valor
    return novo_dic

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

# questao 05

def resultado_votacao(votos):
    novo_dic = []
    for i in votos:
        for chave, valor in i.items():
            novo_dic.append(chave) 
    return dict(novo_dic)

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)  # Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 
                                ###  'candidato_C': (275, 30.79)}