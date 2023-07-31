class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1



class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1


vingadores = Filme("vingadores: guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print("Nome: {} - Ano: {} - Duração: {} - Likes: {}"
      .format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))

atlanta = Serie("atlanta", 2018, 2)
print("Nome: {} - Ano: {} - Temporadas: {} - Likes: {}"
      .format(atlanta.nome, atlanta.ano, atlanta.temporadas, atlanta.likes))