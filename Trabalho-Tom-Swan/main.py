import random
import time
import json
import socket
from classes.sim import Sim
from classes.predio import Predio
from classes.andar import Andar
from classes.elevador import Elevador
from classes.bloco_informatica import BlocoInformacao

class Simulacao:
    def __init__(self):
        self.sims = []
        self.predios = [
            Predio("Centro de Vivência"),
            Predio("Refeitório"),
            BlocoInformacao("Bloco de Informática")
        ]
        self.elevador = Elevador(capacidade=5, andares=len(self.predios))
        self.universo_id = "meu_universo"  # ID do universo de origem
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Criar o socket
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Permitir broadcast
        self.udp_socket.bind(('', 12345))  # Porta para escu
    def criar_sim(self, id):
        tipo = random.choice(["Aluno", "Servidor"])
        sim = Sim(id, tipo)
        self.sims.append(sim)
        return sim

    def enviar_sims(self):
        for sim in self.sims:
            dados = {"id": sim.id, "tipo": sim.tipo, "universo_id": self.universo_id}
            mensagem = json.dumps(dados).encode('utf-8')
            self.udp_socket.sendto(mensagem, ('<broadcast>', 12345))
            print(f"Sim {sim.id} enviado para a rede.")


    def receber_sims(self):
        # Recebe Sims de um arquivo JSON
        while True:
            mensagem, endereco = self.udp_socket.recvfrom(1024)  # Tamanho do buffer
            dados = json.loads(mensagem.decode('utf-8'))
            for sim_data in dados:
                sim = Sim(sim_data['id'], sim_data['tipo'])
                self.sims.append(sim)
                print(f"Recebido Sim: {sim.id}, Tipo: {sim.tipo} de {endereco}")

    def iniciar(self):
        import threading
        threading.Thread(target=self.receber_sims, daemon=True).start()


        while True:
            sim_id = len(self.sims) + 1
            novo_sim = self.criar_sim(sim_id)
            predio_destino = random.choice(self.predios)
            predio_destino.adicionar_sim(novo_sim)

            # Lógica para interação com o elevador
            if len(self.elevador.sims_no_elevador) < self.elevador.capacidade:
                novo_sim.esperar()
                self.elevador.entrar(novo_sim)
                andar_destino = random.randint(0, self.elevador.andares - 1)
                self.elevador.mover_para(andar_destino)
                self.elevador.sair(novo_sim)

            self.enviar_sims()

            time.sleep(1)  # Pausa para simular o tempo entre as ações

if __name__ == "__main__":
    simulacao = Simulacao()
    simulacao.iniciar()
