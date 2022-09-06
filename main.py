# Date : 06/07/2022
# Auteur : Macé Nicolas (Mace Robotics)
# Version : 1.0
# Date derniere modification : 29/08/22


import pygame
import time
import mcp3008


try:
  # init convertisseur MCP3008
  adc = mcp3008.MCP3008()
except:
  print("Erreur init MCP3008")


# init pygame
pygame.init()

# init mixer
pygame.mixer.init()
 
pygame.mixer.set_num_channels(6)

sound_1 = pygame.mixer.Sound("/home/pi/Mixette/music1.mp3")
sound_2 = pygame.mixer.Sound("/home/pi/Mixette/music2.mp3")
sound_3 = pygame.mixer.Sound("/home/pi/Mixette/music3.mp3")
sound_4 = pygame.mixer.Sound("/home/pi/Mixette/music4.mp3")
sound_5 = pygame.mixer.Sound("/home/pi/Mixette/music5.mp3")
sound_6 = pygame.mixer.Sound("/home/pi/Mixette/music6.mp3")


canal_1 = pygame.mixer.Channel(0)
canal_2 = pygame.mixer.Channel(1)
canal_3 = pygame.mixer.Channel(2)
canal_4 = pygame.mixer.Channel(3)
canal_5 = pygame.mixer.Channel(4)
canal_6 = pygame.mixer.Channel(5)

# -1 , permet lire en boucle
canal_1.play(sound_1, -1)
canal_2.play(sound_2, -1)
canal_3.play(sound_3, -1)
canal_4.play(sound_4, -1)
canal_5.play(sound_5, -1)
canal_6.play(sound_6, -1)

print("Début lecture")

while True:
    potar1 = (adc._read_single(mcp3008.CH0))# lecture potentiometre CH0
    potar2 = (adc._read_single(mcp3008.CH1))# lecture potentiometre CH1
    potar3 = (adc._read_single(mcp3008.CH2))
    potar4 = (adc._read_single(mcp3008.CH3))
    potar5 = (adc._read_single(mcp3008.CH5))
    potar6 = (adc._read_single(mcp3008.CH7))
    canal_1.set_volume(potar1) # gestion du volume
    canal_2.set_volume(potar2)
    canal_3.set_volume(potar3)
    canal_4.set_volume(potar4)
    canal_5.set_volume(potar5)
    canal_6.set_volume(potar6)
print("Fin programme")

# end file
