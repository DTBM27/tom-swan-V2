# classes/andar.py
class Andar:
    def __init__(self, numero):
        self.numero = numero  # Número do andar
        self.sims_no_andar = []  # Lista para armazenar os Sims que estão no andar

    def adicionar_sim(self, sim):
        """
        Adiciona um Sim ao andar.
        """
        self.sims_no_andar.append(sim)  # Adiciona o Sim à lista
        print(f"{sim.tipo} {sim.id} entrou no andar {self.numero}.")

    def remover_sim(self, sim):
        """
        Remove um Sim do andar.
        """
        self.sims_no_andar.remove(sim)  # Remove o Sim da lista
        print(f"{sim.tipo} {sim.id} saiu do andar {self.numero}.")

    def listar_sims(self):
        """
        Retorna uma lista dos IDs dos Sims que estão no andar.
        """
        return [sim.id for sim in self.sims_no_andar]  # Retorna uma lista com os IDs dos Sims