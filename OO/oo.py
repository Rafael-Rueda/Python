class Conta:
    def __init__(self, titular, saldo, numero, fatura):
        self.__titular = titular
        self.__saldo = int(saldo)
        self.__numero = int(numero)
        self.__fatura = int(fatura)
    
    # Getters

    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    @property
    def fatura(self):
        return self.__fatura
    
    # Setters

    @titular.setter
    def titular(self, valor):
        self.__titular = valor
    
    # Metodos

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f'Titular: {self.__titular}\nSaldo: {self.__saldo}\n')

    def transferir(self,valor, destinatario):
        self.sacar(valor)
        destinatario.depositar(valor)
