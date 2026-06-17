# questão 01
n = input("Escreva o seu  primeiro nome: ")
sn = input("Escreva o seu sobrenome: ")

print("Bem-vinda, ", n, "", sn,"!")

# questão 02
f = input("Digite a frase: ")
print(f.count(" "))

# questao 03
n2 = input("Digite seu nome: ")
for i in range (len(n2)+1):
    print(n2[:i])

# questao 04
num = input("Digite o número: ")
if len(num) == 8: 
    print("Nùmero completo: ","9"+num[:5],"-",num[5:10])

elif len(num) == 9:
    if "9" in num[0]:
        print("Nùmero completo: ",num[:5],"-",num[5:10])
    else:
        print("O primeiro número precisa ser 9")

# questao 05
s = input("digite uma frase: ")
lista = []
for i in s:
    if i in "aeiou":
        j = s.find(i)
        lista.append(j)

print("Índice das vogais: ", lista)
print("Total: ",len(lista), "vogais")