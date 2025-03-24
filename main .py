import pygame
import random

pygame.init()

WIDTH,HEIGHT=600,400
FPS=30
white=(255,255,255)
black=(0,0,0)
fs=36


screen=pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Rock Paper Scissors")


font = pygame.font.Font(None,fs)

choices = ["rock","paper","scissors"]

def get_winner(player,computer)
    if player == computer:
        return "draw"
    elif (player=="rock" and computer=="scissors")or/
        (player=="paper"and computer== "rock")or/
        (player=="scissor"and computer== "paper")or/:
        return "you win 🥌📃✂"
    else:
        return "you lose 🥌📃✂"


