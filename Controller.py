import time, pygame, os, buttons, char, sys

class Controller:
  def __init__(self, height = 1280, width=800):
    self.state = "start";
    self.height = height;
    self.width = width;
    self.screen = pygame.display.set_mode((self.height, self.width));
    self.char_buttons = pygame.sprite.Group()
    self.start_buttons = pygame.sprite.Group()
    self.startButton = buttons.Button('startButton', (220, 450), "startButton.png")
    self.quitButton = buttons.Button('helpButton', (700, 450), "quitButton.png")
    self.start_buttons.add(self.startButton)
    self.start_buttons.add(self.quitButton)
    self.all_sprites = pygame.sprite.Group((self.start_buttons))
    self.girl_button = buttons.Button('girl_button', (220, 450), "girl.png")
    self.boy_button = buttons.Button('boy_button', (700, 450), 'boy.png')
    self.char_buttons.add(self.girl_button)
    self.char_buttons.add(self.boy_button)

  def mainLoop(self):
    while True:
      if (self.state == "start"):
        self.startingMenu()
      if (self.state == "choose"):
        self.chooseChar()
      if (self.state == "game"):
        self.gameLoop();
      if (self.state == "gameover"):
        self.gameOver()
      if (self.state == "gamewon"):
        self.gameWon()

  def gameLoop(self):
    while self.state == "game":
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseLocation = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
          sys.exit()
      pygame.display.flip()
      self.all_sprites.draw(self.screen)


  def gameWon(self):
    #self.state == gamewon
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit();

  def gameOver(self):
    #self.state == gameover
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit();

  def startingMenu(self):
    while True:
      mouseLocation = pygame.mouse.get_pos()
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "startUpMenu.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      for s in self.start_buttons:
        self.screen.blit(s.image, s.rect.topleft)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if self.startButton.rect.collidepoint(mouseLocation):
            self.chooseChar()
            return None
          elif self.quitButton.rect.collidepoint(mouseLocation):
            pygame.quit
            sys.exit()

  def spawnRoom(self):
    self.state = "game"
    image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "spawn.png")), (self.height, self.width))
    self.screen.blit(image, (0,0))
    coreLounge = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "coreLounge.png")), (400, 300))
    self.screen.blit(coreLounge, (700, 300))
    pygame.display.flip()

  def chooseChar(self):
    while True:
      mouseLocation = pygame.mouse.get_pos()
      self.state = "choose"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "choose.png")), (self.height, self.width))
      self.screen.blit(image, (0,0))
      for s in self.char_buttons:
        self.screen.blit(s.image, s.rect.topleft)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.quit:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if self.girl_button.rect.collidepoint(mouseLocation):
            char = 'jenny'
            self.spawnRoom()
            return None
          elif self.boy_button.rect.collidepoint(mouseLocation):
            char = 'alex'
            self.spawnRoom()
            return None




  #def spawnPizza(self):
