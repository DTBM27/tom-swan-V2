# classes/bloco_informatica.py
from .predio import Predio
from .andar import Andar
from .elevador import Elevador

class BlocoInformacao(Predio):
    def __init__(self, nome):
        super().__init__(nome)
        self.andares = [Andar(i) for i in range(1, 3)]  # Cria 2 andares
        self.elevador = Elevador(capacidade=5, andares=2)  # Cria um elevador com capacidade para 5 Sims

    def mover_sim_entre_andares(self, sim, andar_destino):
        """
        Move um Sim entre andares, utilizando o elevador.
        """
        if len(self.elevador.sims_no_elevador) < self.elevador.capacidade:
            self.elevador.entrar(sim)  # O Sim entra no elevador
            self.elevador.mover_para(andar_destino.numero)  # O elevador se move para o andar de destino
            self.elevador.sair(sim)  # O Sim sai do elevador
            andar_destino.adicionar_sim(sim)  # O Sim é adicionado ao andar de destino
        else:
            sim.esperar()  # Se o elevador estiver cheio, o Sim espera

    def listar_andares(self):
        """
        Retorna uma lista dos números dos andares.
        """
        return [andar.numero for andar in self.andares]  # Retorna uma lista com os números dos andares