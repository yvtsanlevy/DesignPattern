class Coffee:


    def __init__(self):
        self.cost = 15
        self.ingredient = "coffe"

    def getCost(self):
        return self.cost

    def getIngredients(self):
        return self.ingredient

class CoffeeDecorator:

    def __init__(self ,  coffee):
        self.decoraterCoffee = coffee

    def getCost(self):
        return self.decoraterCoffee.getCost()

    def getIngredients(self):
        return self.decoraterCoffee.getIngredients()

class WithMilk(CoffeeDecorator):

    def __init__(self ,  coffee):
        super().__init__(coffee)

    def getCost(self):
        return super(WithMilk, self).getCost() + 2

    def getIngredients(self):
        return super(WithMilk, self).getIngredients() + " with milk"

class WithSprinkles(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self):
        return super(WithSprinkles, self).getCost() + 3

    def getIngredients(self):
        return super(WithSprinkles, self).getIngredients() + " with sprinkles"

def printInfo(coffee):
    print("Cost : " , coffee.getCost() ,"Ingredient : " , coffee.getIngredients())

def main():

    c = Coffee()
    printInfo(c)

    c = WithMilk(c)
    printInfo(c)

    c = WithSprinkles(c)
    printInfo(c)

main()