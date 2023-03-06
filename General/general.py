import random
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('General')
timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 18)
background = (89, 92, 91)
white = (255, 255, 255)
black = (0, 0, 0)
vermelho = (255,0,0)
corb = (79,117,104)

numeros = [0,0,0,0,0] #Para não apresentar nenhum número no dado entre as jogadas
rolar = False
clicked = -1
placar_atual = 0
algo_selecionado = False

rodadas_restantes = 3

escolha_selecionada = [False, False, False, False,False, False, False, False,False, False, False, False ]
possibilidade = [False, False, False, False,False, False, False, False,False, False, False, False ]
feito = [False, False, False, False,False, False, False, False,False, False, False, False ]
placar = [0,0,0,0,0,0,0,0,0,0,0,0] 
totais = [0]
dado_selecionado = [False, False, False, False,False]


def draw_stuff():
    global rodadas_restantes
    botao_jogada_texto = font.render('Clique para jogar os dados', True, white) #Texto do botão de rolar dados
    screen.blit(botao_jogada_texto, (30,165)) #Posição do texto do botão de rolar dados
    botao_aceitar_texto = font.render('Aceitar rodada', True, white) 
    screen.blit(botao_aceitar_texto, (385,165))
    rodadas_restantes_texto = font.render('Rodadas restantes:'+str(rodadas_restantes),True, white) 
    screen.blit(rodadas_restantes_texto, (15,15))
    pygame.draw.rect(screen, (255, 255, 255), [0, 200, 225, HEIGHT - 200])
    pygame.draw.line(screen, (0, 0, 0), (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 200), 3)
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 40), 3)
    pygame.draw.line(screen, (0, 0, 0), (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, (0, 0, 0), (225, 200), (225, HEIGHT), 3)


# Classe dos Dados - define os pontinhos da numeração dos dados
class Dados:
    def __init__(self, x_pos, y_pos, numero, key):
        global dado_selecionado
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.numero = numero
        self.key = key
        self.dado = ''
        self.selecionado = dado_selecionado[key]

    def jogar(self):
        self.dado = pygame.draw.rect(
            screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.numero == 1:
            pygame.draw.circle(
                screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.numero == 2:
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.numero == 3:
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.numero == 4:
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.numero == 5:
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(
                screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.numero == 6:
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.x_pos + 80, self.y_pos + 20), 10)
        
        if self.selecionado:
            pygame.draw.rect(
            screen, vermelho, [self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.dado.collidepoint(coordinates):
            if dado_selecionado[self.key]:
                dado_selecionado[self.key] = False
            elif not dado_selecionado[self.key]:
                dado_selecionado[self.key] = True


def escolha_da_rodada(clicked_num, selected, ok_list):
    for index in range(len(selected)):
        selected[index] =  False
    if not ok_list[clicked_num]:
        selected[clicked_num] = True

    return selected
        
                    
class Opcao():
    def __init__(self, x_pos, y_pos, texto, selecao, possivel, feito, placar):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.texto = texto
        self.selecao = selecao
        self.possivel = possivel
        self.feito = feito
        self.placar = placar

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x_pos, self.y_pos + 31), (self.x_pos + 225, self.y_pos + 31), 2)

        if not self.feito:
            if self.possivel:
                meu_texto = font.render(self.texto, True, (113, 174,131))
            elif not self.possivel:
                meu_texto = font.render(self.texto, True, (255,0,0))
        else:
            meu_texto =  font.render(self.texto, True, black )
        if self.selecao:
            pygame.draw.rect(screen,(20,35,30),[self.x_pos,self.y_pos,155,30])
        screen.blit(meu_texto,(self.x_pos,self.y_pos + 10 ))
        placar_texto =  font.render(str(self.placar), True, (0,0,255))
        screen.blit(placar_texto,(self.x_pos +165 ,self.y_pos + 10 ))


def check_possibilidade(possibilidades_lista,numeros_lista):
    possibilidades_lista[0] = True
    possibilidades_lista[1] = True
    possibilidades_lista[2] = True
    possibilidades_lista[3] = True
    possibilidades_lista[4] = True
    possibilidades_lista[11] = True
    max_count = 0

    for index in range(1,7):
        if numeros_lista.count(index) > max_count:
            max_count = numeros_lista.count(index)


    if max_count >= 3:
        possibilidades_lista[6] = True #Trinca é possível
        if max_count >4:
            possibilidades_lista[7] = True
            if max_count >= 5:
                possibilidades_lista[11] = True
        
    if max_count < 3:
        possibilidades_lista[6] = False #Trinca é impossível
        possibilidades_lista[7] = False #Quadra é impossível
        possibilidades_lista[10] = False #Full House é impossível
        possibilidades_lista[11] = False #General é impossível
    elif max_count == 3:
        possibilidades_lista[7] = False #Quadra é impossível
        possibilidades_lista[11] = False #General é impossível
        checker = False # Checando se há Full House
        for index in range(len(numeros_lista)):
            if numeros_lista.count(numeros_lista[index]) == 2: #Passa pelos números para ver se os dois restantes sao iguais pra formar Full House
                possibilidades_lista[10] = True #Full House
                checker = True
        if not checker:
            possibilidades_lista[10] = False #Não é Full House

    elif max_count == 4:
        possibilidades_lista[11] = False #General é impossível

#Checando sequencia
    menor_valor = 10
    maior_valor = 0

    for index in range(len(numeros_lista)):
        if numeros_lista[index] < menor_valor:
            menor_valor = numeros_lista[index]
        if numeros_lista[index] < maior_valor:
            maior_valor = numeros_lista[index]

    if (menor_valor + 1 in numeros_lista) and (menor_valor + 2 in numeros_lista) and (menor_valor + 3 in numeros_lista) and (menor_valor + 4 in numeros_lista) :
        possibilidades_lista[9] = True
    else: 
        possibilidades_lista[9] = False
    
    if (maior_valor - 1 in numeros_lista) and (maior_valor - 2 in numeros_lista) and (maior_valor - 3 in numeros_lista) and (maior_valor - 4 in numeros_lista) :
        possibilidades_lista[8] = True
    else: 
        possibilidades_lista[8] = False
    
    return possibilidades_lista

def check_score(escolha_lista, numeros_lista, pos_lista, pontos):
    active = 0
    for index in range(len(escolha_lista)):
        if escolha_lista[index]:
            active = index
        if active == 0:
            pontos = numeros_lista.count(1)
        elif active == 1:
            pontos = numeros_lista.count(2)
        elif active == 2:
            pontos = numeros_lista.count(3)
        elif active == 3:
            pontos = numeros_lista.count(4)
        elif active == 4:
            pontos = numeros_lista.count(5)
        elif active == 5:
            pontos = numeros_lista.count(6)
        elif active == 6:
            pontos = 30
        elif active == 7:
            pontos = 40
        elif active == 8 or active ==9:
            if pos_lista[active]:
                pontos = 25
            else:
                pontos = 0
        elif active == 10:
            if pos_lista[active]:
                pontos = 50
        elif active == 11:
            if pos_lista[active]:
                pontos = 60
    return pontos



#########################################################################################################################
running = True
while running:
    timer.tick(fps)
    screen.fill((background))
    botao_jogada = pygame.draw.rect(screen, corb, [10,160,280,30]) #Desenhando botão de rolar dados
    botao_aceitar = pygame.draw.rect(screen, corb, [310,160,280,30]) #Desenhando botão de rolar dados

    draw_stuff()

    #sqe_men_teste = [1,2,3,4,5]
    #sqe_maiteste = [2,3,4,5,6]

    #Dados e posição na tela
    dado1 = Dados(10,50,numeros[0],0)
    dado2 = Dados(130,50,numeros[1],1)
    dado3 = Dados(250,50,numeros[2],2)
    dado4 = Dados(370,50,numeros[3],3)
    dado5 = Dados(490,50,numeros[4],4)


    #Lista da pontuação
    um = Opcao(0,200,'1s', escolha_selecionada[0],possibilidade[0],feito[0], placar[0])
    dois = Opcao(0,230,'2s', escolha_selecionada[1],possibilidade[1],feito[1], placar[1])
    tres = Opcao(0,260,'3s', escolha_selecionada[2],possibilidade[2],feito[2], placar[2])
    quatro = Opcao(0,290,'4s', escolha_selecionada[3],possibilidade[3],feito[3], placar[3])
    cinco = Opcao(0,320,'5s', escolha_selecionada[4],possibilidade[4],feito[4], placar[4])
    seis = Opcao(0,350,'6s', escolha_selecionada[5],possibilidade[5],feito[5], placar[5])
    trinca = Opcao(0,380,'Trinca', escolha_selecionada[6],possibilidade[6],feito[6], placar[6])
    quadra = Opcao(0,410,'Quadra', escolha_selecionada[7],possibilidade[7],feito[7], placar[7])
    sequencia_menor = Opcao(0,440,'Sequencia -', escolha_selecionada[8],possibilidade[8],feito[8], placar[8])
    sequencia_maior = Opcao(0,470,'Sequencia +', escolha_selecionada[9],possibilidade[9],feito[9], placar[9])
    full_house = Opcao(0,500,'Full House', escolha_selecionada[10],possibilidade[10],feito[10], placar[10])
    general = Opcao(0,530,'General', escolha_selecionada[11],possibilidade[11],feito[11], placar[11])

    total = Opcao(0,560,'Total', False,False,True,totais[0])

    possibilidades = check_possibilidade(possibilidade, numeros)

    placar_atual = check_score(escolha_selecionada, numeros, possibilidade, placar)
    if True in escolha_selecionada:
        algo_selecionado = True

#Chama objetos pro jogo 
    dado1.jogar()
    dado2.jogar()
    dado3.jogar()
    dado4.jogar()
    dado5.jogar()
    um.draw()
    dois.draw()
    tres.draw()
    quatro.draw()
    cinco.draw()
    seis.draw()
    sequencia_menor.draw()
    sequencia_maior.draw()
    trinca.draw()
    quadra.draw()
    full_house.draw()
    general.draw()
    total.draw()
    

####################################################################################### LOOP DO JOGO

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN: #Configura clique no botão
            dado1.check_click(event.pos)
            dado2.check_click(event.pos)
            dado3.check_click(event.pos)
            dado4.check_click(event.pos)
            dado5.check_click(event.pos)

    # Posição para clique das escolhas no placar
            if 200 < event.pos[1] < 230:
                clicked = 0
            elif 230 < event.pos[1] < 260:
                clicked = 1
            elif 260 < event.pos[1] < 290:
                clicked = 2
            elif 290 < event.pos[1] < 320:
                clicked = 3
            elif 320 < event.pos[1] < 350:
                clicked = 4
            elif 350 < event.pos[1] < 380:
                clicked = 5
            elif 380 < event.pos[1] < 410:
                clicked = 6
            elif 410 < event.pos[1] < 440:
                clicked = 7
            elif 440 < event.pos[1] < 470:
                clicked = 8
            elif 470 < event.pos[1] < 500:
                clicked = 9
            elif 500 < event.pos[1] < 530:
                clicked = 10
            elif 530 < event.pos[1] < 560:
                clicked = 11
                            
            escolha_selecionada = escolha_da_rodada(clicked, escolha_selecionada, feito) 
                        

            if botao_jogada.collidepoint(event.pos) and rodadas_restantes > 0:
                rolar = True
                rodadas_restantes = rodadas_restantes -1 

            if botao_aceitar.collidepoint(event.pos) and algo_selecionado and rodadas_restantes < 3:
                for i in range(len(escolha_selecionada)):
                    if escolha_selecionada[1]:
                        feito[i] = True
                        placar[i] = placar_atual
                        escolha_selecionada[i] = False
                for i in range(len(dado_selecionado)):
                    dado_selecionado[1] = False
                    numeros = [7,18,29,30,41]
                    algo_selecionado = False    


    if rolar:
        for numero in range(len(numeros)):
            if not dado_selecionado[numero]:
                numeros[numero] = random.randint(1,6) #Aleatoriza número dos dados
        rolar = False


    pygame.display.flip()
pygame.quit()
