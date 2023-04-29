from pygame import *
from random import randint

'''Окно'''
font.init()
mixer.init()
clock = time.Clock()
run = True
mw = display.set_mode((1000,700))
display.set_caption('Save you Car')
background = transform.scale(image.load('fon.jpeg'),(1000,700))
background1 = transform.scale(image.load('road.jpg'),(1000,700))

font1 = 30
font = font.SysFont(None, font1)
mixer.music.load('music.ogg')
mixer.music.play()
sound1 = mixer.Sound('run.ogg')
sound2 = mixer.Sound('proehal.wav')
sound3 = mixer.Sound('avaria.wav')
move_left = False
move_up = False
move_down = False
move_right = False

'''классы'''
class Car(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(70,150))
        self.speed= speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Car_h(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(180,150))
        self.speed= speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Lines(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(20,100))
        self.speed= speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

'''Спрайты'''
car_gg = Car('car.png',550,450,10)
car1 = Car('car1.png',randint(180,730),-30,15)
car2 = Car('car2.png',randint(180,730),-30,10)
car3 = Car_h('car3.png',randint(180,730),-30,5)
line2 = Lines('line.jpg',650,400,5)
line3 = Lines('line.jpg',650,600,5)
line = Lines('line.jpg',650,30,20)
line1 = Lines('line.jpg',650,200,5)

line4 = Lines('line.jpg',350,400,5)
line5 = Lines('line.jpg',350,600,5)
line6 = Lines('line.jpg',350,30,5)
line7 = Lines('line.jpg',350,200,5)

ray = False
avay = None
'''Цикл'''
while run:
    while ray != True:
        c = font.render('Добро пожаловать!',True,(255,0,0))
        a = font.render('Save you car',True,(255,0,0))
        b = font.render('Чтобы начать игру нажмите "P"',True,(255,0,0))
        mw.blit(background,(0,0))
        mw.blit(a,(420,0))
        mw.blit(c,(380,100))
        mw.blit(b,(320,200))
        for e in event.get():
            if e.type == QUIT:
                ray = True
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_p:
                    ray = True

        display.update()
        clock.tick(45)

    mw.blit(background1,(0,0))

    for d in event.get():
        if d.type == QUIT:
            run = False
        elif d.type == KEYDOWN:
            if d.key == K_w:
                move_up = True
            if d.key == K_s:
                move_down = True
            if d.key == K_a:
                move_left = True
            if d.key == K_d:
                move_right = True
        elif d.type == KEYUP:
            if d.key == K_w:
                move_up = False
            if d.key == K_s:
                move_down = False
            if d.key == K_a:
                move_left = False
            if d.key == K_d:
                move_right = False                   
    if car1.rect.y == 750:
        car1.rect.y = 0
        car1.rect.x = randint(180,730)
        sound2.play()
    
    if car2.rect.y == 750:
        car2.rect.y = 0
        car2.rect.x = randint(180,730)
        sound2.play()

    if car3.rect.y == 750:
        car3.rect.y = 0
        car3.rect.x = randint(180,730)
        sound2.play()

    if sprite.collide_rect(car_gg,car1) or sprite.collide_rect(car_gg,car2) or sprite.collide_rect(car_gg,car3):
        sound3.play()


    if move_down == True and car_gg.rect.y <= 580:
        car_gg.rect.y += car1.speed
        line.rect.y -= line.speed
        line1.rect.y -= line.speed
        line2.rect.y -= line.speed
        line3.rect.y -= line.speed
        line4.rect.y -= line.speed
        line5.rect.y -= line.speed
        line6.rect.y -= line.speed
        line7.rect.y -= line.speed

    if move_left == True and car_gg.rect.x >= 180:
        car_gg.rect.x -= car_gg.speed

    if move_right == True and car_gg.rect.x <= 750:
        car_gg.rect.x += car_gg.speed
    
    if move_up == True and car_gg.rect.y >= 5:
        car_gg.rect.y -= car1.speed
        line.rect.y += line.speed
        line1.rect.y += line.speed
        line2.rect.y += line.speed
        line3.rect.y += line.speed
        line4.rect.y += line.speed
        line5.rect.y += line.speed
        line6.rect.y += line.speed
        line7.rect.y += line.speed


    car1.rect.y += car1.speed
    car2.rect.y += car2.speed
    car3.rect.y += car3.speed
    
    car_gg.reset()
    car1.reset()
    car2.reset()
    car3.reset()
    line.reset()
    line1.reset()
    line2.reset()
    line3.reset()

    line4.reset()
    line5.reset()
    line6.reset()
    line7.reset()
    display.update()
    clock.tick(60)
