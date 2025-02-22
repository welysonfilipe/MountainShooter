import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))  # Criando a Janela do Jogo
print('Setup End')

print('Loop Start')
while True:
    # Check por todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Fechar a Janela
            quit()  # Encerrar a inicialização do pygame
