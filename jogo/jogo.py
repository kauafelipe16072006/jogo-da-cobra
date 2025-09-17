import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jogo Cobrinha")

fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 72)

def desenhar(cobra, comida, pontos):
    tela.fill((0, 0, 0))

    for parte in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (parte[0], parte[1], 10, 10))

    pygame.draw.rect(tela, (255, 0, 0), (*comida, 10, 10))

    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    pygame.display.update()

def mostrar_menu_inicial():
    tela.fill((0, 0, 0))

    titulo = fonte_titulo.render("JOGO COBRINHA", True, (0, 255, 0))
    instrucoes1 = fonte.render("Pressione ENTER para jogar", True, (255, 255, 255))
    instrucoes2 = fonte.render("Pressione ESC para sair", True, (255, 255, 255))

    tela.blit(titulo, (100, 100))
    tela.blit(instrucoes1, (150, 200))
    tela.blit(instrucoes2, (170, 250))

    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def mostrar_game_over(pontos):
    tela.fill((0, 0, 0))

    texto = fonte_titulo.render("GAME OVER", True, (255, 0, 0))
    texto_pontos = fonte.render(f"Pontuação final: {pontos}", True, (255, 255, 255))
    texto_instrucao = fonte.render("qualquer tecla para voltar ao menu", True, (200, 200, 200))

    tela.blit(texto, (150, 100))
    tela.blit(texto_pontos, (180, 200))
    tela.blit(texto_instrucao, (60, 260))

    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

def jogar():
    cobra = [(100, 50)]
    direcao = (10, 0)
    comida = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
    pontos = 0

    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != (0, 10):
                    direcao = (0, -10)
                elif evento.key == pygame.K_DOWN and direcao != (0, -10):
                    direcao = (0, 10)
                elif evento.key == pygame.K_LEFT and direcao != (10, 0):
                    direcao = (-10, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-10, 0):
                    direcao = (10, 0)

        nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
        cobra.insert(0, nova_cabeca)

        if nova_cabeca == comida:
            comida = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
            pontos += 1
        else:
            cobra.pop()

        if nova_cabeca in cobra[1:] or \
           nova_cabeca[0] < 0 or nova_cabeca[0] >= 600 or \
           nova_cabeca[1] < 0 or nova_cabeca[1] >= 400:
            rodando = False

        desenhar(cobra, comida, pontos)
        relogio.tick(10)

    mostrar_game_over(pontos)

# Loop principal com menu + jogo
while True:
    mostrar_menu_inicial()
    jogar()
