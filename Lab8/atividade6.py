class Personagem:
    def __init__(self, nome, vida):
        self._nome = nome
        self._vida = vida

    def tomar_dano(self, valor)
        self._vida -= vida

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome<vida)
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
        self.__mana *= 


