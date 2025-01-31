# classes/predio.py
class Predio:
    def __init__(self, nome):
        self.nome = nome  # Nome do prédio
        self.sims_no_predio = []  # Lista para armazenar os Sims que estão no prédio

    def adicionar_sim(self, sim):
        """
        Adiciona um Sim ao prédio.
        """
        self.sims_no_predio.append(sim)  # Adiciona o Sim à lista
        sim.local_atual = self  # Atualiza o local atual do Sim para este prédio
        print(f"{sim.tipo} {sim.id} entrou no {self.nome}.")

    def remover_sim(self, sim):
        """
        Remove um Sim do prédio.
        """
        self.sims_no_predio.remove(sim)  # Remove o Sim da lista
        print(f"{sim.tipo} {sim.id} saiu do {self.nome}.")

    def listar_sims(self):
        """
        Retorna uma lista dos IDs dos Sims que estão no prédio.
        """
        return [sim.id for sim in self.sims_no_predio]  # Retorna uma lista com os IDs dos Sims