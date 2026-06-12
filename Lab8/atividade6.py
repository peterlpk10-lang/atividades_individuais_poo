import random

class Personagem:
    def __init__(self, nome, vida):
        self._nome = nome
        self._vida = vida

    def tomar_dano(self, valor):
        self._vida -= valor

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.__mana = mana
    
    def __str__(self):
        return f'''Nome: {self._nome}
Vida: {self._vida}
Mana: {self.__mana}'''

    def __add__(self, valor):
        self.__mana += valor
        return f"Mana: {self.__mana}"

    def __sub__(self, valor):
        if (self.__mana - valor) >= 0:
            self.__mana -= valor
        else:
            raise TypeError(f"Valor deve ser maior ou igual a quantidade de mana!")
        return f"Mana: {self.__mana}"
    
    def __mul__(self, fator):
        self.__mana *= fator
        return f"Mana: {self.__mana}"

    def __truediv__(self, valor):
        self.__mana /= valor
        return f"Mana: {self.__mana}"

class Barbaro(Personagem):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.__stamina = stamina
        self.__furia = False

    def __str__(self):
        return f'''Nome: {self._nome}
Vida: {self._vida}
Stamina: {self.__stamina}
Fúria: {self.__furia}'''

    def __add__(self, valor):
        mult = 1
        if self.__furia:
            mult = 1.5
        self.__stamina += valor * mult
        return self.__stamina

    def __sub__(self, valor):
        self.__stamina -= valor
        if self.__stamina <= 0 and self.__furia == False:
            self.__furia = True
            self.__stamina = 5
        return self.__stamina

    def __mul__(self, fator):
        self.__stamina *= fator
        if self.__furia:
            self._vida += 5
        
    def __truediv__(self, valor):
        self.__stamina /= valor
        return self.__stamina 
nome = input("Informe o nome do personagem: ")
vida = int(input("Informe quantos pontos de vida: "))
tipo = input('''Informe qual tipo de personagem:
(a) Mago
(b) Bárbaro
R: ''')
match tipo:
    case "a":
        mana = float(input("Informe a quantidade de mana: "))
        p = Mago(nome, vida, mana) 
    case "b":
        stamina = float(input("Informe a quantidade de stamina: "))
        p = Barbaro(nome, vida, stamina)
for i in range(5):
    opcoes = input('''(a) TOMAR POÇÃO SIMPLES
(b) TOMAR POÇÃO ESPECIAL
(c) ATAQUE BÁSICO 
(d) ATAQUE ESPECIAL
R: ''')
    match opcoes:
        case "a":
            print(p + 5)
        case "b":
            print(p * 1.5)
        case "c":
            print(p - 2)
        case "d":
            print(p / 2)
    p.tomar_dano(random.randint(1, 10))
    print(p)