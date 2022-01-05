import pygame # подключаем модуль pygame
import time # для управления временем и счетчиками
import random # генератор псевдослучайных чисел
import body

# инициализируем модули pygame
pygame.init()
import pygame # подключаем модуль pygame
import time # для временем и счетчиками
import random # генератор псевдослучайных чисел
import body

# инициализируем модули pygame
pygame.init()
# создаём объект змеи
snake = body.Snake

# Создаём игровое поле
sizeWidth = 500
sizeHeight = 500
# создаем объект экран
field = pygame.display.set_mode((sizeWidth, sizeHeight))

# Запускаем еду

# Основной цикл
# игровой цикл
def gameLoop():
# флаги окончания и закрытия игры
    gameOver = False
    gameClose = False
# начальное положение  
    x1 = sizeWidth / 2
    y1 = sizeHeight / 2
# временное изменение координат 
    x1Change = 0
    y1Change = 0
# массив звеньев
#    snake_List = []
# длина 
#    Length_of_snake = 1

# еда
   
# начинаем гонять цикл
    while not game_over:
        # цикл игры
        while gameClose == True:
            field.fill(blue)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # отрабатываем нажатие кнопок 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # проверка на выход за границы экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # приращение координат
        x1 += x1_change
        y1 += y1_change
        # закрашиваем экран
        dis.fill(blue)
        # рисуем закуску
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        # отрисовываем голову
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        # добавляем голову в конец массива
        snake_List.append(snake_Head)
        # если длина больше удаляем звено
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # проверка на самосьедение
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        # отрисовываем тело
        our_snake(snake_block, snake_List)
        
        # Счёт
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()