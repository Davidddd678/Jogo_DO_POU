class Jogador:
    x = 0
    y = 0
    velocidade = 8
    pontos = 0
    save = None
    def __init__(self, x, y, IA):
        self.x = x
        self.y = y
        self.IA = IA

        arquivo = open(IA, "r")
        self.pontos = int(arquivo.read())  # Lê o conteúdo do arquivo para uma variável
        arquivo.close()
    def salvarpontos(self, novoponto):
        arquivo = open(self.IA,"w")
        arquivo.write(str(novoponto))
        arquivo.close()
class Bola:
    x = 0
    y = 0
    velocidade = 1
    primeira_vez = 1
    raio = 10
    factor_x = 1
    factor_y = 1
    screen = None

    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.raio = 10
        self.velocidade = 4
        self.factor_x = 1
        self.factor_y = 1
        self.width, self.height = screen.get_size()

    def update(self, player_1, player_2):
        self.x += self.velocidade * self.factor_x
        self.y += self.velocidade * self.factor_y

        # Colisão com o topo/fundo do ecrã
        if self.y - self.raio <= 0 or self.y + self.raio >= self.height:
            self.factor_y *= -1

        # Collision com Jogador 1
        if (player_1.x < self.x < player_1.x + 30 and
                player_1.y < self.y < player_1.y + 100):
            self.factor_x = 1  # Bounce right

        # Collision com Jogador 2
        if (player_2.x < self.x < player_2.x + 30 and
                player_2.y < self.y < player_2.y + 100):
            self.factor_x = -1  # Bounce left

        # Bola fora do limite do ecrã
        if self.x < 0 or self.x > self.width:
            if self.x < 0:
                player_2.pontos = player_2.pontos + 1
                player_2.salvarpontos(player_2.pontos)
            if self.x > 800:
                player_1.pontos = player_1.pontos + 1
                player_1.salvarpontos(player_1.pontos)
            self.reset()

    def reset(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.factor_x *= -1
        self.factor_y *= -1
        self.velocidade = 1
