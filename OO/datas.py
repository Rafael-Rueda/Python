class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data = (str(self.dia), str(self.mes), str(self.ano))

    def data_formatada(self):
        print('/'.join(self.data))
