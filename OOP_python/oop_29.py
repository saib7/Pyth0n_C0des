# Composition / Has a relationship

class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

#=====================================================================================================================================
class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(cc)   # put it in the car class reference. we've created an object here

    def run(self):
        print(self.engine)
        self.engine.start()    # self.engine is holding a object class address
        print("Car is running.")
#=====================================================================================================================================
c1 = Car("BMW", 2000)
c1.run()


