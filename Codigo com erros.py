class JogoOnline:
    def _init_(self):
        self.jogadores = []
        self.tipo_partida = None

    # Adiciona um jogador ao jogo
    def adicionar_jogador(self, nome, nivel):
        jogador = {"nome": nome, "nivel": nivel}
        self.jogadores.append(jogador)

    # Cria uma partida com base no tipo
    def criar_partida(self, tipo):
        self.tipo_partida = tipo
        if tipo == "casual":
            print("Partida Casual criada.")
        elif tipo == "competitiva":
            print("Partida Competitiva criada.")
        elif tipo == "coop":
            print("Partida Cooperativa criada.")
    
    # Inicia a partida com base no tipo
    def iniciar_partida(self):
        if self.tipo_partida == "casual":
            print("Iniciando partida casual com jogadores:", [j["nome"] for j in self.jogadores])
        elif self.tipo_partida == "competitiva":
            print("Iniciando partida competitiva com jogadores:", [j["nome"] for j in self.jogadores])
        elif self.tipo_partida == "coop":
            print("Iniciando partida cooperativa com jogadores:", [j["nome"] for j in self.jogadores])