# questao 01

a = []
r = 's'
while r == 's':
    x = int(input("Digite um número inteiro: "))
    a.append(x)
    r = input("Deseja adicionar mais um número? ")

print(a)
print(a[:3])
print(f"[{a[-2]}, {a[-1]}]")
print(sorted(a, reverse=True))
print([i for i in a if i % 2 == 0])
print([i for i in a if i % 2 != 0])

# questao 02

URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
for i in URLs:
    list(i).remove("w")

print(URLs)