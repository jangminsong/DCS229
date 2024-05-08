'''
Jangmin Song 
Lab 5

No sources used
'''

from LinkedList import LinkedList, EmptyError
from typing import TypeVar
T = TypeVar('T')

class Queue:
    __slots__ = ("_data")  # a Python list

    def __init__(self):
        self._data = LinkedList()

    def push(self, e: T) -> None: 
        '''
        inserts element e at the end of the queue
        Parameters:
            e: T value that is supposed to get added
        Returns:
            none
        '''
        self._data.add_right(e)
        
    def pop(self) -> T:
        '''
        removes & returns element at the front of queue
        Returns:
            T value that is the element at the front of queue
        '''
        if self._data.__len__() == 0:
            raise EmptyError('The list is empty')
        else:
            return self._data.remove_left()

    def top(self) -> T:
        '''
        returns reference to first element without removing
        Returns:
            T value that is the first element queue
        '''
        if self._data.__len__() == 0:
            raise EmptyError('The list is empty')
        else:
            return self._data.front()

    def is_empty(self) -> bool:
        '''
        indicates whether queue is empty
        Returns:
            a boolean indicates whether queue is empty
        '''
        if self._data.__len__() == 0:
            return True
        else:
            return False

    def __len__(self) -> int: 
        '''
        returns queue length
        Returns:
            an integer that shows the length of the list
        '''
        return self._data.__len__() 
    
    def __str__(self):
        return str(self._data)

def main() -> None:
    # your tests here...
    print("Test for Queue")
    q = Queue()

    print('push')
    q.push(0)
    print(f"  result: {q}")
    expected = 'head->[0]<-tail'
    print(f"expected: {expected}")
    print()

    q.push(1)
    print(f"  result: {q}")
    expected = 'head->[0]<->[1]<-tail'
    print(f"expected: {expected}")
    print()

    q.push(2)
    print(f"  result: {q}")
    expected = 'head->[0]<->[1]<->[2]<-tail'
    print(f"expected: {expected}")
    print()

    q.push(3)
    print(f"  result: {q}")
    expected = 'head->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print(f"\n")

    print('pop')
    q.pop()
    print(f"  result: {q}")
    expected = 'head->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print()

    q.pop()
    print(f"  result: {q}")
    expected = 'head->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print()

    q.pop()
    print(f"  result: {q}")
    expected = 'head->[3]<-tail'
    print(f"expected: {expected}")
    print()

    q.pop()
    print(f"  result: {q}")
    expected = 'head-><-tail'
    print(f"expected: {expected}")
    print(f"\n")

    print('top')
    q.push(0)
    q.push(1)
    q.push(2)
    q.push(3)
    print(f"  result: {q.top()}")
    expected = '0'
    print(f"expected: {expected}")
    print(f"\n")

    print('is_empty')
    print(f"  result: {q.is_empty()}")
    expected = 'False'
    print(f"expected: {expected}")
    print()

    for i in range (q.__len__()):
        q.pop()
    print(f"  result: {q.is_empty()}")
    expected = 'True'
    print(f"expected: {expected}")
    print(f"\n")

    q.push(0)
    q.push(1)
    q.push(2)
    q.push(3)

    print('__len__')
    print(f"  result: {len(q)}")
    expected = '4'
    print(f"expected: {expected}")
    print(f"\n")

if __name__ == "__main__":
    main()
