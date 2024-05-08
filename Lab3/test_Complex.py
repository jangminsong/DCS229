from Complex import Complex
from Float import Float
from Integer import Integer

import random
import pytest

@pytest.fixture
def random_integer() -> int:
    return random.randint(1,1000)

@pytest.fixture
def random_negative_integer() -> int:
    return -random.randint(1,1000)

@pytest.fixture
def random_float() -> float:
    return random.random() * 1000

@pytest.fixture
def random_negative_float() -> float:
    return -random.random() * 1000

@pytest.fixture
def zero_Complex() -> Complex:
    return Complex(0,0)

#positive int and positive int
@pytest.fixture
def random_int_and_int_Complex(random_integer: int) -> Complex:
    return Complex(random_integer,random_integer)

#positive int and negative int
@pytest.fixture
def random_int_and_negative_int_Complex(random_integer: int, random_negative_integer: int) -> Complex:
    return Complex(random_integer,random_negative_integer)

#positive int and positive float
@pytest.fixture
def random_int_and_float_Complex(random_integer: int, random_float: float) -> Complex:
    return Complex(random_integer, random_float)

#positive int and negative float
@pytest.fixture
def random_int_and_negative_float_Complex(random_integer: int, random_negative_float: float) -> Complex:
    return Complex(random_integer, random_negative_float)

#negative int and positive int
@pytest.fixture
def random_negative_int_and_int_Complex(random_negative_integer: int, random_integer: int) -> Complex:
    return Complex(random_negative_integer, random_integer)

#negative int and negative int
@pytest.fixture
def random_negative_int_and_negative_int_Complex(random_negative_integer: float) -> Complex:
    return Complex(random_negative_integer, random_negative_integer)

#negative int and positive float
@pytest.fixture
def random_negative_int_and_float_Complex(random_negative_integer: int, random_float: float) -> Complex:
    return Complex(random_negative_integer, random_float)

#positive float and positive int
@pytest.fixture
def random_float_and_int_Complex(random_float: float, random_integer: int) -> Complex:
    return Complex(random_float, random_integer)

#positive float and negative int
@pytest.fixture
def random_float_and_negative_int_Complex(random_float: float, random_negative_integer: int) -> Complex:
    return Complex(random_float, random_negative_integer)

#positive float and positive float
@pytest.fixture
def random_float_and_float_Complex(random_float) -> Complex:
    return Complex(random_float,random_float)

#positive float and negative float
@pytest.fixture
def random_float_and_negative_float_Complex(random_float: float, random_negative_float: float) -> Complex:
    return Complex(random_float,random_negative_float)
  
#negative float and positive int
@pytest.fixture
def random_negative_float_and_int_Complex(random_negative_float: float, random_integer: int) -> Complex:
    return Complex(random_negative_float, random_integer)

#negative float and negative int
@pytest.fixture
def random_negative_float_and_negative_int_Complex(random_negative_float: float, random_negative_integer: int) -> Complex:
    return Complex(random_negative_float, random_negative_integer)

#negative float and positive float
@pytest.fixture
def random_negative_float_and_float_Complex(random_negative_float: float, random_float: float) -> Complex:
    return Complex(random_negative_float,random_float)

#negative float and negative float
@pytest.fixture
def random_negative_float_and_negative_float_Complex(random_negative_float: float) -> Complex:
    return Complex(random_negative_float,random_negative_float)

#positive int and zero
@pytest.fixture
def random_int_and_zero_Complex(random_integer: int) -> Complex:
    return Complex(random_integer,0)

#negative int and zero
@pytest.fixture
def random_negative_int_and_zero_Complex(random_negative_integer: int) -> Complex:
    return Complex(random_negative_integer,0)

#positive float and zero
@pytest.fixture
def random_float_and_zero_Complex(random_float: float) -> Complex:
    return Complex(random_float,0)
   
#negative float and zero
@pytest.fixture
def random_negative_float_and_zero_Complex(random_negative_float: float) -> Complex:
    return Complex(random_negative_float,0)

#zero and positive int
@pytest.fixture
def random_zero_and_int_Complex(random_integer: int) -> Complex:
    return Complex(0,random_integer)

#zero and negative int
@pytest.fixture
def random_zero_and_negative_int_Complex(random_negative_integer: int) -> Complex:
    return Complex(0,random_negative_integer)

