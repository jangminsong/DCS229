'''
Jangmin Song
Lab 3 
2/16/24
No source used.
'''

from Number import Number

######################################################################
class Integer(Number):
    def __init__(self, value: int) -> None:
        ''' initializer method for Integer class
        Parameter:
            value: an integer
        Raises:
            ValueError if value cannot be converted to int
        '''
        super().__init__(int(value))

    def __add__(self, other: 'Float | Integer | Complex') ->'Float | Integer | Complex':
        ''' method to add an Integer object with any object of type
            Integer, Float, int, or float, or Complex
        Parameters:
            other: Number object
        Returns:
            a string of Number object
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float, or Complex
        '''
        # import Float only when needed to avoid circular import
        # (see https://bit.ly/488rlWX)
        from Float import Float
        from Complex import Complex

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Integer(self._value + other)
        if isinstance(other, Complex):
            return Complex(self._value + other._value, self._value + other._ivalue)
        return Integer(self._value + other._value)

    def __mul__(self, other: 'Float | Integer | Complex') ->'Float | Integer | Complex':
        ''' method to mulitply an Integer object with a Number object
        Parameters:
            other: Number object
        Returns:
            a string of Number object
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float, or Complex
        '''
        # import Float only when needed to avoid circular import
        # (see https://bit.ly/488rlWX)
        from Float import Float
        from Complex import Complex

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Integer(self._value * other)
        if isinstance(other, Complex):
            return Complex(self._value * other._value, self._value * other._ivalue)
        return Integer(self._value * other._value)