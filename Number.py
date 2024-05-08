from abc import ABC, abstractmethod

class Number(ABC): 
    __slots__ = ('_value')

    def __init__(self, value: int or float) -> None:
        '''
        This function takes the value and decides weather the value is an integer or a float
        Parameter: 
            self -> global variable that is shared among the class
            value: int or float -> an integer or a float 
        Returns: 
            None
        '''
        if isinstance(value, int): #if the value is an int
            self._value: int = value #assign the value
        elif isinstance(value, float): #if the value is an float
            self._value: float = value #assign the value
        else: 
            raise TypeError(f"The given value is not integer or float. It is {type(value)}.") #raise an error if the value is not an int or a float
    
    def __add__(self, other: 'Number') -> 'Number':
        '''
        This function takes the value and adds with self
        Parameter: 
            self -> global variable that is shared among the class
            other: 'Number' -> other number that gets added
        Returns: 
            sum -> the sum of self and other
        '''
        if not isinstance(other, Number): #if other is not a Number class
            raise TypeError(f'The given value is not a Number class. It is {type(other)}.') #raise a type error 
        else:
            sum = self._value + other._value #add two values
            return sum #returns the sum
        
    def __mul__(self, other: 'Number') -> 'Number':
        '''
        This function takes the value and multiplies with self
        Parameter: 
            self -> global variable that is shared among the class
            other: 'Number' -> other number that gets multiplied
        Returns: 
            product -> the product of self and other
        '''
        if not isinstance(other, Number): #if other is not a Number class
            raise TypeError(f'The given value is not a Number class. It is {type(other)}.') #raise a type error 
        else:
            product = self._value * other._value #multiply two values
            return product #returns the product
    
    def __str__(self) -> str:
        '''
        This function takes the parameter and returns the string of the parameter
        Parameter: 
            self -> global variable that is shared among the class
        Returns: 
            str(self._value) -> string of self._value
        '''
        return str(self._value) #returns the string of self._value
    
######################################################################

class Integer(Number):
    def __init__(self, value: int) -> None:
        '''
        This function takes the value initializes as Integer class
        Parameter: 
            self -> global variable that is shared among the class
            value: int -> must be an integer
        Returns: 
            None
        '''
        if not isinstance(value, int): #if other is not an int
            raise TypeError(f'The given value is not an integer. It is {type(value)}.') #raise an error
        else:
            super().__init__(value) #initializing value

######################################################################
        
class Float(Number):
    __slots__ = ('_decimal')

    def __init__(self, value: float, decimal: int = 2) -> None:
        '''
        This function takes the value initializes as Float class
        Parameter: 
            self -> global variable that is shared among the class
            value: 'Number' -> must be a float
            decimal: int = 2 -> an int that rounds the float with that decimal place
        Returns: 
            None
        '''
        if not isinstance(value, float):  #if other is not an float
            raise TypeError(f'The given value is not a float. It is {type(value)}.') #raise an error
        else:
            super().__init__(value) #initializing value
            self._decimal = round(self._value, decimal) #round the decimal number with initial decimal places

    def changeFormat(self, newDecimal: int) -> None:
        '''
        This function takes the self and rounds up with the newDecimal parameters given
        Parameter: 
            self -> global variable that is shared among the class
            newDecimal: int -> an int that rounds the float with that decimal place
        Returns: 
            None
        '''
        self._decimal = round(self._value, newDecimal) #rounds up the float with the new decimal place
    
    def __str__(self) -> str:
        '''
        This function takes the parameter and returns the string of the parameter
        Parameter: 
            self -> global variable that is shared among the class
        Returns: 
            str(self._decimal) -> string of self._decimal
        '''
        return str(self._decimal) #returns the string of self._decimal


def main() -> None:
    print('Tests')
    m1 = Number(11)
    print(m1)
    m2 = Number(2)
    m3 = Number(2.2849382)
    m4 = Integer(6)
    m5 = Integer(19)
    m6 = Float(4.123456789)
    m7 = Float(5.123456789)
    print(m1.__add__(m2))
    print(m1.__mul__(m2))

    print(f'the type of {m1.__mul__(m2)} is {type(m1.__str__())}')

    print()

    number = 3.14159265358979
    places = 3
    print(f'To {places} decimal places: {number:.{places}f}')
    m6.changeFormat(5)
    print(f'Float with cutting the decimal place at 5 is {m6}')
    print()

    print(f'Integer({m4}) + Integer({m5}) is: {m4.__add__(m5)}')
    print(f'Integer({m4}) * Integer({m5}) is: {m4.__mul__(m5)}')
    print(f'Float({m6}) + Float({m7}) is: {Float(m6.__add__(m7))}')
    print(f'Float({m6}) * Float({m7}) is: {Float(m6.__mul__(m7))}')
    print(f'Float({m6}) * Integer({m5}) is: {m6.__mul__(m5)}')
    print(f'Float({m6}) + Integer({m5}) is: {m6.__add__(m5)}')



if __name__ == "__main__":
    main()