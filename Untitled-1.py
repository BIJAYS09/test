
class Traffic():
    def __init__(self, width, height, velocity, color):
        self.width = width
        self.height = height
        self.velocity = velocity
        self.color = color
        self.x = 0
        self.y = 0
    
    def move(self):
        self.y += self.velocity
        if self.y >= self.height:
            self.y = 0
            self.velocity += 5
            

class Car(Traffic) :
    def __init__(self):
        super().__init__(width=50, height=100, velocity=10, color="red")

class Truck(Traffic) :
    def __init__(self):
        super().__init__(width=70, height=100, velocity=15, color="green")   




def run():
    car = Car()
    truck = Truck()
    
    while True:
        car.move()
        truck.move()
        
run()        

        
        
    
           
        
        