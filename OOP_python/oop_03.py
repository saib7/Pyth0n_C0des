class Car:
    def __init__(self, name, model):
        self.name = name               # instance variable / attribute
        self.model_year = model        # instance variable / attribute
        self.wheel = 4                 # instance variable / attribute

    def view(self):
        print("The model of this", self.name, 
        "is", self.model_year)
        print("It is a", self.wheel, "wheel car.")

#================================================================================================================

c1 = Car("BMW", 2016)
c2 = Car("Audi", 2018)
c2.wheel = 6

c1.view()
c2.view()