#zero and positive float
@pytest.fixture
def random_zero_and_float_Complex(random_float: float) -> Complex:
    return Complex(0,random_float)

#zero and negative float
@pytest.fixture
def random_zero_and_negative_float_Complex(random_negative_float: float) -> Complex:
    return Complex(0,random_negative_float)

@pytest.fixture
def changeFormat_zero_Complex(random_float: float) -> Complex:
    return Complex(random_float, random_float)

@pytest.fixture
def changeFormat_four_Complex(random_float: float) -> Complex:
    return Complex(random_float, random_float)

@pytest.fixture
def random_Integer(random_integer) -> Integer:
    return Integer(random_integer)

@pytest.fixture
def random_Float(random_float) -> Float:
    return Float(random_float) 
######################################################################
def test_Float_init(random_int_and_int_Complex: Complex, random_float_and_float_Complex: Complex, random_integer: int, random_float: float) -> None:
    ''' given: a float
        when:  an Float object is created using that float
        then:  an object of type Float, with appropriate _value 
               should be created
    '''
    assert(isinstance(random_int_and_int_Complex, Complex))
    assert(random_int_and_int_Complex._value == random_integer)
    assert(random_int_and_int_Complex._ivalue == random_integer)

    assert(isinstance(random_float_and_float_Complex, Complex))
    assert(random_float_and_float_Complex._value == random_float)
    assert(random_float_and_float_Complex._ivalue == random_float)

######################################################################
#zero
def test_zero_Complex_str(zero_Complex: Complex) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(zero_Complex.__str__() == "0")

#positive int and positive int
def test_int_and_int_Complex_str(random_int_and_int_Complex: Complex, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_int_Complex.__str__() == f"{random_integer} + {random_integer}i")
    
#positive int and negative int
def test_int_and_negative_int_Complex_str(random_int_and_negative_int_Complex: Complex, random_integer: int, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_negative_int_Complex.__str__() == f"{random_integer} - {random_negative_integer - (random_negative_integer*2)}i")

#positive int and positive float
def test_int_and_float_Complex_str(random_int_and_float_Complex: Complex, random_integer: int, random_float: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_float_Complex.__str__() == f"{random_integer} + {random_float:.1f}i")

#positive int and negative float
def test_int_and_negative_float_Complex_str(random_int_and_negative_float_Complex: Complex, random_integer: int, random_negative_float: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_negative_float_Complex.__str__() == f"{random_integer} - {random_negative_float - (random_negative_float*2):.1f}i")

#negative int and positive int
def test_negative_int_and_int_Complex_str(random_negative_int_and_int_Complex: Complex, random_integer: int, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_int_and_int_Complex.__str__() == f"{random_negative_integer} + {random_integer}i")
    
#negative int and negative int
def test_negative_int_and_negative_int_Complex_str(random_negative_int_and_negative_int_Complex: Complex, random_negative_integer) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_int_and_negative_int_Complex.__str__() == f"{random_negative_integer} - {random_negative_integer - (random_negative_integer*2)}i")

#negative int and positive float
def test_negative_int_and_float_Complex_str(random_negative_int_and_float_Complex: Complex, random_float: float, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_int_and_float_Complex.__str__() == f"{random_negative_integer} + {random_float:.1f}i")

#positive float and positive int
def test_float_and_int_Complex_str(random_float_and_int_Complex: Complex, random_float: float, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_float_and_int_Complex.__str__() == f"{random_float:.1f} + {random_integer}i")

#positive float and negative int
def test_float_and_negative_int_Complex_str(random_float_and_negative_int_Complex: Complex, random_float: float, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_float_and_negative_int_Complex.__str__() == f"{random_float:.1f} - {random_negative_integer - (random_negative_integer*2)}i")

#positive float and positive float
def test_float_and_float_Complex_str(random_float_and_float_Complex: Complex, random_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_float_and_float_Complex.__str__() == f"{random_float:.1f} + {random_float:.1f}i")

#positive float and negative float
def test_float_and_negative_float_Complex_str(random_float_and_negative_float_Complex: Complex, random_float: float, random_negative_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_float_and_negative_float_Complex.__str__() == f"{random_float:.1f} - {random_negative_float - (random_negative_float*2):.1f}i")
    
#negative float and positive int
def test_negative_float_and_int_Complex_str(random_negative_float_and_int_Complex: Complex, random_negative_float: float, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_float_and_int_Complex.__str__() == f"{random_negative_float:.1f} + {random_integer}i")

