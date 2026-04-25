from models.exercicio import Exercicio

class Treino:
    def __init__(self,nome):
        self.nome = nome
        self.exercicios = []

    def adicionar_exercicio(self, nome, series, repeticoes):
            exercicio = Exercicio(nome, series, repeticoes)
            self.exercicios.append(exercicio)

    def __str__ (self):
            if len(self.exercicios) == 0:
                return f"{self.nome} (sem exercícios)"

            resultado = f"{self.nome}:\n"
            for exercicio in self.exercicios:
                resultado += f" - {exercicio}\n"
            return resultado