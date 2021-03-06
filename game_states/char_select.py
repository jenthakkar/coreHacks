# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # Character select state
    def chooseChar(self):
        # Create game state
        while True:
            self.state = "choose"
            # Create interface
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/choose.png")), (self.height, self.width))
            self.screen.blit(image, (0,0))
            # Blit buttons onto interface
            for s in self.char_buttons:
                self.screen.blit(s.image, s.rect.topleft)
                pygame.display.flip()
            # Select screen logic
            mouseLocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.girl_button.rect.collidepoint(mouseLocation):
                        self.pick = 'jenny'
                        self.spawnRoom(640, 400)
                        return None
                    elif self.boy_button.rect.collidepoint(mouseLocation):
                        self.pick = 'alex'
                        self.spawnRoom(640, 400)
                        return None
