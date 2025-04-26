import pygame
import sys


import classes
meu_pou = classes.Pou(50,50, "nome",51,50,50, 50)


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo do POU")

# Cores
BRANCO = (255, 255, 255)
AZUL = (100, 100, 255)
AZUL_MOUSE = (150, 150, 255)

cena = "MENU"

# carrega as imagens e coloca numa varíavel
image = pygame.image.load('pou.png')
image1 = pygame.image.load('mortopou.png')
casado = pygame.image.load("POU casado.png")
logo = pygame.image.load('Menu.imagem.png')
image2 = pygame.image.load('um-quarto-lindamente-decorado-apresentando-uma-mistura-de-design-de-interiores-moderno-e-aconchegante.png')

image_rect = image.get_rect(center=(400, 200))
tamanho_fundo = (800, 600)
image2 = pygame.transform.scale(image2, tamanho_fundo)

tamanho_logo = (800, 600)
logo = pygame.transform.scale(logo, tamanho_logo)

#onde vão ficar os botões no fundo
# os parametros são esquerda,topo,largura e altura, respetivamente
Carinho = pygame.Rect(300, 400, 150, 50)
Alimentar = pygame.Rect(300, 480, 150, 50)
Brainrot = pygame.Rect(100, 400, 150, 50)
Brincar = pygame.Rect(100, 480, 150, 50)
Banho = pygame.Rect(300, 550, 150, 50)
Rebelde = pygame.Rect(550, 400, 150, 50)
Amor = pygame.Rect(550, 480, 150, 50)
Jogar = pygame.Rect(300, 400, 200, 50)


#métodos quer ocorrem quando o botão é clicado
def Carinho_clicked():
    meu_pou.coracao()
    meu_pou.limites()
    meu_pou.perda()



def Alimentar_clicked():
    meu_pou.alimentar()
    meu_pou.limites()
    meu_pou.perda()

def Brainrot_clicked():
    meu_pou.brainrot()
    print("Parabéns!! Destruis-te a mente do teu pou!!!!!")


def Brincar_clicked():
    meu_pou.brincar()
    meu_pou.limites()
    meu_pou.perda()

def Banho_clicked():
    meu_pou.banho()
    meu_pou.limites()
    meu_pou.perda()


def Rebelde_clicked():
    meu_pou.miudodagangue()
    meu_pou.limites()
    meu_pou.perda()



def Amor_clicked():
    meu_pou.amorverdadeiro()
    meu_pou.limites()
    meu_pou.perda()

def Jogar_clicked():
    print(" Então vamos começar o jogo!!!")





running = True
while running:
    screen.fill(BRANCO)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if cena == "JOGO": # faz com que tudo o que está la inserido só aconteça quando cena == JOGO
                    if Carinho.collidepoint(event.pos):
                        Carinho_clicked()
                    if Alimentar.collidepoint(event.pos):
                        Alimentar_clicked()
                    if Brainrot.collidepoint(event.pos):
                        Brainrot_clicked()
                    if Brincar.collidepoint(event.pos):
                        Brincar_clicked()
                    if Rebelde.collidepoint(event.pos):
                        Rebelde_clicked()
                    if Amor.collidepoint(event.pos):
                        Amor_clicked()
                    if Banho.collidepoint(event.pos):
                        Banho_clicked()

                if cena == "MENU": # faz com que tudo o que está la inserido só aconteça quando cena == MENU
                    if Jogar.collidepoint(event.pos):
                        Jogar_clicked()
                        cena = "JOGO"

    mouse_pos = pygame.mouse.get_pos()




    font = pygame.font.SysFont('Arial', 30)# Customiza os botoes
    text1 = font.render("Carinho", True, (255, 255, 255))
    text2 = font.render("Alimentar", True, (255, 255, 255))
    text3 = font.render("Brainrot", True, (255, 255, 255))
    text4 = font.render("Brincar", True, (255, 255, 255))
    text5 = font.render("Rebelde", True, (255, 255, 255))
    text6 = font.render("Amor", True, (255, 255, 255))
    text7 = font.render("Banho", True, (255, 255, 255))
    text = font.render("Jogar", True, (255, 255, 255))





    texto_pou = font.render(f" Brincar {meu_pou.felicidade}     Níveldefome:  {meu_pou.niveldefome}  Sujidade:  {meu_pou.sujidade}  " , False, (0,0,0,))
    texto_pou1 = font.render(f"Carinho:     {meu_pou.carinho} Rebelde:  {meu_pou.rebeldia} Amor:  {meu_pou.amor}", False, (0,0,0))

    texto_pou2 = font.render("DAVID MARQUES, O CRIADOR", True, (0,0,0))

    if cena == "MENU":
        screen.blit(texto_pou2, (100, 300))
        screen.blit(logo, (0, 0))

        if Jogar.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Jogar)
        else:
            pygame.draw.rect(screen, AZUL, Jogar)

        screen.blit(text, (Jogar.centerx - text.get_width() // 2, Jogar.centery - text.get_height() // 2))






    elif cena == "JOGO":
        screen.blit(image2, (0, 0))
        if meu_pou.amor > 50:
            screen.blit(casado, image_rect)
        else:
            screen.blit(image, image_rect)
        if Carinho.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Carinho)
        else:
            pygame.draw.rect(screen, AZUL, Carinho)

        if Alimentar.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Alimentar)
        else:
            pygame.draw.rect(screen, AZUL, Alimentar)

        if Brainrot.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Brainrot)
        else:
            pygame.draw.rect(screen, AZUL, Brainrot)

        if Brincar.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Brincar)
        else:
            pygame.draw.rect(screen, AZUL, Brincar)

        if Rebelde.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Rebelde)
        else:
            pygame.draw.rect(screen, AZUL, Rebelde)

        if Amor.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Amor)
        else:
            pygame.draw.rect(screen, AZUL, Amor)

        if Banho.collidepoint(mouse_pos):
            pygame.draw.rect(screen, AZUL_MOUSE, Banho)
        else:
            pygame.draw.rect(screen, AZUL, Banho)

        screen.blit(text1, (Carinho.centerx - text1.get_width() // 2, Carinho.centery - text1.get_height() // 2))
        screen.blit(text2, (Alimentar.centerx - text2.get_width() // 2, Alimentar.centery - text2.get_height() // 2))
        screen.blit(text3, (Brainrot.centerx - text3.get_width() // 2, Brainrot.centery - text3.get_height() // 2))
        screen.blit(text4, (Brincar.centerx - text4.get_width() // 2, Brincar.centery - text4.get_height() // 2))
        screen.blit(text5, (Rebelde.centerx - text5.get_width() // 2, Rebelde.centery - text5.get_height() // 2))
        screen.blit(text6, (Amor.centerx - text6.get_width() // 2, Amor.centery - text6.get_height() // 2))
        screen.blit(text7, (Banho.centerx - text6.get_width() // 2, Banho.centery - text7.get_height() // 2))
        screen.blit(texto_pou, (0, 0))
        screen.blit(texto_pou1, (0, 50))


    pygame.display.flip()


pygame.quit()
sys.exit()