class House:
    def __init__(self):
        self.window = 4  # Instance variable / attribute
        self.door = 2    # Instance variable / attribute

    def view(self):
        print(self.window, "Windows", self.door, "doors")

#================================================================================================================

h1 = House()
h2 = House()
h1.window = 6
h2.door = 3
h1.view()
h2.view()