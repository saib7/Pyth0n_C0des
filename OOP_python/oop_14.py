# Operator Overloading 1

class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has", self.window, "windows and",
        self.door, "door(s).")

    def __add__(self, other):
        new_window = self.window + other.window
        new_door = self.door + other.door
        obj = House(new_window, new_door)
        return obj
        # return "New house has " + str(new_window) + " windows and " + str(new_door) + " door(s)."

#=====================================================================================================================================

h1 = House(6,2)
h2 = House(4,1)
h1.view()
h2.view()

# merge h1 and h2 . asked by client
h3 = h1+h2
h3.view( )
#print(h1+h2) # h1.__add(h2)