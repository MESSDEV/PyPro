from pygame import *
#parent class for other sprites
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y):
       # Calling the class constructor (Sprite):
       sprite.Sprite.__init__(self)
       # each sprite must store an image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
  
       # each sprite must store the rect property - the rectangle which it's inscribed in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   # the method that draws the character in the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   #the method where the sprite is controlled by the arrow keys of the keyboard
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
       # Calling the class constructor (Sprite):
       GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
  
       self.x_speed = player_x_speed
       self.y_speed = player_y_speed
   def update(self):
       ''' moves the character by applying the current horizontal and vertical speed'''
       # horizontal movement first
       self.rect.x += self.x_speed
       self.rect.y += self.y_speed
#Creating a window
win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#setting the color according to the RGB color scheme
#creating wall pictures
w1 = GameSprite('platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('platform2_v.png', 370, 100, 50, 400)
#creating sprites
packman = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)
#game loop
run = True
while run:
   #the loop is triggered every 0.05 seconds
   time.delay(50)
   window.fill(back)#fill the window with color
  
   for e in event.get():
       if e.type == QUIT:
           run = False
       elif e.type == KEYDOWN:
           if e.key == K_LEFT:
               packman.x_speed = -5
           elif e.key == K_RIGHT:
               packman.x_speed = 5
           elif e.key == K_UP:
               packman.y_speed = -5
           elif e.key == K_DOWN:
               packman.y_speed = 5
       elif e.type == KEYUP:
           if e.key == K_LEFT:
               packman.x_speed = 0
           elif e.key == K_RIGHT:
               packman.x_speed = 0
           elif e.key == K_UP:
               packman.y_speed = 0
           elif e.key == K_DOWN:
               packman.y_speed = 0
   #draw objects
   #  w1.reset()
   #  w2.reset()
   packman.reset()
  
   #turning on the movement
   packman.update()
  
   display.update()
