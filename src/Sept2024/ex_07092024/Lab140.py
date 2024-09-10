# Duck Typing
class Bird:
    def fly(self):
        print("Birds can fly")


class Duck(Bird):
    def fly(self):
        super().fly()
        print("Flying duck")


class Sparrow:
    def fly(self):
        print("Flying Sparrow")


def flyable(flyable_object):
    flyable_object.fly()


sp = Sparrow()
d = Duck()

flyable(sp)
flyable(d)
