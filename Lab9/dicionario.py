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
arquivo.close()
texto = texto.replace(".", " ")
texto = texto.replace(",", " ")
texto = texto.replace("\n", " ")

palavras = texto.split()

quant_palavras = {}

for palavra in palavras:
    if palavra in quant_palavras:
        quant_palavras[palavra] += 1
    else:
        quant_palavras[palavra] = 1

def pega_valor(item):
    return item[1]

quant = dict(sorted(quant_palavras.items(), key = pega_valor, reverse=True))

print(quant)

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
    novo_dic = {}
    for voto in votos:
        for chave, valor in voto.items():
            if chave in novo_dic:
                novo_dic[chave] += valor
            else:
                novo_dic[chave] = valor
    total = sum(novo_dic.values())
    for chave, valor in novo_dic.items():
        media = round((valor / total) * 100, 2)
        novo_dic[chave] = (valor, media)
    return novo_dic

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)