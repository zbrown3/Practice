class Fruits:
    def __init__(self, fruitname, price, qty):
        self.price = price
        self.qty = int(input("Enter quantity: "))
        if self.qty <= 0:
            self.qty = int(input("Please enter quantity over 0: "))
        self.fruitname = fruitname

    def computeTotal(self):
        total = self.price * self.qty
        print("Thanks for your purchase")
        print(f"Your {self.fruitname} total is {total}.")

myFruits = Fruits("orange", 0.5, 6)
myFruits.computeTotal()

