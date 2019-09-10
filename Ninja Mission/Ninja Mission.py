# This program was written by R.Fan on May 3. It plays the game of Ninja Mission
import pygame, os, random, time
from pygame.locals import *

#set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 522

#set up the colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#set up the frame rate
FRAMERATE = 55

def terminate():
    """This function is called when the user closes the window"""
    pygame.quit()
    os._exit(1)
    
def drawText(text, font, surface, x, y, textcolour):
    """This function is used to draw text on the screen at a specified location"""
    textobj = font.render(text, 1, textcolour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def blink_text(windowSurface, image, rectangle, text, count):
    """This function creates a blinking text"""
    windowSurface.blit(image, rectangle)
    basicFont = pygame.font.SysFont("Comic Sans MS", 20)
    if count < 220:
        drawText(text, basicFont, windowSurface, 300, 480, WHITE)
        count +=1
    elif count < 300:
        count +=1
    else:
        count = 0

    pygame.display.update()
    return(count)

def display_menu(windowSurface, play_sound):
    """This function is used to display a menu on the screen with a background image and a blinking text"""
    Menu_Backgound, Menu_Rect = load_image("IntroScreen.png")
    text = "Press Enter To Start"
    textcount = 0
    
    ST_Game = False                 #a boolean variable to check if the user wants to start the game
    Instruct = False                #a boolean variable to check if the user wants to see the instruction

    #play the background music if it is not muted
    pygame.mixer.music.load("MenuSong.mp3")
    if play_sound:
        pygame.mixer.music.play(-1, 12.0)
  
    while not Instruct and not ST_Game:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    ST_Game = True
                elif event.key == ord('i'):
                    play_sound = display_instruction(windowSurface, play_sound)
                    Instruct = True
                elif event.key == ord('m'):
                    if play_sound:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 12.0)
                    play_sound = not play_sound
                    
        textcount = blink_text(windowSurface, Menu_Backgound, Menu_Rect, text, textcount)
        

    return(play_sound)

        
def display_instruction(windowSurface, play_sound):
    """This function is used to dispaly the intruction page"""
    Instr_Background, Instr_rect = load_image("Instr_Background.png")
    text = "Press Escape To Go Back"
    Escape = False                  #a boolean variable to check if the user wants to go back to the menu
    textcount = 0

    #play the background music if it is not muted
    pygame.mixer.music.load("MenuSong.mp3")
    if play_sound:
        pygame.mixer.music.play(-1, 12.0)

    while not Escape:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    play_sound = display_menu(windowSurface, play_sound)
                    Escape = True
                elif event.key == ord('m'):
                    if play_sound:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 12.0)
                    play_sound = not play_sound

        textcount = blink_text(windowSurface, Instr_Background, Instr_rect, text, textcount)

    return(play_sound)

def Mission_Failed(windowSurface, play_sound):
    """This function is used to display the Mission Failed page"""
    MissionF_background, MissionF_rect = load_image("MissionFailed.png")
    text = "Press Enter To Restart"
    restart = False                 #a boolean variable to check if the user wants to restart and go back to the menu
    textcount = 0

    #play the background music if it is not muted
    pygame.mixer.music.load("GameOver.mp3")
    if play_sound:
        pygame.mixer.music.play(-1, 0.0)

    while not restart:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    main(play_sound)
                    restart = True
                elif event.key == ord('m'):
                    if play_sound:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 12.0)
                    play_sound = not play_sound

        textcount = blink_text(windowSurface, MissionF_background, MissionF_rect, text, textcount)

    return(play_sound)

def Mission_Complete(windowSurface, play_sound):
    """This function is used to display the Mission Complete page"""
    MissionC_background, MissionC_rect = load_image("MissionComplete.png")
    text = "Press Enter To Restart"
    restart = False         #a boolean variable to check if the user wants to restart and go back to the menu
    textcount = 0

    #play the background music if it is not muted
    pygame.mixer.music.load("victory.mp3")
    if play_sound:
        pygame.mixer.music.play(-1, 0.5)

    while not restart:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    main(play_sound)
                    restart = True
                elif event.key == ord("m"):
                    if play_sound:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 2.5)
                    play_sound = not play_sound

        textcount = blink_text(windowSurface, MissionC_background, MissionC_rect, text, textcount)
        
    return(play_sound)

