from abc import ABC, abstractmethod

# Interface para Partida
class Partida(ABC):
    @abstractmethod
    def iniciar(self, jogadores):
        pass

# Implementações específicas de tipos de Partida
class PartidaCasual(Partida):
    def iniciar(self, jogadores):
        print("Iniciando partida casual com jogadores:", [j.nome for j in jogadores])

class PartidaCompetitiva(Partida):
    def iniciar(self, jogadores):
        print("Iniciando partida competitiva com jogadores:", [j.nome for j in jogadores])

class PartidaCooperativa(Partida):
    def iniciar(self, jogadores):
        print("Iniciando partida cooperativa com jogadores:", [j.nome for j in jogadores])

# Classe para representar um jogador
class Jogador:
    def _init_(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

# Gerenciador de Partidas que segue o OCP, criando instâncias de partidas
class FabricaDePartidas:
    def criar_partida(self, tipo: str) -> Partida:
        if tipo == "casual":
            return PartidaCasual()
        elif tipo == "competitiva":
            return PartidaCompetitiva()
        elif tipo == "coop":
            return PartidaCooperativa()
        else:
            raise ValueError("Tipo de partida inválido.")

# Classe Lobby para organizar jogadores e iniciar partidas
class Lobby:
    def _init_(self, fabrica_partidas: FabricaDePartidas):
        self.jogadores = []
        self.partida = None
        self.fabrica_partidas = fabrica_partidas

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def criar_partida(self, tipo: str):
        self.partida = self.fabrica_partidas.criar_partida(tipo)
        print(f"Partida do tipo {tipo} criada.")

    def iniciar_partida(self):
        if self.partida is not None:
            self.partida.iniciar(self.jogadores)
        else:
            print("Nenhuma partida foi criada.")