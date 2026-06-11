class Onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.num_assentos = num_assentos
        self.assentos = [True, False]

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if 0 <= indice < (len(self.assentos)):
            return self.assentos[indice]
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)-1}")
        
    def __setitem__(self, indice, valor):
        if not isinstance(valor, bool):
            raise TypeError(f"Valor deve ser booleano (True/False)")
        if 0 > indice or indice >= (len(self.assentos)):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        else:
            self.assentos[indice] = valor

    def __str__(self):
        ocupados = []
        for i in self.assentos:
            if i == False:
                ocupados.append(i)
        return f'''Ônibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}
        Assentos totais: {self.num_assentos}
        Assentos ocupados: {len(ocupados)}'''
obj = Onibus("adjfashkjd", "marcio", 30)
tungh = 1
a = obj[tungh]
print(a)
print(obj)

