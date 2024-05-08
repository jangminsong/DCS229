from abc import ABC, abstractmethod

class Parent(ABC):
    def __init__(self, value: int) -> None:
        self._value = value


    #@ is a python decorator
    @abstractmethod
    def commonMethod(self) -> None: 
        print(f"{self._value}")

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self._value}"

class Child(Parent):
    def __init__(self, value: int, name: str) -> None:
        super().__init__(value)
        self._name = name

    def commonMethod(self) -> None:
        print(f"{self._name}: {self._value}")

def main() -> None:
    # p = Parent(39)
    # p.commonMethod()

    c = Child(39, "name")
    c.commonMethod()
    print(c)

    print(f"{isinstance(c, Child)}")
    # print(f"{isinstance(p, Parent)}")
    # print(f"{isinstance(, ABC)}")

if __name__ == "__main__":
    main()
