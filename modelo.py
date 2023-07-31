class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme("Vingadores: Guerra Infinita", 2018, 160)
print("Nome: {} - Ano: {} - Duração: {}".format(vingadores.nome, vingadores.ano, vingadores.duracao))

atlanta = Serie("Atlanta", 2018, 2)
print("Nome: {} - Ano: {} - Temporadas: {}".format(atlanta.nome, atlanta.ano, atlanta.temporadas))