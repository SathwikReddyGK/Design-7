# Dictionary and Deque (Deque in python is probably doubly linked list)
class SnakeGame:
    def addToSet(self,list):
        self.snakeSet.add(str(list[0])+str(list[1]))

    def deleteFromSet(self,list):
        self.snakeSet.discard(str(list[0])+str(list[1]))

    def checkIfNotOnSnake(self,list):
        key = str(list[0])+str(list[1])
        if key in self.snakeSet:
            return False
        else:
            return True

    def updateHead(self,direction):
        self.snakeHead = self.snakeHead.copy()
        if direction == "R":
            self.snakeHead[1] += 1
        elif direction == "D":
            self.snakeHead[0] += 1
        elif direction == "U":
            self.snakeHead[0] -= 1
        else:
            self.snakeHead[1] -= 1
    
    def checkBoundaries(self):
        if self.snakeHead[0] < 0 or self.snakeHead[0] >= self.height or self.snakeHead[1] < 0 or self.snakeHead[1] >= self.width:
            return False
        else:
            return True

    def checkIfFood(self):
        if self.foodIdx < len(self.food) and self.food[self.foodIdx][0] == self.snakeHead[0] and self.food[self.foodIdx][1] == self.snakeHead[1]:
            return True
        else:
            return False

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snakeSet = set()
        self.snakeSize = 0
        self.score = 0
        self.foodIdx = 0
        self.snakeQueue = deque()
        self.snakeQueue.append([0,0])
        self.snakeHead = [0,0]
        self.addToSet([0,0])
        self.food = food
        self.width = width
        self.height = height
        
    def addToQueue(self,list):
        self.snakeQueue.append(list)
        self.addToSet(list)
        if len(self.snakeQueue) > self.snakeSize:
            tempList = self.snakeQueue.popleft()
            self.deleteFromSet(tempList)

    def move(self, direction: str) -> int:
        self.updateHead(direction)
        if self.checkBoundaries():
            if self.checkIfNotOnSnake(self.snakeHead):
                if self.checkIfFood():
                    self.score += 1
                    self.snakeSize += 1
                    self.foodIdx += 1
                
                self.addToQueue(self.snakeHead)
                return self.score
            else:
                return -1
        else:
            return -1