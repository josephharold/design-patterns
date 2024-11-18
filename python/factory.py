from abc import ABC, abstractmethod


# IMPORTANT:I'm still confused
# from what I understand... you may use factory method 
# when you need to instantiate/create many objects that are of different classes
# but are bound to a shared/common interface


# A pizza store can only have a single factory at a time. Its factory can be replaced
# A concrete factory can make any kind of pizza as long as it conforms to a specific interface
# PROCESS:

# pizza store has order method
# 1. client orders Pizza
# 2. pizza store instructs the factory to get an instance of that pizza
# 3. factory finds that kind of pizza from it's known pizzas and returns it to pizza store
# 4. pizza store calls the prepare() and box() methods of the pizza that is received


# pizza interface
class Pizza(ABC):
    @abstractmethod
    def prepare():
        pass
    @abstractmethod
    def box():
        pass

# creator/pizza interface
class PizzaFactory(ABC):
    @abstractmethod
    def createPizza(type: str)->Pizza:
        pass

class NYCheesePizza(Pizza):
    def prepare(self):
        print('preparing ny cheese pizza')
    def box(self):
        print("putting ny cheese pizza in a box")

class NYPepperoniPizza(Pizza):
    def prepare(self):
        print('preparing ny pepperoni pizza')
    def box(self):
        print("putting ny cheese pepperoni in a box")

class FiloPepperoniPizza(Pizza):
    def prepare(self):
        print("nag-prepare sa pepperoni pizza")
    def box(self):
        print("gibutang ang pepperoni pizza sa karton")

class FiloCheesePizza(Pizza):
    def prepare(self):
        print("nag-prepare sa cheese pizza")
    def box(self):
        print("gibutang ang cheese pizza sa karton")


class FiloPizzaFactory(PizzaFactory):
    def createPizza(self, type: str)->Pizza:
        match type:
            case "pepperoni":
                return FiloPepperoniPizza()
            case "cheese":
                return FiloCheesePizza()
            case _:
                return FiloPepperoniPizza()

class NYPizzaFactory(PizzaFactory):
    def createPizza(self, type: str)->Pizza:
        match type:
            case "pepperoni":
                return NYPepperoniPizza()
            case "cheese":
                return NYCheesePizza()
            case _:
                return NYPepperoniPizza()

class PizzaStore():
    _factory: PizzaFactory = None
    def __init__(self, factory: PizzaFactory):
        self._factory = factory
    def orderPizza(self, type):
        pizza = self._factory.createPizza(type)
        pizza.prepare()
        pizza.box()

filo = FiloPizzaFactory()
american = NYPizzaFactory()
store = PizzaStore(american)
store.orderPizza("pepperoni")

