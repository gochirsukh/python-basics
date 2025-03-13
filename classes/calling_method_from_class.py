class Person: 
    def __init__(self, name):
        self.name = name 
    
    def greet(self):
        return f"Hello my name is {self.name}"
    def congrats(self):
        return f"I {self.name} have mastered classes and objects"

b = Person("John Wick")    
p = Person("Fitzgerald")

for i in range(5):
    print( p.greet(), " ", p.congrats(),)
