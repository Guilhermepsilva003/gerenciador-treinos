class Exercicio:
    def __init__(self,nome,series,repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes

    def __str__(self):
        return f"{self.nome} - {self.series} séries x {self.repeticoes} repetições"