import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Dimensões da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Parâmetros do jogo
clock = pygame.time.Clock()
tamanho_cobra = 10
velocidade = 15

# Função para desenhar a cobrinha
def desenhar_cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_cobra, tamanho_cobra])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobrinha
    x1 = largura / 2
    y1 = altura / 2
    x1_mudar = 0
    y1_mudar = 0

    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0

    while not game_over:
        while game_close:
            tela.fill(preto)
            fonte = pygame.font.SysFont("comicsansms", 35)
            mensagem = fonte.render("Você perdeu! Pressione C para continuar ou Q para sair.", True, vermelho)
            tela.blit(mensagem, [largura / 6, altura / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudar = -tamanho_cobra
                    y1_mudar = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudar = tamanho_cobra
                    y1_mudar = 0
                elif evento.key == pygame.K_UP:
                    y1_mudar = -tamanho_cobra
                    x1_mudar = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudar = tamanho_cobra
                    x1_mudar = 0

        # Verifica se a cobrinha bateu nas bordas
        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True

        # Atualiza a posição da cobrinha
        x1 += x1_mudar
        y1 += y1_mudar
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        
        # Atualiza a lista da cobrinha
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica colisão com o próprio corpo
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True

        desenhar_cobra(tamanho_cobra, lista_cobra)

        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        # Controla a taxa de quadros
        clock.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
