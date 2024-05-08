'''
Jangmin Song
Lab 3 
2/16/24
No source used.
'''

from Number import Number

######################################################################
class Float(Number):
    __slots__ = ("_digits")

    def __init__(self, value: float | int, digits: int = 2) -> None:
        ''' initializer method for Float class
        Parameter:
            value: a float or integer
            digits: an integer representing # of digits beyond
                decimal to be displayed when printing
        Raises:
            ValueError if value cannot be converted to float
        '''
        super().__init__(float(value))
        self._digits = digits

    def __add__(self, other: 'Float | Integer | Complex') ->'Float | Integer | Complex':
        ''' method to add an Float object with any object of type
            Float, Integer, float, Complex or int
        Parameters:
            other: an Float, Integer, float, Complex or int object
        Returns:
            a Float object
        Raises:
            TypeError if the type of other is not one of Float, Integer, float, Complex or int
        '''

        # import Integer only when needed to avoid circular import
        from Integer import Integer
        from Complex import Complex

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Integer):
            return Float(self._value + other._value)
        if isinstance(other, int):
            return Float(self._value + other)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, Complex):
            return Complex(self._value + other._value, self._value + other._ivalue)
        return Float(self._value + other._value)
        
    def __mul__(self, other: 'Float | Integer | Complex') ->'Float | Integer | Complex':
        ''' method to mulitply an Integer object with any object of type
            Float, Integer, float, Complex or int
        Parameters:
            other: an Float, Integer, float, Complex or int object
        Returns:
            a Float object
        Raises:
            TypeError if the type of other is not one of Float, Integer, float, Complex or int
        '''

        # import Integer only when needed to avoid circular import
        from Integer import Integer
        from Complex import Complex

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Integer):
            return Float(self._value * other._value)
        if isinstance(other, int):
            return Float(self._value * other)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, Complex):
            return Complex(self._value * other._value, self._value * other._ivalue)
        return Float(self._value * other._value)

    def changeFormat(self, digits: int) -> None:
        ''' for this object, sets the number of digits to apepear after the
            decimal when printed
        Parameters:
            digits: integer number of digits to appear after the decimal
        Raises:
            ValueError if digits cannot be converted to int
        '''
        self._digits = int(digits)

    def __str__(self) -> str:
        ''' returns a string representation of this Number object
        Returns:
            a string representing the Number object
        '''
        return f"{self._value:.{self._digits}f}"