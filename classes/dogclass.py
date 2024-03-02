
# Dog class that creates dog objects that includes different bread 

class dog: 
    def __init__(self, breed, name, color, age, height, weight):    
        self.breed = breed
        self.name = name
        self.color = color
        self.age = age
        self.height = height 
        self.weight = weight 
    
    def dogFunc(self):

        print("Breed: " + self.breed, 
              "Name: " + self.name,
              "Color: " + self.color,
              "Age: " + self.age,
              "Height: " + self.height,
              "Weight: " + self.weight        
        )

dog1 = dog("Boston\n", "Brutus\n", "Black\n", "4\n", "12 inch\n", "40LB\n")
dog2 = dog("PitBull\n", "Maximus\n", "Grey\n", "5\n", "22 inch\n", "150LB\n")


dog1.dogFunc()
dog2.dogFunc()