def animate_levels(windowSurface, text1, text2):
    """This function is used display texts in between each level of the game"""
    basicFont = pygame.font.SysFont("Comic Sans MS", 35)
    done = False        #a boolean variable used to check if the animation is done
    start = time.time()
    
    while not done:
        if time.time()-start < 1:
            windowSurface.fill(BLACK)
            drawText(text1, basicFont, windowSurface, 325, WINDOWHEIGHT//2, WHITE)
        elif time.time()-start < 1.5:
            windowSurface.fill(BLACK)
            drawText(text2, basicFont, windowSurface, 365, WINDOWHEIGHT//2, WHITE)
        else:
            done = True
            
        pygame.display.update()

def level1_animation(windowSurface):
    """This function is used to creat the LEVEL_1 and GO animation"""
    text1 = "LEVEL_1"
    text2 = "GO"

    animate_levels(windowSurface, text1, text2)

def level2_animation(windowSurface):
    """This function is used to creat the LEVEL_2 and GO animation"""
    text1 = "LEVEL_2"
    text2 = "GO"

    animate_levels(windowSurface, text1, text2)

def level3_animation(windowSurface):
    """This function is used to creat the LEVEL_3 and GO animation"""
    text1 = "LEVEL_3"
    text2 = "GO"

    animate_levels(windowSurface, text1, text2)

def load_image(filename):
    """This function is used to load an image from a file. Return the image and its corresponding rectangle"""
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image, image.get_rect()

class BouncyBall(pygame.sprite.Sprite):
    """Ball that bounce around the screen and can cause the player to lose lives"""
    def __init__(self, x, y, yspeed, xspeed, filename, gravity, direct):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(filename)

        #set up the initial location, speed and direction of the bouncy ball
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.gravity = gravity
        self.direct = direct
        
    def update(self):
        """Change the position of the bouncy ball's rectangle"""
        if self.direct == "right":
            self.x += self.xspeed
        elif self.direct == "left":
            self.x -= self.xspeed

        #keep the bouncy ball within the screen, change its horizontal and vertical speed
        if self.x+self.image.get_width() > WINDOWWIDTH:
            self.xspeed *= -1
        elif self.x < 0:
            self.xspeed *= -1

        self.y += self.yspeed

        self.yspeed += self.gravity

        if self.y+self.image.get_height() > 400:
            self.yspeed *= -0.97
        elif self.y < 0 :
            self.yspeed *= -1

        self.rect.x = self.x
        self.rect.y = self.y

class Player(pygame.sprite.Sprite):
    """A ninja character control by the user"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #two lists of images that contain the right and left movements of the ninja
        self.RightMotion = [pygame.image.load('RM1.png').convert_alpha(), pygame.image.load('RM2.png').convert_alpha(), pygame.image.load('RM3.png').convert_alpha(), pygame.image.load('RM4.png').convert_alpha(), pygame.image.load('RM5.png').convert_alpha()]
        self.LeftMotion = [pygame.image.load('LM1.png').convert_alpha(), pygame.image.load('LM2.png').convert_alpha(), pygame.image.load('LM3.png').convert_alpha(), pygame.image.load('LM4.png').convert_alpha(), pygame.image.load('LM5.png').convert_alpha()]

        self.dead_image = pygame.image.load("Dead_Ninja.png").convert_alpha()       #the dead image of the ninja

        #set up the initial location, speed, walking steps and lives for the ninja
        self.rect = self.RightMotion[0].get_rect()
        self.rect.x = 210
        self.rect.y = 317
        self.movespeed = 5
        self.walknums = 0
        self.lives = 3
        self.left = False       #a boolean variable to check if the ninja is moving to the left before stopping

        #set up movement variables
        self.moveLeft = False
        self.moveRight = False
        self.dead = False

    def Movements(self):
        """Pick the right image from the right or left movement list by using the walking steps of the ninja"""
        if self.dead:
            self.image = self.dead_image
        else:
            if self.walknums + 1 >= 15:
                self.walknums = 0

            if self.moveLeft:
                self.image = self.LeftMotion[self.walknums//3]
                self.walknums += 1
            elif self.moveRight:
                self.image = self.RightMotion[self.walknums//3]
                self.walknums += 1
            else:
                if self.left:
                    self.image = self.LeftMotion[0]
                else:
                    self.image = self.RightMotion[0]

    def update(self):
        """Change the position of the ninja's rectangle"""
        if not self.dead:
            if self.moveLeft and self.rect.left > 0:
                self.left = True
                self.rect.left -= self.movespeed
                
            elif self.moveRight and self.rect.right < WINDOWWIDTH:
                self.left = False
                self.rect.right += self.movespeed
                
            else:
                self.walknums = 0

class Bullets(pygame.sprite.Sprite):
    """The weapon (ninja start) shoot out by the player"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image, self.rect = load_image('NStar.png')         

        #set up the intial location, speed and rotation degree for the ninja star
        self.rect.x = x
        self.rect.y = y
        self.wspeed = 5
        self.degrees = 0
        
        self.RTimage = pygame.transform.rotate(self.image, self.degrees)        #rotate the image while it is moving

    def update(self):
        """Change the position and rotation degree of the ninja star's rectangle"""
        if self.rect.top > 0 and self.rect.bottom < WINDOWHEIGHT:
            self.rect.top -= self.wspeed
        else:
            self.kill()

        self.degrees += 20

class NinjaHeart(pygame.sprite.Sprite):
    """Images used to show the number of lives the ninja have"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image("Ninja_Heart.png")

        #set up the location of the heart
        self.rect.x = x
        self.rect.y = y
        
    def disappear(self):
        """Getting rid of the heart when the player loses a life"""
        self.kill()

class Wall(pygame.sprite.Sprite):
    """Walls that divides the screen into sections"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image("Ninja_Wall.png")

        #set up the location of the wall
        self.rect.x = x
        self.rect.y = y

class Boss(pygame.sprite.Sprite):
    """The ultimate boss of the game that the player has to destroy"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image("Ninja_Boss.png")

        #set up the initial location, speed and lives of the boss
        self.rect.x = 300
        self.rect.y = 0
        self.xspeed = 3
        self.lives = 10

    def update(self):
        """Change the position of the boss's rectangle"""
        self.rect.x -= self.xspeed
        
        if self.rect.right > WINDOWWIDTH:
            self.xspeed *= -1
        elif self.rect.left < 0:
            self.xspeed *= -1

class BossHeart(pygame.sprite.Sprite):
    """An image that represents the boss, beside its health bar"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image("Boss_Heart.png")

        #set up the location of the boss's image
        self.rect.x = 430
        self.rect.y = 5

class HealthPack(pygame.sprite.Sprite):
    """ A free life that drops down from a bouncy ball when the player hits it"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image("Ninja_Heart.png")

        #set up the initial location of the free life image
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Change the position of the free life's rectangle"""
        if self.rect.bottom < 400:
            self.rect.y += 5


class Game():
    """This class represents an instance of the game"""
    def __init__(self, image, rect, level, player, play_sound, songfile):
        """ Constructor. Create all the attributes and initialize the game"""

        #set to ture when the player loses all lives or the player destroys the boss
        self.game_over = False

        #set up the level of the game
        self.level = level

        #set up the background image of the game and its rectangle
        self.image = image
        self.rect = rect

        #set up the different sprite groups
        self.all_sprites = pygame.sprite.Group()

        #set up the player
        self.player = player
        self.all_sprites.add(self.player)

        #set up the bullets (ninja stars)
        self.bullets = pygame.sprite.Group()
        
        #set up the bouncy balls
        self.balls = pygame.sprite.Group()

        #set up the music and the sound effects
        self.play_sound = play_sound
        self.NinjaSound = pygame.mixer.Sound("Ninja_SE.wav")
        self.BulletSound = pygame.mixer.Sound("Bullet_SE.wav")
        self.BlopSound = pygame.mixer.Sound("Blop_SE.wav")
        self.GotHitSound = pygame.mixer.Sound("GotHit_SE.wav")

        #set up a starting time
        self.start_time = time.time()

        if self.level == 1 or self.level == 2:
            #create bouncy balls that only belong to level 1 and 2
            self.aball = BouncyBall(50, 150, 0, 3, "Ninja_Ball.png", 0.1, "right")
            self.balls.add(self.aball)
            self.all_sprites.add(self.aball)
            
            self.aball2 = BouncyBall(700, 150, 0, 3, "Ninja_Ball.png", 0.1, "left")
            self.balls.add(self.aball2)
            self.all_sprites.add(self.aball2)

            self.aball3 = BouncyBall(450, 150, 0, 3, "Ninja_Ball.png", 0.1, "left")
            self.balls.add(self.aball3)
            self.all_sprites.add(self.aball3)

            self.aball4 = BouncyBall(250, 150, 0, 3, "Ninja_Ball.png", 0.1, "right")
            self.balls.add(self.aball4)
            self.all_sprites.add(self.aball4)

            if self.level == 2:
                #set up the walls for level2
                self.walls = pygame.sprite.Group()
                pos = 165
                for x in range(3):
                    awall = Wall(pos,0)
                    self.walls.add(awall)
                    self.all_sprites.add(awall)
                    pos += 210

        elif self.level == 3:
            #set up the boss for level 3
            self.boss = Boss()
            self.all_sprites.add(self.boss)
            self.bossheart = BossHeart()

        #set up the free lives
        self.healthpacks = pygame.sprite.Group()

        #set up the hearts (number of lives) for the ninja
        self.hearts = pygame.sprite.Group()
        self.space = 0                      #needed for the proper display of heart images for the ninja
        for x in range(self.player.lives):
            aheart = NinjaHeart(self.space,0)
            self.hearts.add(aheart)
            self.all_sprites.add(aheart)
            self.space += aheart.image.get_width()

        #play the background music
        pygame.mixer.music.load(songfile)
        if play_sound:
            pygame.mixer.music.set_volume(0.5)
            if songfile == "MenuSong.mp3":
                pygame.mixer.music.play(-1, 12.0)
            else:
                pygame.mixer.music.play(-1, 0.0)
            
    def process_events(self, windowSurface):
        """Process all of the keyboard and mouse events"""
        for event in pygame.event.get():
            end_time = time.time()
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    #check for the left movement of the ninja
                    self.player.moveRight = False
                    if self.player.dead:
                        #when the ninja gets hit by a bouncy ball, it can not move for 0.1 second
                        self.player.moveLeft = False
                        if end_time - self.start_time > 0.1:
                            self.player.moveLeft = True
                            self.player.dead = False
                    else:
                        self.player.moveLeft = True
                        
                elif event.key == K_RIGHT or event.key == ord('d'):
                    #check for the right movement of the ninja
                    self.player.moveLeft = False
                    if self.player.dead:
                        #when the ninja gets hit by a bouncy ball, it can not move for 0.1 second
                        self.player.moveRight = False
                        if end_time - self.start_time > 0.1:
                            self.player.moveRight = True
                            self.player.dead = False
                    else:
                        self.player.moveRight = True
                        
                elif event.key == K_SPACE:
                    #check for shooting, the ninja can not move when it is shooting
                    self.player.moveLeft = False
                    self.player.moveRight = False
                    if self.player.dead:
                        #when the ninja gets hit by a bouncy ball, it can not shoot for 0.1 second
                        self.player.spaceBar = False
                        if end_time - self.start_time > 0.1:
                            self.player.spaceBar = True
                            self.player.dead = False
                    else:
                        if self.play_sound:
                            #play the sound effects
                            self.NinjaSound.play()
                            self.BulletSound.play()
                            
                        self.player.spaceBar = True
                    
                        if len(self.bullets) < 1:
                            #the player can only shoot out one ninja star at a time
                            abullet = Bullets(self.player.rect.x+25, self.player.rect.y-41)
                            self.bullets.add(abullet)
                            self.all_sprites.add(abullet)

                elif event.key == ord('m'):
                    # toggles the background music
                    if self.play_sound:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    self.play_sound = not self.play_sound
                        
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_LEFT or event.key == ord('a'):
                    self.player.moveLeft = False
                elif event.key == K_RIGHT or event.key == ord('d'):
                    self.player.moveRight = False
                elif event.key == K_SPACE:
                   self.bullets.spaceBar = False

    def run_logic(self):
        """ This method is run each time through the frame. It
        updates positions, checks for collisions and levels"""
        if not self.game_over:

            end_time = time.time()              #get an ending time
            self.player.Movements()             #pick a right image of the ninja for its corresponding movement
            randnum = random.randrange(5)       #get a random number between 0-4

            self.all_sprites.update()           #update the movements of all sprites

            #the free lives pick up the ninja when it destroys the bouncy balls
            pickup_health_list = pygame.sprite.spritecollide(self.player, self.healthpacks, True)
            for ahealth in pickup_health_list:
                self.player.lives += 1
                aheart = NinjaHeart(self.space,0)
                self.hearts.add(aheart)
                self.all_sprites.add(aheart)
                self.space += 60                #needed for the display of the heart images for the ninja
                
            #the bouncy balls that are destroyed by the ninja
            ball_destroy_list = pygame.sprite.groupcollide(self.balls, self.bullets, 1, 1)
            for aball in ball_destroy_list:
                if self.play_sound:
                    #play the sound effect
                    self.BlopSound.play()
                
                if randnum == 1 and self.player.lives < 5:
                    #create a free life when the random number is 1 and the player has less than 5 lives
                    apack = HealthPack(aball.rect.x, aball.rect.y)
                    self.healthpacks.add(apack)
                    self.all_sprites.add(apack)
                        
                if self.level == 1 or self.level == 2:
                    #split up the bouncy balls into the two smaller bouncy balls
                    if aball == self.aball:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)
                        
                    elif aball == self.aball2:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)

                    elif aball == self.aball3:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)
                        
                    elif aball == self.aball4:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -4, 3, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)
                        
            #the bouncy balls that hit the ninja
            ball_hit_list = pygame.sprite.spritecollide(self.player, self.balls, True)
            for aball in ball_hit_list:
                if self.play_sound:
                    #play the sound effect
                    self.GotHitSound.play()

                #make the last heart image of the ninja on the screen to disappear
                count = 1
                for aheart in self.hearts:
                    if count == self.player.lives:
                        aheart.disappear()
                    count += 1

                if self.player.lives > 0:
                    #the ninja loses a life
                    self.player.lives -= 1

                self.space -= 60            #needed for the display of the heart images for the ninja
                    
                #the ninja is dead and reset the time
                self.player.dead = True
                self.start_time = time.time()

                if self.level == 1 or self.level == 2:
                    #split up the bouncy balls into the two smaller bouncy balls
                    if aball == self.aball:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)
                        
                    elif aball == self.aball2:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)

                    elif aball == self.aball3:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)

                    elif aball == self.aball4:
                        ballone = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "left")
                        self.balls.add(ballone)
                        self.all_sprites.add(ballone)
                        
                        balltwo = BouncyBall(aball.rect.x, aball.rect.y, -5, 2, "SmNinja_Ball.png", 0.1, "right")
                        self.balls.add(balltwo)
                        self.all_sprites.add(balltwo)

            if self.level == 1:
                #if all of the bouncy balls are destroyed in level 1, move on to level 2
                if len(self.balls) == 0:
                    self.level = 2

            elif self.level == 2:
                #allows the balls to bounce off the walls properly
                ball_hitWall_list = pygame.sprite.groupcollide(self.balls, self.walls, 0, 0)
                for aball in ball_hitWall_list:
                    aball.xspeed *= -1
                    if aball.rect.y < 310 and aball.rect.y > 290 and aball.yspeed < 0:
                        aball.yspeed *= -1
                        
                #ensure that the ninja can not shoot out ninja stars when it is under the walls
                bullet_hitWall_list = pygame.sprite.groupcollide(self.bullets, self.walls, 1, 0)
                for abullet in bullet_hitWall_list:
                    abullet.kill()

                if len(self.balls) == 0:
                    #if all of the bouncy balls are destroyed in level 2, move on to level 3
                    self.level = 3

            elif self.level == 3:
                #for every second, two bouncy balls will be generated by the boss until there is maximum of six bouncy balls on the screen
                if end_time - self.start_time >= 1:
                    self.start_time = time.time()
                    if len(self.balls) < 6:
                        ball_1 = BouncyBall(self.boss.rect.x+80, 100, 0, 3, "Ninja_Ball.png", 0.1, "right")
                        self.balls.add(ball_1)
                        self.all_sprites.add(ball_1)

                        ball_2 = BouncyBall(self.boss.rect.x+80, 100, 0, 3, "Ninja_Ball.png", 0.1, "left")
                        self.balls.add(ball_2)
                        self.all_sprites.add(ball_2)

                #keeps track of the number of ninja stars that hit the boss and reduce the boss's lives
                boss_destroy_list = pygame.sprite.spritecollide(self.boss, self.bullets, True)
                for ahit in boss_destroy_list:
                    self.boss.lives -= 1

                if self.boss.lives == 0:
                    self.game_over = True

        #rotate the ninja star while it is moving
        for abullet in self.bullets:
            abullet.image = pygame.transform.rotate(abullet.RTimage, abullet.degrees)

        if self.player.lives == 0:
            self.game_over = True


    def display_frame(self, windowSurface):
        """ Display everything to the screen for the game"""
        if self.game_over:
            if self.player.lives == 0:
                self.play_sound = Mission_Failed(windowSurface, self.play_sound)
            elif self.boss.lives == 0:
                self.play_sound = Mission_Complete(windowSurface, self.play_sound)
        else:
            #draw the background image and the images of all different sprites onto the screen
            windowSurface.blit(self.image, self.rect)
            if self.level == 3:
                #draw the health bar of the boss in level 3
                pygame.draw.rect(windowSurface, RED, (490, 10, 300-(30*(10-self.boss.lives)), 25))
                pygame.draw.line(windowSurface, WHITE, (490, 10), (790, 10), 2)
                pygame.draw.line(windowSurface, WHITE, (490, 35), (790, 35), 2)
                pygame.draw.line(windowSurface, WHITE, (490, 10), (490, 35), 2)
                pygame.draw.line(windowSurface, WHITE, (790, 10), (790, 35), 2)
                windowSurface.blit(self.bossheart.image, self.bossheart.rect)

            self.all_sprites.draw(windowSurface)

        pygame.display.update()
        
