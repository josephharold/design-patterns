from abc import ABC, abstractmethod

class IObserver(ABC):
    """
    The observer interface declares the update method, 
    which will be called by the subject
    """
    @abstractmethod
    def update(self, message: str)->None:
        pass

class ISubject(ABC):
    """
    Declares (but does not define) methods for adding, removing, and notifying Observers
    """
    @abstractmethod
    def registerObserver(self, observer: IObserver):
        pass
    @abstractmethod
    def removeObserver(self, observer: IObserver):
        pass
    @abstractmethod
    def notifyObservers(self):
        pass

class ConcreteObserver(IObserver):
    _name: str = ""
    def __init__(self, name: str)->None:
        self._name = name 

    def update(self, message: str)->None:
        print(f"observer {self._name} update: {message}")

class DifferentObserver(IObserver):
    _name: str = ""
    _class: str = ""
    _hero_number: str = ""
    def __init__(self, name: str, class_: str, hero_number: str):
        self._name = name
        self._class = class_
        self._hero_number = hero_number

    def update(self, message: str)->None:
        print(f"Hero name: {self._name} class {self._class} number {self._hero_number} reporting updates: {message}")

class ConcreteSubject(ISubject):
    _observers = []
    def registerObserver(self, observer: IObserver):
        self._observers.append(observer)

    def notifyObservers(self, message: str)->None:
        for observer in self._observers:
            observer.update(message)
    def removeObserver(self, observer: IObserver):
        if observer not in self._observers:
            return
        self._observers.remove(observer)



red = ConcreteObserver("Red")
yellow = ConcreteObserver("Yellow")
blue = ConcreteObserver("Blue")
white_ranger = DifferentObserver("white ranger", "power ranger", "vafds789214389")

# register observers and notify all of them
subject = ConcreteSubject()
subject.registerObserver(red)
subject.registerObserver(yellow)
subject.registerObserver(blue)
subject.registerObserver(white_ranger)
subject.notifyObservers("hello world")

# We remove the white ranger .
# Check again if the white ranger can still receive an update
subject.removeObserver(white_ranger)
subject.notifyObservers("hello again")

