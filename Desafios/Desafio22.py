import pygame
Ataque = False
Defesa = False
pygame.mixer.init() #Incia
Click = str(input("\033[1;36;40m Escreva click(Direito/Esquerdo) para ativar o attack:\n"))

def Attack_player(Attack, Shild):
    if Click == "Direito":
       Attack = True
       print("Ataque ativado")
      
       pygame.mixer.music.load("Punch.mp3")
       pygame.mixer.music.play()
       while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)
    elif Click == "Esquerdo":
        Shild = True
        print("Defesa ativada")
        pygame.mixer.music.load("Defesa.mp3")
        pygame.mixer.music.play()
        while True:
           if pygame.mixer.music.get_busy():
              pygame.time.Clock().tick(10)
           else:
              break
Attack_player(Ataque, Defesa)
        