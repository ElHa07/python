# Exercício Python #006 - Tocando um MP3

# Exercício: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass