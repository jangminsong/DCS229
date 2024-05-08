from abc import ABC, abstractmethod
from ast import Num

class Number(ABC): 
    __slots__ = ('_value')

    def __init__(self, value: int or float) -> None:
        self._value = value
    
    @abstractmethod
    def __add__(self, other: 'Number') -> 'Number':
        pass

    @abstractmethod
    def __mul__(self, other: 'Number') -> 'Number':
        pass

    #not abstract so that subclasses can use them
    def __str__(self) -> str:
        return f"{self._value}"

class Integer(Number):
    def __init__(self, value: int) -> None:
        super().__init__(int(value))

    #inherited from Number as abstractmethod, but it's override
    def __add__(self, other: 'Number') -> 'Number':
        if isinstance(other, float):
            return Float(self._value + other._value)
        return Integer(self._value + other._value) 

    def __mul__(self, other: 'Number') -> 'Number':
        if isinstance(other, float):
            return Float(self._value * other._value)
        return Integer(self._value * other._value) 
    
class Float(Number):
    __slots__ = ('_digits')

    def __init__(self, value: float or int, digits: int = 2) -> None:
        super().__init__(value)
        self._digits = digits

    def __add__(self, other: 'Number') -> 'Number':
        result = self._value + other._value
        return Float(result)

    def __mul__(self, other: 'Number') -> 'Number':
        result = self._value * other._value
        return Float(result)
    
    def changeFormat(self, digits: int) -> None:
        self._digits = digits

    def __str__(self) -> str:
        return f'{self._value:.{self._digits}f}'

def main() -> None:
    #n = Number(5)
    i1 = Integer(5)
    i2 = Integer(7)
    i3 = i1+i2
    i4 = i1*i2
    print(i3)
    print(i4)

    f1 = Float(5.12)
    f2 = Float(3.33)
    f3 = f1+f2
    f4 = f1*f2
    f5 = f1+i2
    f6 = f1*i2
    print(f'{f1} + {f2} = {f3}')
    print(f'{f1} * {f2} = {f4}')
    print(f'{f1} + {i2} = {f5}')
    print(f'{f1} * {i2} = {f6}')

if __name__ == "__main__":
    main()