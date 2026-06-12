class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura
    
    def __str__(self):
        return f"Nome: {self.nome}, altura: {self.altura}"

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura

ps = int(input("Quantas pessoas serão cadastradas? "))

lista = []
for i in range(0, ps):
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    obj = Pessoa(nome, altura)
    lista.append(obj)

print(f"Maior altura: {max(lista)}")
print(f"Menor altura: {min(lista)}")

for pessoa in sorted(lista):
    print(pessoa)

