class elem():
    '''Класс элемента тела змейки'''
    elemX = 0
    elemY = 0
    imgID = 1
    move = 'up' # up; down; left; right; levelUP; levelDOWN


    def __init__(self, x, y, imgID, move) -> None:
        self.elemX = x
        self.elemY = y
        self.imgID = imgID
        self.move = move

    def setX(self):
        return self.elemX
    def setY(self):
        return self.elemY
    def setImgID(self):
        return self.imgID
    def setMove(self):
        return self.move
        
    def getX(self,x):
        self.elemX = x
    def getY(self,y):
        self.elemY = y
    def getImgID(self,imgID):
        self.elemX = imgID   
    def getMove(self, move):
        self.move = move



class Snake:
    '''Класс тела змейки'''
    
    allBody = []
    countElem = 1
    msgGameOver = False
    def __init__(self) -> None:
        pass 
    # сообщение об конфликте например замыкание
    def setMsgGameOver(self):
        return self.msgGameOver

    # возвращает объект элемент
    def setElem(self,n=0):
        return self.allBody[n]       

    # добавляет элемент
    def addElem(self, elem):
        self.allBody.append(elem)
        self.countElem +=1

    # количество звеньев
    def countElements(self):
        return len(self.allBody)

    # перемещение 
    def moveSnake(self, direct, delta, foodx, foody):
        """перемещает змейку, параметр eat = True соответствует поеданию
        возвращает параметр eat"""

        x,y = self.allBody[-1].elemX , self.allBody[-1].elemY
        eat = False
        if direct == "left":
            x -= delta
        elif direct == "right":
            x += delta
        elif direct == "up":
            y -= delta
        elif direct == "down":
            y += delta
                        
        if foodx != x or foody != y :
            self.addElem(elem(x,y,1,direct))
            self.delElem(0)
        else: 
            self.addElem(elem(x,y,1,direct))
            eat = True
        return eat


    # удаляет элемент
    def delElem(self,n):
        if self.countElem > 1 : 
            del self.allBody[n]
            self.countElem -=1
        else:
            self.msgGameOver = True # если последний элемент
    
    # проверка на замыкание
    def conflictBody(self):
        cnt = len(self.allBody)
        for i in cnt:
            if self.allBody[cnt-1].elemX == self.allBody[i-1].elemX and self.allBody[cnt-1].elemY == self.allBody[i-1].elemY:
                return True
        return False

    # проверка на соответствие координат
    def isFindElem(self, x,y):
        for i in self.allBody:
            if i.elemX == x and i.elemY == y :
                return True
        return False    
        
