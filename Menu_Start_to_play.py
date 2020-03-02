import pygame
import Game
import simple

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Game
                elif event.key == pygame.K_2:
                    simple
            font = pygame.font.Font(None, 30) # 30 отвечает за размер текста
            first_text = font.render("Добро пожаловать в GameWorld!", 1, (255, 215, 0))
            second_text = font.render("Если Вы хотите сыграть в Пакмена, нажмите '1'", 1, (255, 215, 0))
            third_text = font.render("Если хотите сыграть в Змейку, нажмите '2'", 1, (255, 215, 0))
            screen.blit(first_text, (20, 150))
            screen.blit(second_text, (20, 200))
            screen.blit(third_text, (20, 250))
        pygame.display.flip()
