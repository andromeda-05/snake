import pygame # подключаем модуль pygame
import time # для временем и счетчиками
import random
from pygame.constants import K_8 # генератор псевдослучайных чисел
import body

# определяем переменные цвета
white = (255,255,255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# скорость обновлния поля
snakeSpeed = 5

# смещение
delta = 10

# текущее направление
keyDirect = "up" 

# Создаём игровое поле
sizeWidth = 500
sizeHeight = 500

# инициализируем модули pygame
pygame.init()

# создаем объект экран
field = pygame.display.set_mode((sizeWidth, sizeHeight))
# счетчик
clock = pygame.time.Clock()

# создаём объект змеи
snake = body.Snake()

# добавляем голову
snake.addElem(body.elem(sizeHeight/2, sizeWidth/2,1, keyDirect))

# еда
def foodCreate():
    fx = round(random.randrange(0, sizeWidth - delta) / 10.0) * 10.0
    fy = round(random.randrange(0, sizeHeight - delta) / 10.0) * 10.0
    return [fx, fy]   


# игровой цикл
def gameLoop():
# флаги окончания и закрытия игры
    gameOver = False
    gameClose = False

# запускаем еду
    food = foodCreate()
    
# начинаем гонять цикл
    while not gameOver:
        # цикл игры
        while gameClose == True:
            # заполняем поле цветом
            field.fill(blue)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        global keyDirect
        # отрабатываем нажатие кнопок 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keyDirect ="left"
                elif event.key == pygame.K_RIGHT:
                    keyDirect = "right"
                elif event.key == pygame.K_UP:
                    keyDirect = "up"
                elif event.key == pygame.K_DOWN:
                    keyDirect = "down"
        
        # выполняем перемещение змейки
        if snake.moveSnake(keyDirect, delta, food[0], food[1]) == True:
            food = foodCreate()
        

        # проверка на выход за границы экрана и самосьедение
        def conflictRange(x,y):
            if x > sizeWidth or x < 0 or y > sizeHeight or y < 0:
                return True
            else:
                return snake.conflictBody
        
        if conflictRange(snake.allBody[-1].setX(),snake.allBody[-1].setY()) == True or snake.conflictBody == True :
            gameClose = True
        else: gameClose = False
        
        
        

        # закрашиваем экран
        field.fill(blue)
        # рисуем закуску
        pygame.draw.rect(field, green, [food[0], food[1], delta, delta])
        
        # отрисовываем snake
        def paintSnake(body):
            for elm in body:
                pygame.draw.rect(field,black,[elm.setX(),elm.setY(),delta, delta])
        
        paintSnake(snake.allBody)
        
        pygame.display.update()
 
        clock.tick(snakeSpeed)
 
    pygame.quit()
    quit()


gameLoop()