play_sound = True           #a boolean variable to check if the music & sound effects of the game are played or muted

def main(play_sound):
    """mainline for the program"""
    
    pygame.init()
    mainClock = pygame.time.Clock()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Ninja Mission')

    #display the menu
    play_sound = display_menu(windowSurface, play_sound)

    background, backgroundrect = load_image("Night_Background.png")

    #instantiate a player
    player = Player()

    songfile = "Ninja_song.mp3"

    #stop the music while the level_1 animation is happening
    pygame.mixer.music.stop()
    level1_animation(windowSurface)

    #instantiate a game
    game = Game(background, backgroundrect, 1, player, play_sound, songfile)

    level2 = False
    level3 = False

    #run the game loop until the user quits
    while True:
        play_sound = game.play_sound

        #process events to check for keystrokes and mouse clicks
        game.process_events(windowSurface)

        #update object position, check for collisions and levels
        game.run_logic()
        if game.level == 2 and not level2:
            #stop the music while the level_2 animation is happening
            pygame.mixer.music.stop()
            level2_animation(windowSurface)
            game = Game(background, backgroundrect, 2, player, play_sound, songfile)
            level2 = True
            
        elif game.level == 3 and not level3:
            #stop the music while the level_3 animation is happening
            pygame.mixer.music.stop()
            level3_animation(windowSurface)
            songfile = "Boss.mp3"
            game = Game(background, backgroundrect, 3, player, play_sound, songfile)
            level3 = True
            
        #draw the current frame
        game.display_frame(windowSurface)
        
        mainClock.tick(FRAMERATE)

main(play_sound)
