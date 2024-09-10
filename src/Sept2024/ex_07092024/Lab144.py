from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine):
    def start(self):
        print("Car starting")

    @abstractmethod
    def stop(self):
        pass


class Car2(Car):
    def stop(self):
        print("Car is stopping")

    def drive(self):
        self.start()
        self.stop()


car = Car2()
car.drive()
