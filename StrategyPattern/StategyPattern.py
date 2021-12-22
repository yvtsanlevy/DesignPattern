# In the following example, we want to create different types of ducks
# instead of building multiple sub-classes,
# we just create different behaviors and put into our duck the behaviors we want it to have.

class Duck:

    def __init__(self, fb, qb):
        self.IFlyBehavior = fb
        self.IQuackBehvior = qb

    def Fly(self):
        self.IFlyBehavior.Fly()

    def Quack(self):
        self.IQuackBehvior.Quack()

# The Quack strategy
class QuackBehavior:

    normalQuack = "QUACK QUACK"
    strongQuack = "QUUUUUAAAAAAAAACCCKKKKK"

    def __init__(self, qb):
        self.QuackB = qb

    def Quack(self):
        print( self.QuackB)

# The Fly strategy

class FlyBehavior:

    dayFly = "Flying at day"
    nightFly = "Flying at night"

    def __init__(self, fb):
        self.FlyB = fb

    def Fly(self):
        print( self.FlyB)


def main():

    normalQ = QuackBehavior(QuackBehavior.normalQuack)
    strongQ = QuackBehavior(QuackBehavior.strongQuack)

    DayF = FlyBehavior(FlyBehavior.dayFly)
    NightF = FlyBehavior(FlyBehavior.nightFly)

    duck1 = Duck(DayF,normalQ)
    duck2 = Duck(NightF,strongQ)

    duck1.Quack()
    duck1.Fly()

    duck2.Quack()
    duck2.Fly()



main()



