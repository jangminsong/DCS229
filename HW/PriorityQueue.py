from __future__ import annotations

import heapq
import random
import string
import copy

#################
class EmptyError(Exception):
    ''' class to represent an empty list exception '''
    def __init__(self, message: str) -> None:
        self.message = message
#################
class Entry[K,V]:
    __slots__ = ('key', 'value')

    def __init__(self, priority: K, data: V) -> None:
        self.key  : K = priority
        self.value: V = data

    def __str__(self) -> str:
        return f"({self.key},{self.value})"

    def __eq__(self, other: Entry[K,V]) -> bool:
        return self.key == other.key and self.value == other.value

    def __lt__(self, other: Entry[K,V]) -> bool:
        return self.key < other.key

    # not the Pythonic way to use __repr__ but allows us to print list of Entry
    def __repr__(self) -> str: 
        return f"({repr(self.key)},{'∅' if self.value is None else repr(self.value)})"

#######################
class PriorityQueue[E]:
    __slots__ = ('_container')

    def __init__(self):
        self._container: list[Entry] = list()

    def __len__(self)  -> int:   return len(self._container)
    def is_empty(self) -> bool:  return len(self._container) == 0

    def insert(self, key: K, item: V) -> None: 
        '''
        inserts the key item pair into the array
        Parameters:
            key: the int that determines the priority in the arrary
            item: the item being inserted
        Returns:
            None
        '''
        entry = Entry(key, item)
        heapq.heappush(self._container, entry)

    def remove_min(self) -> Entry:
        '''
        removes the minimum key from the array
        Parameters:
            None
        Returns:
            None
        '''
        if self.is_empty():
            raise EmptyError("Priority queue is empty")
        return heapq.heappop(self._container)

    def min(self) -> Entry:
        '''
        Outputs the minimum key of the array
        Parameters:
            None
        Returns:
            None
        '''
        if self.is_empty():
            raise EmptyError("Priority queue is empty")
        return copy.deepcopy(self._container[0])

    def __str__(self) -> str:
        return str(self._container)

##########################
def main():
    pq = PriorityQueue()
    print(f"len of pq = {len(pq)}")
    # more tests below

    # Insert test
    print("insert test:")
    pq.insert(4, 'D')
    print(f"Expected: [(4,'D')]")
    print(f'  Result: {pq}')
    pq.insert(7, 'G')
    print(f"Expected: [(4,'D'), (7,'G')]")
    print(f'  Result: {pq}')
    pq.insert(2, 'B')
    print(f"Expected: [(2,'B'), (7,'G'), (4,'D')]")
    print(f'  Result: {pq}')
    pq.insert(4, 'P')
    print(f"Expected: [(2,'B'), (4,'P'), (4,'D'), (7,'G')]")
    print(f'  Result: {pq}')
    pq.insert(9, 'A')
    print(f"Expected: [(2,'B'), (4,'P'), (4,'D'), (7,'G'), (9,'A')]")
    print(f'  Result: {pq}')
    print()

    # Remove min test
    print("removal of min test:")
    pq.remove_min()
    print(f"Expected: [(4,'D'), (4,'P'), (9,'A'), (7,'G')]")
    print(f'  Result: {pq}')
    pq.remove_min()
    print(f"Expected: [(4,'D'), (4,'P'), (7,'G')]")
    print(f'  Result: {pq}')
    pq.remove_min()
    print(f"Expected: [(4,'D'), (7,'G')]")
    print(f'  Result: {pq}')
    pq.remove_min()
    print(f"Expected: [(4,'D')]")
    print(f'  Result: {pq}')
    print()

    print('min test')
    pq.insert(4, 'D')
    print(f'Expected: (4,D)')
    print(f'  Result: {pq.min()}')
    pq.insert(7, 'G')
    print(f'Expected: (4,D)')
    print(f'  Result: {pq.min()}')
    pq.insert(2, 'B')
    print(f'Expected: (2,B)')
    print(f'  Result: {pq.min()}')

    
    pq2 = PriorityQueue()
    pq2.insert(4, 'C')
    pq2.insert(5, 'A')
    pq2.insert(6, 'Z')
    pq2.insert(15, 'K')
    pq2.insert(9, 'F')
    pq2.insert(7, 'Q')
    pq2.insert(20, 'B')
    pq2.insert(16, 'X')
    pq2.insert(25, 'J')
    pq2.insert(14, 'E')
    pq2.insert(12, 'H')
    pq2.insert(11, 'S')
    pq2.insert(13, 'W')
    print(pq2)
    print()
    
    print('insertion of (2,T) into tree on slide 11')
    pq2.insert(2, 'T')
    print(pq2)
    print()

    pq2.remove_min()

    print('removal of min from tree on slide 18')
    pq2.remove_min()
    print(pq2)



if __name__ == "__main__":
    main()


