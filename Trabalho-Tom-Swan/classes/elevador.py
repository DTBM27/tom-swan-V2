# classes/elevador.py
class Elevador:
    def __init__(self, capacidade, andares):
        self.capacidade = capacidade  # Capacidade máxima do elevador
        self.andares = andares  # Total de andares que o elevador atende
        self.sims_no_elevador = []  # Lista para armazenar os Sims que estão no elevador
        self.andar_atual = 0  # Andar atual do elevador

    def entrar(self, sim):
        """
        Permite que um Sim entre no elevador, se houver espaço.
        """
        if len(self.sims_no_elevador) < self.capacidade:
            self.sims_no_elevador.append(sim)  # Adiciona o Sim à lista
            print(f"{sim.tipo} {sim.id} entrou no elevador.")
        else:
            print(f"O elevador está cheio. {sim.tipo} {sim.id} não pode entrar.")

    def sair(self, sim):
        """
        Permite que um Sim saia do elevador.
        """
        if sim in self.sims_no_elevador:
            self.sims_no_elevador.remove(sim)  # Remove o Sim da lista
            print(f"{sim.tipo} {sim.id} saiu do elevador.")
        else:
            print(f"{sim.tipo} {sim.id} não está no elevador.")

    def mover_para(self, andar_destino):
        """
        Move o elevador para um andar específico.
        """
        if 0 <= andar_destino < self.andares:
            print(f"O elevador está se movendo do andar {self.andar_atual} para o andar {andar_destino}.")
            self.andar_atual = andar_destino  # Atualiza o andar atual
        else:
            print("Andar inválido. O elevador não pode se mover.")

    def listar_sims(self):
        """
        Retorna uma lista dos IDs dos Sims que estão no elevador.
        """
        return [sim.id for sim in self.sims_no_elevador]  # Retorna uma lista com os IDs dos Sims