
# classes/sim.py
class Sim:
    def __init__(self, id, tipo):
        self.id = id  # Identificador do Sim
        self.tipo = tipo  # Tipo do Sim (Aluno ou Servidor)
        self.local_atual = None  # Local atual do Sim (pode ser um prédio e andar)

    def mover_para(self, predio, andar=None):
        """
        Move o Sim para um prédio e, opcionalmente, para um andar.
        """
        print(f"{self.tipo} {self.id} está se movendo para {predio.nome} {andar if andar is not None else ''}")
        self.local_atual = (predio, andar)  # Atualiza o local atual para uma tupla (prédio, andar)

    def esperar(self):
        """
        Indica que o Sim está aguardando o elevador.
        """
        print(f"{self.tipo} {self.id} está aguardando o elevador.")