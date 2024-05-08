from Number import Number

######################################################################
class Complex(Number):
    __slots__ = ("_ivalue", "_digits")

    def __init__(self, value: float | int, ivalue: float | int, digits: int = 1) -> None:
        ''' initializer method for Float class
        Parameter:
            value: a float or integer of value
            ivalue: a float or intteger of an imaginary value
            digits: an integer representing # of digits beyond decimal to be displayed when printing
        '''
        #initialize by based on what type the value is
        if isinstance(value, int):
            super().__init__(int(value))
        if isinstance(value, float):
            super().__init__(float(value))

        #assign digits and ivalue
        self._digits = digits
        self._ivalue = ivalue
    
    def changeFormat(self, digits: int) -> None:
        ''' for this object, sets the number of digits to appear after the
            decimal when printed
        Parameters:
            digits: integer number of digits to appear after the decimal
        '''
        self._digits = digits
    
    def __add__(self, other: Number) -> Number:
        ''' method to add an Complex object with any object of type
            Float, Integer, float, int, or complex itlsef
        Parameters:
            other: an Float, Integer, float, int, or Complex object
        Returns:
            a Complex object
        '''

        # import Integer only when needed to avoid circular import
        from Integer import Integer
        from Float import Float

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Integer):
            return Complex(self._value + other._value, self._ivalue + other._value) 
        if isinstance(other, int):
            return Complex(self._value + other, self._ivalue + other)
        if isinstance(other, Float):
            return Complex(self._value + other._value, self._ivalue + other._value)
        if isinstance(other, float):
            return Complex(self._value + other, self._ivalue + other)
        return Complex(self._value + other._value, self._ivalue + other._ivalue)
        
    def __mul__(self, other: Number) -> Number:
        ''' method to mulitply an Complex object with any object of type
            Float, Integer, float, int or Complex
        Parameters:
            other: an Float, Integer, float, int, or Complex object
        Returns:
            a Complex object
        '''

        # import Integer only when needed to avoid circular import
        from Integer import Integer
        from Float import Float

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float, Complex])

        #calculate andreturn object based on what the other parameter is
        if isinstance(other, Integer):
            return Complex(self._value * other._value, self._ivalue * other._value)
        if isinstance(other, int):
            return Complex(self._value * other, self._ivalue * other)
        if isinstance(other, Float):
            return Complex(self._value * other._value, self._ivalue * other._value)
        if isinstance(other, float):
            return Complex(self._value * other, self._ivalue * other)
        return Complex(self._value * other._value - self._ivalue * other._ivalue, self._value * other._ivalue + self._ivalue * other._value)
    

    def __str__(self) -> str:
        ''' format the numeric parts to the complex number
        Parameter:
            value: a float or integer
            digits: an integer representing # of digits beyond
                decimal to be displayed when printing
        Returns:
            a string representing the Complex object
        '''
        from Integer import Integer
        from Float import Float

        if self._value == 0:
            if self._ivalue == 0:
                if isinstance(self._ivalue, int):
                    return f"0"
            else: 
                if self._ivalue == 1:
                    return f"i"
                elif self._ivalue == -1:
                    return f"-i"
                else:
                    if isinstance(self._ivalue, float):
                        return f"{self._ivalue:.{self._digits}f}i"
                    else:
                        return f"{self._ivalue}i"
        if isinstance(self._value, int):
            if self._ivalue < 0:
                newSelf = round(self._ivalue - (self._ivalue*2), self._digits)
                return f"{self._value} - {newSelf}i"
            elif self._ivalue == 0:
                return f"{self._value}"
            else:
                if isinstance(self._ivalue, int):
                    return f"{self._value} + {self._ivalue}i"
                else:
                    return f"{self._value} + {self._ivalue:.{self._digits}f}i"
        if isinstance(self._value, float):
            if self._ivalue < 0:
                newSelf = round(self._ivalue - (self._ivalue*2), self._digits)
                return f"{self._value:.{self._digits}f} - {newSelf}i"
            elif self._ivalue == 0:
                return f"{self._value:.{self._digits}f}"
            else:
                if isinstance(self._ivalue, int):
                    return f"{self._value:.{self._digits}f} + {self._ivalue}i"
                else:
                    return f"{self._value:.{self._digits}f} + {self._ivalue:.{self._digits}f}i"
        
