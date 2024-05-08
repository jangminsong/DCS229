from Integer import Integer
from Float import Float
from Complex import Complex

import random
import pytest

#pytest fixture
@pytest.fixture
def zero_Integer() -> Integer:
    return Integer(0)

@pytest.fixture
def random_integer() -> int:
    return random.randint(1,1000)

@pytest.fixture
def random_negative_integer() -> int:
    return -random.randint(1,1000)

@pytest.fixture
def random_Integer(random_integer) -> Integer:
    return Integer(random_integer)

@pytest.fixture
def random_negative_Integer(random_negative_integer) -> Integer:
    return Integer(random_negative_integer)

@pytest.fixture
def random_float() -> float:
    return random.random() * 1000

@pytest.fixture
def random_Float(random_float) -> Float:
    return Float(random_float) 

@pytest.fixture
def random_int_Complex(random_integer) -> Complex:
    return Complex(random_integer,random_integer)

@pytest.fixture
def random_float_Complex(random_float) -> Complex:
    return Complex(random_float,random_float)
######################################################################

def test_Integer_init(random_Integer: Integer, random_integer: int) -> None:
    ''' given: an int
        when:  an Integer object is created using that int
        then:  an object of type Integer, with appropriate _value 
               should be created
    '''
    assert(isinstance(random_Integer, Integer))
    assert(random_Integer._value == random_integer)

######################################################################

def test_zero_Integer_str(zero_Integer: Integer) -> None:
    ''' given: an Integer object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''
    assert(zero_Integer.__str__() == "0")

def test_positive_Integer_str(random_Integer: Integer, random_integer: int) -> None:
    ''' given: an Integer object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''
    assert(random_Integer.__str__() == str(random_integer))

def test_negative_Integer_str(random_negative_Integer: Integer, random_negative_integer: int) -> None:
    ''' given: an Integer object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''
    assert(random_negative_Integer.__str__() == str(random_negative_integer))

######################################################################
def test_add_Integer_and_Integer(random_Integer: Integer) -> None:
    ''' given: two Integer objects 
        when:  the objects are added
        then:  a new Integer object should be returned with value
               being the sum of the values of the given objects
    '''
    i1 = random_Integer
    i2 = random_Integer
    i3 = i1 + i2
    assert(isinstance(i3, Integer))
    assert(i3._value == i1._value + i2._value)
    
def test_add_Integer_and_int(random_Integer: Integer, random_integer: int) -> None:
    ''' given: an Integer object and an int object
        when:  the objects are added
        then:  a new Integer object should be returned with value
               being the sum of the values of the given objects
    '''
    i1 = random_Integer
    i2 = random_integer
    i3 = i1 + i2
    assert(isinstance(i3, Integer))
    assert(i3._value == i1._value + i2)

def test_add_Integer_and_float(random_Integer: Integer, random_float: float) -> None:
    ''' given: an Integer object and a float object
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    i1 = random_Integer
    f1 = random_float
    f2 = i1 + f1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (i1._value + f1)) < 1e-6) # check for "close enough"

def test_add_Integer_and_Float(random_Integer: Integer, random_Float: Float) -> None:
    ''' given: an Integer object and a Float object
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    i1 = random_Integer
    f1 = random_Float
    f2 = i1 + f1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (i1._value + f1._value)) < 1e-6) # check for "close enough"

def test_add_Integer_and_int_Complex(random_Integer: int, random_int_Complex: Complex) -> None:
    ''' given: an Float object and an Complex object
        when:  the objects are added
        then:  a new Complex object should be returned with value
               being the sum of the values of the given objects and the imaginary value
    '''
    i1 = random_Integer
    c1 = random_int_Complex
    c2 = i1 + c1
    assert(isinstance(c2, Complex))
    assert(c2._value == i1._value + c1._value) # check for "close enough"

def test_add_Integer_and_float_Complex(random_Integer: int, random_float_Complex: Complex) -> None:
    ''' given: an Float object and an Complex object
        when:  the objects are added
        then:  a new Complex object should be returned with value
               being the sum of the values of the given objects and the imaginary value
    '''
    i1 = random_Integer
    c1 = random_float_Complex
    c2 = i1 + c1
    assert(isinstance(c2, Complex))
    assert(c2._value == i1._value + c1._value) # check for "close enough"

######################################################################
def test_multiply_Integer_and_Integer(random_Integer: Integer) -> None:
    ''' given: two Integer objects 
        when:  the objects are multiplied
        then:  a new Integer object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    i2 = random_Integer
    i3 = i1 * i2
    assert(isinstance(i3, Integer))
    assert(i3._value == i1._value * i2._value)

def test_multiply_Integer_and_int(random_Integer: Integer, random_integer: int) -> None:
    ''' given: an Integer object and an int object
        when:  the objects are multiplied
        then:  a new Integer object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    i2 = random_integer
    i3 = i1 * i2
    assert(isinstance(i3, Integer))
    assert(i3._value == i1._value * i2)

def test_multiply_Integer_and_float(random_Integer: Integer, random_float: float) -> None:
    ''' given: an Integer object and a float object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    f1 = random_float
    f2 = i1 * f1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (i1._value * f1)) < 1e-6) # check for "close enough"

def test_multiply_Integer_and_Float(random_Integer: Integer, random_Float: Float) -> None:
    ''' given: an Integer object and a Float object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    f1 = random_Float
    f2 = i1 * f1
    assert(isinstance(f2, Float))
    assert(abs(f2._value - (i1._value * f1._value)) < 1e-6) # check for "close enough"

def test_multiply_Integer_and_int_Complex(random_Integer: Integer, random_int_Complex: Complex) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    c1 = random_int_Complex
    c2 = i1 * c1
    assert(isinstance(c2, Complex))
    assert(c2._value == c1._value * i1._value) # check for "close enough"

def test_multiply_Integer_and_float_Complex(random_Integer: Integer, random_float_Complex: Complex) -> None:
    ''' given: an Float object and an Integer object
        when:  the objects are multiplied
        then:  a new Float object should be returned with value
               being the product of the values of the given objects
    '''
    i1 = random_Integer
    c1 = random_float_Complex
    c2 = i1 * c1
    assert(isinstance(c2, Complex))
    assert(abs(c2._value - (i1._value * c1._value)) < 1e-6) # check for "close enough"