#negative float and negative int
def test_negative_float_and_int_Complex_str(random_negative_float_and_negative_int_Complex: Complex, random_negative_float: float, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_float_and_negative_int_Complex.__str__() == f"{random_negative_float:.1f} - {random_negative_integer - (random_negative_integer*2)}i")

#negative float and positive float
def test_negative_float_and_float_Complex_str(random_negative_float_and_float_Complex: Complex, random_negative_float: float, random_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_float_and_float_Complex.__str__() == f"{random_negative_float:.1f} + {random_float:.1f}i")

#negative float and negative float
def test_negative_float_and_negative_float_Complex_str(random_negative_float_and_negative_float_Complex: Complex, random_negative_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_float_and_negative_float_Complex.__str__() == f"{random_negative_float:.1f} - {(random_negative_float - (random_negative_float*2)):.1f}i")

#positive int and zero
def test_int_and_zero_Complex_str(random_int_and_zero_Complex: Complex, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_zero_Complex.__str__() == f"{random_integer}")
    
#negative int and zero
def test_int_and_zero_Complex_str(random_int_and_zero_Complex: Complex, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_int_and_zero_Complex.__str__() == f"{random_integer}")

#positive float and zero
def test_float_and_zero_Complex_str(random_float_and_zero_Complex: Complex, random_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_float_and_zero_Complex.__str__() == f"{random_float:.1f}")

#negative float and zero
def test_negative_float_and_zero_Complex_str(random_negative_float_and_zero_Complex: Complex, random_negative_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_negative_float_and_zero_Complex.__str__() == f"{random_negative_float:.1f}")

#zero and positive int
def test_zero_and_int_Complex_str(random_zero_and_int_Complex: Complex, random_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_zero_and_int_Complex.__str__() == f"{random_integer}i")

#zero and negative int
def test_zero_and_negative_int_Complex_str(random_zero_and_negative_int_Complex: Complex, random_negative_integer: int) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_zero_and_negative_int_Complex.__str__() == f"{random_negative_integer}i")

#zero and positive float
def test_zero_and_float_Complex_str(random_zero_and_float_Complex: Complex, random_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_zero_and_float_Complex.__str__() == f"{random_float:.1f}i")

#zero and negative float
def test_zero_and_negative_float_Complex_str(random_zero_and_negative_float_Complex: Complex, random_negative_float: float) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    assert(random_zero_and_negative_float_Complex.__str__() == f"{random_negative_float:.1f}i")

######################################################################

def test_changeFormat_zero_decimals(changeFormat_zero_Complex: Complex, random_float: float) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating zero decimals
        then:  __str__ should return an appropriate string with zero
            decimals
    '''
    assert(changeFormat_zero_Complex.__str__() == f"{random_float:.1f} + {random_float:.1f}i")
    changeFormat_zero_Complex.changeFormat(0)
    assert(changeFormat_zero_Complex.__str__() == f"{random_float:.0f} + {random_float:.0f}i")

def test_changeFormat_four_decimals(changeFormat_four_Complex: Complex, random_float: float) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating four decimals
        then:  __str__ should return an appropriate string with four
            decimals
    '''
    assert(changeFormat_four_Complex.__str__() == f"{random_float:.1f} + {random_float:.1f}i")
    changeFormat_four_Complex.changeFormat(4)
    assert(changeFormat_four_Complex.__str__() == f"{random_float:.4f} + {random_float:.4f}i")

######################################################################
# add Complex and Complex
def test_add_int_Complex_and_int_Complex(random_int_and_int_Complex: Complex) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_int_and_int_Complex
    c2 = random_int_and_int_Complex
    c3 = c1 + c2
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + c2._value)) # check for "close enough"

def test_add_float_Complex_and_int_Complex(random_float_and_float_Complex: Complex, random_int_and_int_Complex: Complex) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_float_and_float_Complex
    c2 = random_int_and_int_Complex
    c3 = c1 + c2
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + c2._value)) # check for "close enough"

def test_add_float_Complex_and_float_Complex(random_int_and_int_Complex: Complex, random_float_and_float_Complex: Complex) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_int_and_int_Complex
    c2 = random_float_and_float_Complex
    c3 = c1 + c2
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + c2._value)) # check for "close enough"

