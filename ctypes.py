from ctypes import *

class MyList: 
    __slots__ = ('_array', '_capacity', '_num_stored')

    def __init__(self) -> None:
        self._num_stored = 0
        self._capacity = 2
        #here, the ctypes stuff hapeens

    def _make_array(self, capacity: int) -> 'ctypes array':
        ArrayType = capacity * c_int # a class type
        return ArrayType() #return an object of ctypes array of length capacity

    def __len__(self) -> int:
        return self._num_stored
    
    def append(self, value: int) -> None:
        if self._num_stored < self._capacity:
            self._array[self._num_stored] = value
            self._num_stored = 1
        else:
            
    def __str__(self) -> str:
        #return "[" + "," .join(i for i in self._array) + "]"
        string = "["
        for i in range(self._num_stored):
            string += str(self._array[i]) + ","
        string += "]"
        return string


def main() -> None:
    n = MyList()
    print(f"len of n = {len(n)}")
    print(f"n = {n}")

main()

    