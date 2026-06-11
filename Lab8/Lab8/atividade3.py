class Carteira:
    def __init__(self, moeda, saldo):
        self.__moeda = moeda
        self.__saldo = saldo

    def __add__(self, valor_yuan):
        if self.__moeda == "USD":
            valor_yuan *= 0.14
        elif self.__moeda == "BRL":
            valor_yuan *= 0.85
        return self.__saldo + valor_yuan

    def __sub__(self, valor_yuan):
        if self.__moeda == "USD":
            valor_yuan *=  0.14
        elif self.__moeda == "BRL":
            valor_yuan *= 0.85
        return self.__saldo - valor_yuan


carteira_usd = Carteira("USD", 10.0)
print('Soma de carteira USD + 50 yuan = ', carteira_usd + 50.0)