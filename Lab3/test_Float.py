from Float import Float
from Integer import Integer
from Complex import Complex

import random
import pytest

#pytest fixture
@pytest.fixture
def zero_Float() -> Float:
    return Float(0)

@pytest.fixture
def four_zero_Float() -> Float:
    return Float(0, 4)

@pytest.fixture
def random_float() -> float:
    return random.random() * 1000

@pytest.fixture
def random_negative_float() -> float:
    return -random.random() * 1000

@pytest.fixture
def random_Float(random_float) -> Float:
    return Float(random_float) 

@pytest.fixture
def random_negative_Float(random_negative_float) -> Float:
    return Float(random_negative_float) 

@pytest.fixture
def random_positive_Float_str_four_decimals(random_float) -> Float:
    return Float(random_float,4) 

@pytest.fixture
def random_positive_Float_str_zero_decimals(random_float) -> Float:
    return Float(random_float,0) 

@pytest.fixture
def random_negative_Float_str_four_decimals(random_negative_float) -> Float:
    return Float(random_negative_float,4) 

@pytest.fixture
def random_negative_Float_str_zero_decimals(random_negative_float) -> Float:
    return Float(random_negative_float,0) 

@pytest.fixture
def random_integer() -> int:
    return random.randint(1,1000)

@pytest.fixture
def random_Integer(random_integer) -> Integer:
    return Integer(random_integer)

@pytest.fixture
def random_int_Complex(random_integer) -> Complex:
    return Complex(random_integer,random_integer)

@pytest.fixture
def random_float_Complex(random_float) -> Complex:
    return Complex(random_float,random_float)
######################################################################

def test_Float_init(random_Float: Float, random_float: float) -> None:
    ''' given: a float
        when:  an Float object is created using that float
        then:  an object of type Float, with appropriate _value 
               should be created
    '''
    assert(isinstance(random_Float, Float))
    assert(random_Float._value == random_float)

######################################################################

