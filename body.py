

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
    def getY(self,x):
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
    # удаляет элемент
    def delElem(self,n):
        if self.countElem > 1 : 
            del self.allBody[n]
            self.countElem -=1
        else:
            self.msgGameOver = True # если последний элемент
    
    # проверка на замыкание
    def conflictBody(self):
        for i in len(self.allBody)-1:
            if self.allBody[0].elemX == self.allBody[i].elemX and self.allBody[0].elemY == self.allBody[i].elemY:
                return True
        return False
        
    # проверка на соответствие координат
    def isFindElem(self, x,y):
        for i in self.allBody:
            if i.elemX == x and i.elemY == y :
                return True
        return False    
        
