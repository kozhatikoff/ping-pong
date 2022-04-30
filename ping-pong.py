from pygame import *
#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Ping-Pong")
background=transform.scale(image.load("ping-pong.jpg"),(700,700))
window.blit(background,(0,0))
clock=time.Clock()
FPS=60
win_widht=700
win_height=500
mixer.init()
mixer.music.load("stadium.mp3")     
mixer.music.play()
font.init()
font1=font.SysFont("Arial",32)
font3=font.SysFont("Arial",32)
finish=False
run=True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y< win_widht - 50:
            self.rect.y += self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y< win_widht - 50:
            self.rect.y += self.speed

racket_1=Player("racket.png",670,200,10,30,150)
racket_2=Player("racket.png",0,200,10,30,150)
ball=Player("pngwing.com.png",320,250,0,60,60)
score=0
lose1=font3.render("PLAYER 1 LOSE",1,(255,45,45))
lose2=font3.render("PLAYER 2 LOSE",1,(255,45,45))
speed_x=3
speed_y=3
while run != False:
    clock.tick(FPS)
    for e in event.get():
        if e.type==QUIT:
            run=False
    if finish != True:  
        window.blit(background,(0,0))     
        racket_1.update_r()
        racket_2.update_l()
        racket_1.reset()
        racket_2.reset()
        ball.reset()    
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y*=-1
        if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_2,ball):
            speed_x*= -1
        if ball.rect.x > 650:
            finish=True
            window.blit(lose2,(430,250))
        if ball.rect.x < 0:
            finish=True
            window.blit(lose1,(100,250))
        



    display.update()
    