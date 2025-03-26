import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.Font(None, FONT_SIZE)

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "you win 🥌📃✂"
    else:
        return "you lose 🥌📃✂"


def main():
    clock = pygame.time.Clock()
    running = True
    player_choice = None
    computer_choice = None
    result = ""

    while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            player_choice = "rock"
                        elif event.key == pygame.K_p:
                            player_choice = "paper"
                        elif event.key == pygame.K_s:
                            player_choice = "scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            player_choice = "rock"
                    elif event.key == pygame.K_p:
                            player_choice = "paper"
                    elif event.key == pygame.K_s:
                            player_choice = "scissors"
    screen.fill(WHITE)

    if player_choice:
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)
                    player_text = font.render(f"Player: {player_choice}", True, BLACK)
                    screen.blit(player_text, (20, 100))
                    computer_text = font.render(f"Computer: {computer_choice}", True, BLACK)
                    screen.blit(computer_text, (20, 150))
                    result_text = font.render(result, True, BLACK)
                    screen.blit(result_text, (20, 200))

                
                    pygame.display.flip()
    
    clock.tick(FPS)



    pygame.quit()

    if __name__=="__main__":
         main()