def test_zero_Float_str_two_decimals(zero_Float: Float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(zero_Float.__str__() == "0.00")

def test_zero_Float_str_four_decimals(four_zero_Float: Float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default four decimals
    '''
    assert(four_zero_Float.__str__() == "0.0000")

def test_positive_Float_str_two_decimals(random_Float: Float, random_float: float) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_Float.__str__() == f"{random_float:.2f}")

def test_positive_Float_str_four_decimals(random_positive_Float_str_four_decimals: Float, random_float: float) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_positive_Float_str_four_decimals.__str__() == f"{random_float:.4f}")

def test_positive_Float_str_zero_decimals(random_positive_Float_str_zero_decimals: Float, random_float: float) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_positive_Float_str_zero_decimals.__str__() == f"{random_float:.0f}")

def test_negative_Float_str_two_decimals(random_negative_Float: Float, random_negative_float: float) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_negative_Float.__str__() == f"{random_negative_float:.2f}")

def test_negative_Float_str_four_decimals(random_negative_Float_str_four_decimals: Float, random_negative_float: float) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_negative_Float_str_four_decimals.__str__() == f"{random_negative_float:.4f}")

def test_negative_Float_str_zero_decimals(random_negative_Float_str_zero_decimals: Float, random_negative_float: float) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    assert(random_negative_Float_str_zero_decimals.__str__() == f"{random_negative_float:.0f}")

######################################################################

def test_changeFormat_zero_decimals(random_Float: Float, random_float: float) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating zero decimals
        then:  __str__ should return an appropriate string with zero
            decimals
    '''
    assert(random_Float.__str__() == f"{random_float:.2f}")
    random_Float.changeFormat(0)
    assert(random_Float.__str__() == f"{random_float:.0f}")

def test_changeFormat_four_decimals(random_Float: Float, random_float: float) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating four decimals
        then:  __str__ should return an appropriate string with four
            decimals
    '''
    assert(random_Float.__str__() == f"{random_float:.2f}")
    random_Float.changeFormat(4)
    assert(random_Float.__str__() == f"{random_float:.4f}")

######################################################################

# your pytest functions for __add__ and __mul__ go below...

def test_add_Float_and_Float(random_Float: Float) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    f1 = random_Float
    f2 = random_Float
    f3 = f1 + f2
    assert(isinstance(f3, Float))
    assert(abs(f3._value - (f1._value + f2._value)) < 1e-6) # check for "close enough"
    
def test_add_Float_and_float(random_Float: Float, random_float: float) -> None:
    ''' given: an Float object and a float object
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    f1 = random_Float
    f2 = random_float
    f3 = f1 + f2
    assert(isinstance(f3, Float))
    assert(abs(f3._value - (f1._value + f2)) < 1e-6) # check for "close enough"

def test_add_Float_and_int(random_Float: Float, random_integer: int) -> None:
    ''' given: an Float object and an int object
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_integer
    f2 = f1 + i1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (f1._value + i1)) < 1e-6) # check for "close enough"

def test_add_Float_and_Integer(random_Float: Float, random_Integer: Integer) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_Integer
    f2 = f1 + i1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (f1._value + i1._value)) < 1e-6) # check for "close enough"

def test_add_Float_and_int_Complex(random_Float: Float, random_int_Complex: Complex) -> None:
    ''' given: an Float object and an Complex object
        when:  the objects are added
        then:  a new Complex object should be returned with value
               being the sum of the values of the given objects and the imaginary value
    '''
    f1 = random_Float
    i1 = random_int_Complex
    f2 = f1 + i1
    assert(isinstance(f2, Complex))
    assert(abs(f2._value - (f1._value + i1._value)) < 1e-6) # check for "close enough"

def test_add_Float_and_float_Complex(random_Float: Float, random_float_Complex: Complex) -> None:
    ''' given: an Float object and an Complex object
        when:  the objects are added
        then:  a new Complex object should be returned with value
               being the sum of the values of the given objects and the imaginary value
    '''
    f1 = random_Float
    i1 = random_float_Complex
    f2 = f1 + i1
    assert(isinstance(f2, Complex))
    assert(abs(f2._value - (f1._value + i1._value)) < 1e-6) # check for "close enough"

######################################################################

def test_multiply_Float_and_Float(random_Float: Float) -> None:
    ''' given: two Float objects 
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    f2 = random_Float
    f3 = f1 * f2
    assert(isinstance(f3, Float))
    assert(abs(f3._value - (f1._value * f2._value)) < 1e-6) # check for "close enough"
    
def test_multiply_Float_and_float(random_Float: Float, random_float: float) -> None:
    ''' given: an Float object and a float object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    f2 = random_float
    f3 = f1 * f2
    assert(isinstance(f3, Float))
    assert(abs(f3._value - (f1._value * f2)) < 1e-6) # check for "close enough"

def test_multiply_Float_and_int(random_Float: Float, random_integer: int) -> None:
    ''' given: an Float object and an int object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_integer
    f2 = f1 * i1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (f1._value * i1)) < 1e-6) # check for "close enough"

def test_multiply_Float_and_Integer(random_Float: Float, random_Integer: Integer) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_Integer
    f2 = f1 * i1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (f1._value * i1._value)) < 1e-6) # check for "close enough"

def test_multiply_Float_and_int_Complex(random_Float: Float, random_int_Complex: Complex) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_int_Complex
    f2 = f1 * i1
    assert(isinstance(f2, Complex))
    assert(abs(f2._value - (f1._value * i1._value)) < 1e-6) # check for "close enough"

def test_multiply_Float_and_Integer(random_Float: Float, random_float_Complex: Complex) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    f1 = random_Float
    i1 = random_float_Complex
    f2 = f1 * i1
    assert(isinstance(f2, Complex))
    assert(abs(f2._value - (f1._value * i1._value)) < 1e-6) # check for "close enough"