class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name:", self.name,
        "\nAuthor:", self.author,
        "\nPrice:", self.price, "BDT")

#===================================================================================================================================

# b1 = Book("Opekkha", "Humayun Ahmed")
# b1.set_price(250)
# # print(b1.get_price()) # we have to print it or hold it in a variable
# b1.details()
