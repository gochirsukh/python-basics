class tacoma:
    def __init__(self, make, model, terrain, color):
        self.make = make
        self.terrain = terrain
        self.color = color
        self.model = model

obj=tacoma("toyota", "tacoma", "two wheel drive", "sylver")

print("I driver", obj.make, obj.model, "with",  obj.terrain, obj.color, "color")

# Output: 
# I driver toyota tacoma with two wheel drive sylver color




