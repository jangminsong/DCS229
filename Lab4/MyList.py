from ctypes import *
import math
from typing import TypeVar
T = TypeVar('T')  # used to represent an arbitrary type

class MyList:
    __slots__ = ('_n', '_capacity', '_array')

    # class-level variables for stats
    _resizes: int = 0  # total number of resizes
    _copies:  int = 0  # number of array-to-array copies during resizing

    @classmethod
    def resetStats(cls) -> None:
        MyList._resizes = 0
        MyList._copies = 0

    @classmethod
    def getStatsDict(cls) -> dict:
        return {"resizes" : MyList._resizes, \
                "copies"  : MyList._copies}

    def __init__(self):
        self._n        = 0  # number of actual elements currently in the list
        self._capacity = 1  # default MyList capacity

        self._array    = self._make_array(self._capacity)

    def _make_array(self, capacity: int) -> 'ctypes array':
        ''' private method to reserve space for a low-level array of the
            given capacity
        Parameters:
            capacity: integer size of the array
        Returns:
            a ctypes low-level array
        '''
        ArrayType = (capacity * c_int)  # defined in ctypes
        return ArrayType() # create and return an array of py_object of size capacity

    def __len__(self) -> int:
        ''' returns number of actual elements in the array
        Returns:
            integer count of number of elements in the array
        '''
        return self._n

    def __getitem__(self, index: int) -> T:
        ''' returns the item in the array at the given index
        Parameters:
            index: integer index between 0 and self.len() - 1
        Returns:
            item of type T at given index
        Raises:
            IndexError exception if index is invalid
        '''
        if isinstance(index, int) and 0 <= index and index < self._n: #right index and within the right range
            return self._array[index]
        else:
            raise IndexError(f"index is invalid") 

    def __setitem__(self, index: int, item: T) -> None:
        ''' sets the entry in the array at the given index to the given item
        Parameters:
            index: integer index between 0 and self.len() - 1
            item:  type-T element (must match type of entries already in list)
        Returns:
            None
        Raises:
            IndexError exception of index is invalid
            TypeError exception if type of item does not match types in array
        '''
        if isinstance(index, int) and 0 <= index and index < self._n and isinstance(item, type(self._array[0])): #right index and within the right range
            self._array[index] = item
        elif index > self._n-1:
            raise IndexError(f'index is invalid')
        elif not isinstance(item, type(self._array[0])):
            raise TypeError(f'does not match the type')
        elif not isinstance(index, int): 
            raise IndexError(f'index is invalid')
            

    def append(self, item: T) -> None:
        ''' appends the given item to the array, increasing the capacity of
            the array as necessary
        Parameters:
            item: type-T element to append to the array
        Return:
            None
        Raises:
            TypeError exception if type of item does not match types in array
        '''
        if isinstance(item, type(self._array[0])):
            if self._n == self._capacity:
                self._resize(self._capacity * 2)
                # self._resize(round(self._capacity * 1.5))
                # self._resize(math.ceil(self._capacity * 1.25))
                # self._resize(self._capacity + 1024)
                # self._resize(self._capacity + 4096)
                # self._resize(self._capacity + 16384)
                
            self._array[self._n] = item
            self._n += 1
        else:
            raise TypeError(f'type of item does not match types in array')

    def _resize(self, capacity: int) -> None:
        ''' private method to resize the array to a specific capacity,
            copying elements from the old array into the new
        Parameters:
            capacity: integer size of the new array
        Returns:
            nothing
        '''
        newArray = self._make_array(capacity)
        for i in range(self._n):
            newArray[i] = self._array[i]
        self._array = newArray
        self._capacity = capacity
        MyList._resizes += 1
        MyList._copies += self._n

    def __str__(self) -> str:
        ''' a string representation of this MyList
        Returns:
            a printable string format of the MyList contents
        '''
        list = "[" + ", ".join(str(self._array[i]) for i in range(self._n)) + "]"
        return list