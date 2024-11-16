# OVERVIEW

# I got this from head first design patterns book
# Basically we have a super class Duck, but there are also different kinds of ducks (Mallard, etc.)
# Not all ducks can quack, not all ducks can fly
# Each duck has its own way i.e. own implementation of quacking and flying 

# interface for fly
class IFly:
    def fly(self)->None:
        pass
#interface for quack
class IQuack:
    def quack(self)->None:
        pass

# implementations for the interfaces above
class FlyWithWings(IFly):
    def fly(self):
        print("I'm flying with wingsss")
class FlyWithRockets(IFly):
    def fly(self):
        print("Rockets go brrrr...")

class RegularQuack(IFly):
    def quack(self):
        print("quack!")

class SonicBoomQuack(IQuack):
    def quack(self):
        print("KOOOOOH-WAAAAAAK")
class DeadSilenceQuack(IQuack):
    def quack(self):
        print("zzzzz :(")


class Duck:
    # we allow this class to accept 
    # a specific implementation of 
    # IFly interface and IQuack interface
    _flyStrategy: IFly = None
    _quackStrategy: IQuack = None
    def __init__(self, flyStrat, quackStrat)->None:
        self._flyStrategy = flyStrat 
        self._quackStrategy =  quackStrat

    def fly(self):
        self._flyStrategy.fly()

    def quack(self):
        self._quackStrategy.quack()

    def setQuack(self, quackStrat): 
        self._quackStrategy = quackStrat

    def setFly(self, flyStrat): 
        self._flyStrategy = flyStrat
class Mallard(Duck):
    def __init__(self):
        self._flyStrategy = FlyWithWings()
        self._quackStrategy = RegularQuack()

class DuckCybord(Duck):
    def __init__(self):
        self._flyStrategy = FlyWithRockets()
        self._quackStrategy = SonicBoomQuack()

duck = Duck(FlyWithRockets(), SonicBoomQuack())
duck.quack()
duck.setQuack(DeadSilenceQuack())
duck.quack()
duck.setQuack(SonicBoomQuack())
duck.quack()


# test fly
duck.fly()
duck.setFly(FlyWithWings())
duck.fly()

# test mallard
mallard = Mallard()
mallard.quack()
mallard.setQuack(SonicBoomQuack())
mallard.quack()

# CONCLUSION (I'm not sure about this):
# basically strategy pattern is a patter that allows the class to accept an implementation of an interface which will get called in its own methods???
# tapos dependency injection dayun???
