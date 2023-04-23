from pygame import *
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
sound2 = mixer.Sound('proehal.ogg')
sound2 = mixer.Sound('avaria.ogg')
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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            sound1.play()
        if keys_pressed[K_a] and self.rect.x > 180:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < 580:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < 750:
            self.rect.x += self.speed

car_gg = Car('car.png',550,450,10)
ray = False
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
    
    
    for d in event.get():
        if d.type == QUIT:
            run = False
    
    mw.blit(background1,(0,0))
    car_gg.reset()
    car_gg.update()
    display.update()
    clock.tick(60)
