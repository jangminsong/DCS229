import math

class Shape:
    __slots__ = ("_name", "_area")

    def __init__(self, name: str) -> None:
        self._name: str   = name
        self._area: float = 0   # nebulous Shape doesn't have area

    def __str__(self) -> str:
        #return f"Shape {self._name}: area = {self._area}"
        return f"{type(self).__name__} {self._name}: area = {self._area}"

    def getArea(self) -> float:
        return self._area

######################################################################

class Circle(Shape):            # Circle inherits from Shape
    __slots__ = ("_radius")     # include only new instance varaibles

    def __init__(self, name: str, radius: float) -> None:
        super().__init__(name)  # call __init__ in the parent class
        self._radius = radius
        self._area = math.pi * (radius**2)  # directly access an inherited field

class Triangle(Shape):
    __slots__ = ("_base", "_height")

    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name)  # call __init__ in the parent class
        self._area = 0.5 * base * height
        self._base = base
        self._height = height

    def __str__(self) -> str:
        # overriding the __str__ method inherited from Shape
        return f"{type(self).__name__} {self._name}: area = {self._area} " + \
               f"with base {self._base} and height {self._height}"

    def getBase(self) -> float:
        return self._base

######################################################################

class Whatever:  # not in the Shape hierarchy
    __slots__ = ('_whatevs')
    def __init__(self, whatevs: str) -> None:
        self._whatevs = whatevs
    def getArea(self) -> float:
        return 0.0

######################################################################


def processShape(shape: Shape) -> None:
    # from Wikipedia:
    #       In object-oriented programming, polymorphism is the provision of a
    #       single interface to entities of different type.
    #
    # Notice that there is no explicit type requirement for shape here (the 
    # Shape type hint is not enforced).  As such, any object that has a
    # __str__ and getArea methods (i.e., shares this same interface) can
    # be operated on by this processShape method.
    #
    print(f"shape = {shape}")                 # needs __str__ 
    print(f"area  = {shape.getArea()}")       # needs getArea
    print(f"type  = {type(shape).__name__}")


######################################################################

def main() -> None:
    s1 = Shape("blob")
    c1 = Circle("Luke", 2.0)
    t1 = Triangle("Bermuda", 2.0, 4.0)
    processShape(s1)
    processShape(c1)
    processShape(t1)

    w1 = Whatever("aalskdfjla")
    processShape(w1)

def old_main() -> None:
    s1 = Shape("blob")
    print(s1)
    print(s1.__str__())
    print(s1.getArea())

    print("-----------")

    c1 = Circle("Luke", 2.0)
    print(type(c1))
    print(c1.__str__())
    #print(Shape.__str__(c1))
    print(c1.getArea())

    print("-----------")

    t1 = Triangle("Bermuda", 2.0, 4.0)
    print(type(t1))
    print(t1)  # calling __str__ in Triangle

    print(Shape.__str__(t1))  # calling __str__ in Shape
    print(object.__str__(t1))  # calling __str__ in object

    print(t1.getArea())



if __name__ == "__main__":
    main()

 
