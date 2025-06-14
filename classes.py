import pygame
import sys
import time

class Criatura:

    def __init__(self,nome):
        self.nome = nome
        self.felicidade1 = 0
        self.fome1 = 0
        self.sujidade1 = 0
        self.odio = 50
        self.lista = [self.felicidade1, self.fome1, self.sujidade1, self.ódio]


    def alimentar1(self):
        self.alimentar1 -= 5

    def carinho1(self):
        self.carinho1 += 20

    def sujidade1(self):
        self.sujidade1 += 50

    def odio(self):
        self.ódio += 20

class Pou(Criatura):
    def __init__(self, nome):
        super().__init__(nome)
class Pou:
# faz com que cada vez que um pou seja criado o "init" aconteça
    def __init__(self, niveldefome, felicidade, nome, sujidade, rebeldia, carinho,amor):
        self.nome = nome
        self.niveldefome = int(niveldefome)
        self.felicidade = int(felicidade)
        self.sujidade = int(sujidade)
        self.rebeldia = int(rebeldia)
        self.carinho = int(carinho)
        self.amor = int(amor)

    def perda(self):
        if self.niveldefome >= 100:
            print("O teu pou está a morrer de fome, LITERALMENTE!!!")
            pygame.time.delay(1000)
            print("Ele morreu de fome")
            pygame.quit()
            sys.exit()
        if self.niveldefome <= 0:
            print("O teu pou ESTÁ CHEIO!!!")
            pygame.time.delay(1000)
            print("Ele morreu de comer")
            pygame.quit()
            sys.exit()
        if self.felicidade >= 100:
            print("O teu pou está demasiado feliz, ELE DEITOU VÔMITO ARCO-ÍRIS")
            pygame.time.delay(1000)
            print("Ele morreu de felicidade")
            pygame.quit()
            sys.exit()
        if self.felicidade <= 0:
            print("Ele precisa de amigos ")
            pygame.time.delay(1000)
            print("Ele morreu de tédio")
            pygame.quit()
            sys.exit()
        if self.sujidade >= 100:
            print("Ele está demasiado limpo para uma criatura como ele!!!")
            pygame.time.delay(1000)
            print("Ele morreu de lindez")
            pygame.quit()
            sys.exit()
        if self.sujidade <= 0:
            print("Ele precisa de tomar banho rapidamente !!!")
            pygame.time.delay(1000)
            print("Ele morreu de sujidade")
            pygame.quit()
            sys.exit()
        if self.rebeldia >= 100:
            print("Ele está muito rebelde!")
            pygame.time.delay(1000)
            print("Ele morreu num tiroteio de forma suja")
            pygame.quit()
            sys.exit()
        if self.rebeldia <= 0:
            print("Ele precisa de rebeldia!!!")
            pygame.time.delay(1000)
            print("Ele morreu de falta de rebeldia")
            pygame.quit()
            sys.exit()
        if self.carinho >= 100:
            print("Ele têm demasiado carinho acumulado!!!!")
            pygame.time.delay(1000)
            print("Ele morreu de carinho")
            pygame.quit()
            sys.exit()
        if self.carinho <= 0:
            print("Ele precisa de algum carinho!!!")
            pygame.time.delay(1000)
            print("Ele morreu por falta de carinho")
            pygame.quit()
            sys.exit()
        if self.amor >= 100:
            print("Ele têm demasiado amores !!!")
            pygame.time.delay(1000)
            print("Ele morreu 'pelo amor'")
            pygame.quit()
            sys.exit()
        if self.amor <= 0:
            print("Ele precisa de algum amor !!!")
            pygame.time.delay(1000)
            print("Ele morreu por falta de amor")
            pygame.quit()
            sys.exit()

    def limites(self):#faz com que as variáveis não consigam subir de 100 e descer de 0
        if self.niveldefome < 0:
            self.niveldefome = 0
        elif self.niveldefome > 100:
            self.niveldefome = 100
        if self.felicidade < 0:
            self.felicidade = 0
        elif self.felicidade > 100:
            self.felicidade = 100
        if self.sujidade < 0:
            self.sujidade = 0
        elif self.sujidade > 100:
            self.sujidade= 100
        if self.rebeldia < 0:
            self.rebeldia = 0
        elif self.rebeldia > 100:
            self.rebeldia = 100
        if self.carinho < 0:
            self.carinho = 0
        elif self.carinho > 100:
            self.carinho = 100
        if self.amor < 0:
            self.amor = 0
        elif self.amor > 100:
            self.amor = 100


    def alimentar(self):
        if self.niveldefome > 0:
            self.niveldefome -= 10
        if self.sujidade < 100:
            self.sujidade += 5
        if self.felicidade < 100:
            self.felicidade += 5
        if self.rebeldia < 100:
            self.rebeldia -= 5
        if self.carinho < 100:
            self.carinho -= 5
        if self.amor < 100:
            self.amor -= 5
            print("Alimentaste o Teu pou!")



    def banho(self):
        if self.sujidade > 0:
            self.sujidade -= 50
        if self.niveldefome < 100:
            self.niveldefome += 5
        if self.felicidade < 100:
            self.felicidade -= 5
        if self.rebeldia < 100:
            self.rebeldia -= 5
        if self.carinho < 100:
            self.carinho -= 5
        if self.amor < 100:
            self.amor -= 5
            print("O teu pou tomou banho!")

    def brincar(self):
        if self.felicidade > 0:
            self.felicidade += 20
            if self.niveldefome < 100:
                self.niveldefome += 5
            if self.sujidade < 100:
                self.sujidade -= 5
            if self.rebeldia < 100:
                self.rebeldia -= 15
            if self.carinho < 100:
                self.carinho += 5
            if self.amor < 100:
                self.amor += 5
            print("O teu pou brincou")


    def miudodagangue(self):
        if self.rebeldia > 0:
            self.rebeldia += 25
            if self.niveldefome < 100:
                self.niveldefome += 5
            if self.sujidade < 100:
                self.sujidade += 5
            if self.felicidade < 100:
                self.felicidade -= 5
            if self.carinho < 100:
                self.carinho -= 5
            if self.amor < 100:
                self.amor -= 5
            print("O teu pou foi rebelde")




    def coracao(self):
        if self.carinho > 0:
            self.carinho += 20
            if self.niveldefome < 100:
                self.niveldefome += 5
            if self.sujidade < 100:
                self.sujidade -= 5
            if self.felicidade < 100:
                self.felicidade += 10
            if self.rebeldia < 100:
                self.rebeldia -= 5
            if self.amor < 100:
                self.amor += 5
            print ("O pou recebeu carinho")

    def brainrot(self):
        print(
            "Only in ohio "" IM HIM "" Are you skibidi "" IMAGINE IF NINJA GOT A LOWWWWWWWW TAPERRRRRRRR FADEEEEEEEEEE "" Eye of rah "" I buyed a proprety in Egypt and what they do for you is they give you the proprety "" If he doesn´t hawk tuah i don´t talk tuah "" MANGO MANGO MANGO"" Artist you can sing VS Artists who can´t sing"" Do you have any relationships whit your father.  What´s that,  What´s a father?" " No my hotspot" " We just got 8 free pizzas" " I knew that door had a lock on it and everbody made me think I was losing my mind!")

    def amorverdadeiro(self):
        if self.amor > 0:
            self.amor += 20
            if self.niveldefome < 100:
                self.niveldefome += 5
            if self.sujidade < 100:
                self.sujidade -= 5
            if self.felicidade < 100:
                self.felicidade += 10
            if self.rebeldia < 100:
                self.rebeldia -= 15
            if self.carinho < 100:
                self.carinho += 5
            print(" O teu pou recebeu amor")

    def jogar(self):
        ()
    def Pong(self):
        ()
    def Voltar(self):
        ()
    def IA(self):
        ()
    def Humanos(self):
        ()

    def stats(self):
        print(f"Felicidade: {self.felicidade}")
        print(f"nivel de fome: {self.niveldefome}")
        print(f"sujidade: {self.sujidade}")
        print(f"rebeldia: {self.rebeldia}")
        print(f"carinho: {self.carinho}")
        print(f"amor: {self.amor}")




