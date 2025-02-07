class Calc: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def add(self):
        return self.x + self.y

obj = Calc(4, 5) 

num = obj.add()
print(num)


