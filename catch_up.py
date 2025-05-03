from pygame import *

#создай окно игры
win = display.set_mode((700, 500))
display.set_caption('догонялки')

#задай фон сцены
bg = transform.scale(image.load('images (5).jfif'), (700, 500))
game = True
sp1 = transform.scale(image.load('images (3).jfif'), (100, 100))
sp2 = transform.scale(image.load('images (2).jfif'), (100, 100))
x1 = 100
y1 = 300
x2 = 500
y2 = 300
clock = time.Clock()
while game:
    win.blit(bg, (0, 0))
    win.blit(sp1, (x1, y1))
    win.blit(sp2, (x2, y2))
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 < 400:
        y1 += 10
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += 10
    if keys_pressed[K_w] and y2 > 0:
        y2 -= 10
    if keys_pressed[K_s] and y2 < 400:
        y2 += 10
    if keys_pressed[K_a] and x2 > 0:
        x2 -= 10
    if keys_pressed[K_d] and x2 < 600:
        x2 += 10
    clock.tick(60)
    display.update()
#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»