def test_add_float_Complex_and_float_Complex(random_float_and_float_Complex: Complex) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_float_and_float_Complex
    c2 = random_float_and_float_Complex
    c3 = c1 + c2
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + c2._value)) # check for "close enough"

# Complex and Integer
def test_add_int_Complex_and_Integer(random_int_and_int_Complex: Complex, random_Integer: Integer) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_int_and_int_Complex
    i1 = random_Integer
    c3 = c1 + i1
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + i1._value)) # check for "close enough"

# Complex and integer
def test_add_float_Complex_and_integer(random_float_and_float_Complex: Complex, random_integer: int) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_float_and_float_Complex
    i1 = random_integer
    c3 = c1 + i1
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + i1)) # check for "close enough"

# Complex and Float
def test_add_int_Complex_and_Float(random_int_and_int_Complex: Complex, random_Float: Float) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_int_and_int_Complex
    f1 = random_Float
    c3 = c1 + f1
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + f1._value)) # check for "close enough"

# Complex and float
def test_add_float_Complex_and_float(random_float_and_float_Complex: Complex, random_float: float) -> None:
    ''' given: two Float objects 
        when:  the objects are added
        then:  a new Float object should be returned with value
               being the sum of the values of the given objects
    '''
    c1 = random_float_and_float_Complex
    f1 = random_float
    c3 = c1 + f1
    assert(isinstance(c3, Complex))
    assert(c3._value == (c1._value + f1)) # check for "close enough"

######################################################################



# Complex and Float
# Complex and float

# def test_add_Float_and_float() -> None:
#     ''' given: an Float object and a float object
#         when:  the objects are added
#         then:  a new Float object should be returned with value
#                being the sum of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     f2 = random.random() * 1000
#     f3 = f1 + f2
#     assert(isinstance(f3, Float))
#     assert(abs(f3._value - (f1._value + f2)) < 1e-6) # check for "close enough"

# def test_add_Float_and_int() -> None:
#     ''' given: an Float object and an int object
#         when:  the objects are added
#         then:  a new Float object should be returned with value
#                being the sum of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     i1 = random.randint(1,1000)
#     f2 = f1 + i1
#     assert(isinstance(f2, Float))
#     assert(abs(f2._value - (f1._value + i1)) < 1e-6) # check for "close enough"

# def test_add_Float_and_Integer() -> None:
#     ''' given: an Float object and an Integer object
#         when:  the objects are added
#         then:  a new Float object should be returned with value
#                being the sum of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     i1 = Integer(random.randint(1,1000))
#     f2 = f1 + i1
#     assert(isinstance(f2, Float))
#     assert(abs(f2._value - (f1._value + i1._value)) < 1e-6) # check for "close enough"

# ######################################################################

# def test_multiply_Float_and_Float() -> None:
#     ''' given: two Float objects 
#         when:  the objects are multiplied
#         then:  a new Float object should be returned with value
#                being the product of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     f2 = Float(random.random() * 1000)
#     f3 = f1 * f2
#     assert(isinstance(f3, Float))
#     assert(abs(f3._value - (f1._value * f2._value)) < 1e-6) # check for "close enough"
    
# def test_multiply_Float_and_float() -> None:
#     ''' given: an Float object and a float object
#         when:  the objects are multiplied
#         then:  a new Float object should be returned with value
#                being the product of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     f2 = random.random() * 1000
#     f3 = f1 * f2
#     assert(isinstance(f3, Float))
#     assert(abs(f3._value - (f1._value * f2)) < 1e-6) # check for "close enough"

# def test_multiply_Float_and_int() -> None:
#     ''' given: an Float object and an int object
#         when:  the objects are multiplied
#         then:  a new Float object should be returned with value
#                being the product of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     i1 = random.randint(1,1000)
#     f2 = f1 * i1
#     assert(isinstance(f2, Float))
#     assert(abs(f2._value - (f1._value * i1)) < 1e-6) # check for "close enough"

# def test_multiply_Float_and_Integer() -> None:
#     ''' given: an Float object and an Integer object
#         when:  the objects are multiplied
#         then:  a new Float object should be returned with value
#                being the product of the values of the given objects
#     '''
#     f1 = Float(random.random() * 1000)
#     i1 = Integer(random.randint(1,1000))
#     f2 = f1 * i1
#     assert(isinstance(f2, Float))
#     assert(abs(f2._value - (f1._value * i1._value)) < 1e-6) # check for "close enough"