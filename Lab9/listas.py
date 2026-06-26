import random
# questao 01

a = []
r = 's'
r2 = int(input("Quantos números você deseja armazenar: "))
for i in range(r2):
    x = int(input("Digite um número inteiro: "))
    a.append(x)

print(a)
print(a[:3])
print(f"[{a[-2]}, {a[-1]}]")
print(sorted(a, reverse=True))
print([i for i in a if i % 2 == 0])
print([i for i in a if i % 2 != 0])

# questao 02

URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
for indice, valor in enumerate(URLs):
    URLs[indice] = valor[4:-4]
print(URLs)

# questao 03

nums = []
for i in range(10):
    nums.append(random.randint(-100, 100))

print(sorted(nums))
print(nums)
print(nums.index(max(nums)))
print(nums.index(min(nums)))
print(sum(nums))
print(sum(nums)/10)

# questao 04

l1 = []
quant_l1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os 4 elementos da lista 1: ")
for i in range(quant_l1):
    l1.append(int(input(f"{i+1}º número: ")))
l2 = []
quant_l2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os 4 elementos da lista 2: ")
for i in range(quant_l2):
    l2.append(int(input(f"{i+1}º número: ")))

lista_inter = []
if len(l1) > len(l2):
    for i in l2:
        lista_inter.append(i)
        lista_inter.append(l1[i-1])
    for i in l1[-(len(l1)-len(l2)):]:
        lista_inter.append(i)
if len(l1) == len(l2):
    for i in range(len(l2)):
        lista_inter.append(l1[i])
        lista_inter.append(l2[i])
else:
    for i in l1:
        lista_inter.append(i)
        lista_inter.append(l2[i-1])
    for i in l2[-(len(l2)-len(l1)):]:
        lista_inter.append(i)

print(f"Lista intercalada: {lista_inter}")

# questao 05

l1 = [random.randint(0, 50) for i in range(20)]
l2 = [random.randint(0, 50) for i in range(20)]
interseccao = [i for i in range(0, 50) if (i in l1) and (i in l2) ]
print(f"Lista 1 - {l1}")
print(f"Lista 2 - {l2}")
print(f"Intersecção - {interseccao}")

# questao 06

lista100 = [random.randint(0, 100) for i in range(20)]
listadiv3 = [lista100[i:i+3] for i in range(0, 20, 3)]
listadiv4 = [lista100[i:i+4] for i in range(0 ,20, 4)]

# questao 07

n = int(input("Digite n: "))
result = [[i  for j in range(n)] for i in range(n)]
for i in range(n):
    print(result[i])


