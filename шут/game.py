from pygame import *
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel
import time as t


display.set_caption("Шутер")
win_width, win_height = 1200 , 700
FPS = 70

clock = time.Clock()




#⚙️properties/свойства⚙️



amount_enemy = 5 #кол-во противников на карте

speed_player = 8
level_player = 1
ammunition_player = 500

score = 0 # сбито кораблей/score
goal = 100 # столько кораблей нужно сбить для победы

lost = 0 # пропущено кораблей
max_lost = 7 # проиграли, если пропустили столько





#🐍 FONT 🐍
font.init() 

font1 = font.Font("GangSmallYuxian.ttf", 25) 
font2 = font.Font("GangSmallYuxian.ttf", 30) 



#🐍 SOUND 🐍
mixer.init()
#backgaraund_sound
mixer.music.load('Sounds\sounds_backgraund.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()

sound_win = mixer.Sound('Sounds\sounds_win.mp3')
sound_kick = mixer.Sound('Sounds\sounds_bullet.mp3') #bullet
sound_kick.set_volume(0.2)
sound_gameOver = mixer.Sound('Sounds\sounds_gameOver.mp3')


#🐍 IMG/png/gif 🐍
img_win = "img\win.jpg" 
img_gameOver = "img\gamE_Over.jpeg" #фон проигрыша  img_los
img_backgraund = "img\spaceBackgraund.jpg" 
img_bullet = "img\img_bullet.png" 
img_hero = "img\player_2.png" 
img_enemy = "img\shrecksons.png" #враг
img_bonus = "img\heart1.png"






#🐍CLASSES🐍
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   # метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    
    def update(self):   
        global level_player 
        
        if keys[K_a] and self.rect.x > 5 or keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed_player
        if keys[K_d] and self.rect.x < win_width - 100 or keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += speed_player
        if keys[K_s] and self.rect.y < win_height -120 or keys[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += speed_player/2
        if keys[K_w] and self.rect.y > 5 or keys[K_UP] and self.rect.y > 5:
            self.rect.y -= speed_player/2

        

        if keys[K_1]:
            level_player = 1
        if keys[K_2]:
            level_player = 2
        if keys[K_3]:
            level_player = 3  
        if keys[K_4]:
            level_player = 4
        if keys[K_5]:
            level_player = 5
        if keys[K_0]:
            window = display.set_mode((0,0),FULLSCREEN)
        if keys[K_9]:
            run = False

        

    

    def fire1(self):
        bullet1  = Bullet (img_bullet, self.rect.centerx-5 , self.rect.top, 15, 60, -6)
        bullets.add(bullet1)
        sound_kick.play()

    def fire2(self):
        bullet1 = Bullet (img_bullet, self.rect.centerx+20 , self.rect.top, 15, 60, -6)
        bullet2 = Bullet (img_bullet, self.rect.centerx-20 , self.rect.top, 15, 60, -6)
        bullets.add(bullet1, bullet2)
        sound_kick.play()

    def fire3(self):
        bullet1 = Bullet (img_bullet, self.rect.centerx  , self.rect.top, 40, 20, -6)
        bullet2 = Bullet (img_bullet, self.rect.centerx-30 , self.rect.top, 40, 20, -6)
        bullet3 = Bullet (img_bullet, self.rect.centerx+30 , self.rect.top, 40, 20, -6)
        bullets.add(bullet1, bullet2, bullet3)
        sound_kick.play()
        sound_kick.play()

    def fire4(self):
        bullet1  = Bullet (img_bullet, self.rect.x  , self.rect.top, 40, 20, -6)
        bullets.add(bullet1)
        sound_kick.play()

    def fire5(self):
        bullet1  = Bullet (img_bullet, self.rect.x  , self.rect.top, 40, 20, -6)
        bullets.add(bullet1)
        sound_kick.play()


    def fire6(self):
        print("ss")


#👽 Enemy 👽
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = 500#randint(80, win_width - 80)
            self.rect.y = 0
            global lost
            lost = lost + 1

class Bonuses(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = 500
            self.rect.y = 50
            global lost
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()







bullets = sprite.Group()
monsters = sprite.Group()


window = display.set_mode((win_width, win_height))
backgraund = transform.scale(image.load(img_backgraund), (win_width, win_height))
ship = Player(img_hero, win_width/2-40, win_height-150, 100, 100, 10)





time_start = t.time()-0.1

finish = False
run = True

for i in range(0,amount_enemy):
    monster1 = Enemy(img_enemy, randint(80, win_width - 80), -100, randint(50,80), randint (50,80), randint(1, 3))
    monsters.add(monster1)


while run:
    
    

    time_ALL = t.time()
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys[K_ESCAPE]:
            run = False
    if keys[K_r]:
        finish=False
        print(finish)


    if not finish:
        if keys[K_SPACE]:
            if level_player == 1 and ammunition_player>0 and time_start+0.2<time_ALL:
                ship.fire1()
                ammunition_player-=1
                time_start = t.time()

            if level_player == 2 and ammunition_player>1 and time_start+0.3<time_ALL:
                ship.fire2()
                ammunition_player-=2
                time_start = t.time()

            if level_player == 3 and time_start+0.3<time_ALL:
                ship.fire3()

            if level_player ==4 and time_start+0.3<time_ALL:
                ship.fire4()

            if level_player ==5 and time_start+0.3<time_ALL:
                ship.fire4()

            if level_player ==6 and time_start+0.4<time_ALL:
                ship.fire4()




        window.blit(backgraund,(0, 0))
    
        ship.update()
        monsters.update()
        bullets.update()


        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
              
   

        collides = sprite.groupcollide(monsters, bullets, True, True)


        #Text
        text = font1.render("Score: " + str(score)+ "/" + str(goal), 1, (130, 105, 255))   
        window.blit(text, (10, 10))
        
        text_lose = font2.render("Omitted: " + str(lost) + "/" + str(max_lost), 1, (255, 100, 100))
        window.blit(text_lose, (10, 40))
        
        text_level_player = font1.render("Level: " + str(level_player) , 1, (255, 255, 0))
        window.blit(text_level_player, (10, 70))

        text_ammunition_player = font1.render("Ammunition: " + str(ammunition_player) , 1, (130, 105, 255))
        window.blit(text_ammunition_player, (10, 90))
        

        text_Game_Over = font1.render("Press F to Pay Respects", 1, (10, 10, 10))
        place = text_Game_Over.get_rect(center = (200, 500))
        
        

        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -100, randint(50,80), randint(50,80), randint(1,1))
            monsters.add(monster)



        #Game Over
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            img = image.load(img_gameOver)
            mixer.music.stop()
            sound_gameOver.play()
            d = img.get_width() // img.get_height()
            #window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (-200, 0))
            window.blit(text_Game_Over, place)

        #Win
        if score >= goal:
            finish = True
            img = image.load(img_win)
            mixer.music.pause()
            sound_win.play()
            #window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

        display.update()
        clock.tick(FPS)