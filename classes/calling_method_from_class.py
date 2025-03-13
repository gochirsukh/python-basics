class Person: 
    def __init__(self, name):
        self.name = name 
    
    def greet(self):
        return f"Hello my name is {self.name}"
    def congrats(self):
        return f"I {self.name} have mastered classes and objects"
    
p = Person("Fitzgerald")
print(p.greet())
print(p.congrats())