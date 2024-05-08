from typing import Callable

def func(other_func: Callable) -> None:
    return other_func('hello world')

def outer_func(param: int) -> Callable:
    def inner_func() -> int:
        print('before')
        value = param*param
        print('after')
        return value
    return inner_func

# def outer_func(param: int) -> int:
#     def inner_func() -> int:
#         print('before')
#         value = param*param
#         print('after')
#         return value
#     result = inner_func()
#     return result

#a decorator is a function that wraps another function
def my_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> int:
        print(f'before calling {func.__name__}')
        value = func(*args, **kwargs)
        print(f'after calling {func.__name__}')
        return value
    return wrapper #returning a function, not the function call result
    
@my_decorator
def computeSum(a: int, b: int, debug: bool = False) -> int:
    if debug:
        print('We are debugging')
    return a+b

# computeSum = my_decorator(computeSum)

@my_decorator
def computeProduct(a,b,c,d,e) -> int:
    return a*b*c*d*e

# computeProduct = my_decorator(computeProduct)

# def computeSum(a: int, b: int, *args: tuple, **kwargs: dict) -> int:
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'*args = {args}  type: {type(args)}')
#     print(f'kwargs = {kwargs}  type: {type(kwargs)}')
#     print('-' * 40)
#     #*args allows us to pass in an arbitrary number of arguments
#     result = int(a) +int(b)
#     for arg in args:
#         result += int(arg) # add each element from the args tuple
#     try:
#         value = kwargs['expected']
#         print(f'the excpted result is {value}')
#     except:
#         pass
#     return result


def main() -> None:
    # print('func function')
    # func(print)

    # print()

    # print('outer func')
    # result = outer_func(4)
    # print(type(result))
    # print(result)

    # print()

    # print('outer func')
    # print(outer_func(4))

    print()

    print('my_decorator')
    result = computeSum(1,2, True)
    print(f'result = {result}')
    print()
    result = computeProduct(1,2,3,4,5)
    print(f'result = {result}')

    # print()

    # print('computeSum args')
    # result = computeSum(1,2,3,4, expected = 33, hello = 40)
    # print(f'result = {result}')
    # print()
    # result = computeSum(1,2,3,4, hello = 40)
    # print(f'result = {result}')


main()