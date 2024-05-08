'''
Jangmin Song 
Lab 5

No sources used
'''

from __future__ import annotations

######################################################################
class EmptyError(Exception):
    ''' class to represent an empty list exception '''
    def __init__(self, message: str) -> None:
        self.message = message

######################################################################
class Node[T]:
    ''' class to represent a node in a doubly-linked list '''
    def __init__(self, data: T):
        self.data: T      = data
        self.prev: Node[T] = None  # pointer to the previous Node in the list
        self.next: Node[T] = None  # pointer to the next Node in the list

######################################################################
class LinkedList[T]:
    ''' class to implement a doubly-linked list '''
    
    __slots__ = ('_head', '_tail', '_size')

    def __init__(self) -> None:
        self._head: Node[T] = None   # the head pointer in the linked list
        self._tail: Node[T] = None   # the tail pointer in the linked list
        self._size: int     = 0      # number of entries in the list

    def __len__(self) -> int:
        ''' returns the number of entries in the linked list
        Returns:
            integer valued number of list entries
        '''
        return self._size

    def front(self) -> T:
        ''' method to return the data item at the front of the list without
            removing that node
        Returns:
            the T-valued item at the front of the list
        Raises:
            EmptyError if the list is empty
        '''
        if self._head is None:
            raise EmptyError("List is empty")
        else:
            return self._head.data

    def back (self) -> T:
        ''' method to return the data item at the end of the list without
            removing that node
        Returns:
            the T-valued item at the end of the list
        Raises:
            EmptyError if the list is empty
        '''
        if self._tail is None:
            raise EmptyError("List is empty")
        else:
            return self._tail.data

    def add_left(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the left
            of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Raises:
            TypeError if non-empty list and item type does not match list entry types
        '''
        new_node = Node(item)
        if self._size != 0 and not isinstance(item, type(self._head.data)):
            raise TypeError('item type does not match list entry types')
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def add_right(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the right 
            of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Raises:
            TypeError if non-empty list and item type does not match list entry types
        '''
        new_node = Node(item)  # constructs a Node object with data == item
        if self._size != 0 and not isinstance(item, type(self._head.data)):
            raise TypeError('item type does not match list entry types')
        if self._head is None:
            # list is currently empty
            self._head = self._tail = new_node
        else:
            # list is not empty so append to the end 
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._size += 1

    def remove_left(self) -> T:
        ''' removes the first Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        if self._size == 0:
            raise EmptyError("cannot remove_left from an empty list")
        value: T = self._head.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return value

    def remove_right(self) -> T:
        ''' removes the last Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        if self._size == 0:
            raise EmptyError("cannot remove_right from an empty list")
        value: T = self._tail.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev

            ptr: Node[T] = self._head
            self._tail.next = None
            # while ptr.next != self._tail:
            #     ptr = ptr.next
            # ptr.next = None
            # self._tail = ptr
        self._size -= 1
        return value

    def __str__(self):
        ''' a str representation of the linked list data
        Returns:
            str representation of the linked list, showing head and tail
            pointers and list data items
        '''
        str_ = "head->"
        # start out at the head Node, and walk through Node by Node until we
        # reach the end of the linked list (i.e., the ._next entry is None)
        ptr_ = self._head
        while ptr_ is not None:
            str_ += "[" + str(ptr_.data) + "]<->" 
            ptr_ = ptr_.next  # move ptr_ to the next Node in the linked list

        if self._head != None: str_ = str_[:-3]  # remove the last "<->"
        str_ += "<-tail"
        return str_
    




        
###################
def main() -> None:
    # create a LinkedList and try out some various adds and removes
    #test for readWords
    print(f"Test for LinkedList")
    ll = LinkedList()

    print('add_right')
    ll.add_right(0)
    print(f"  result: {ll}")
    expected = 'head->[0]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_right(1)
    print(f"  result: {ll}")
    expected = 'head->[0]<->[1]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_right(2)
    print(f"  result: {ll}")
    expected = 'head->[0]<->[1]<->[2]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_right(3)
    print(f"  result: {ll}")
    expected = 'head->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print(f"\n")


    print('add_left')
    ll.add_left(4)
    print(f"  result: {ll}")
    expected = 'head->[4]<->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print("")

    ll.add_left(5)
    print(f"  result: {ll}")
    expected = 'head->[5]<->[4]<->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print("")

    ll.add_left(6)
    print(f"  result: {ll}")
    expected = 'head->[6]<->[5]<->[4]<->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_left(7)
    print(f"  result: {ll}")
    expected = 'head->[7]<->[6]<->[5]<->[4]<->[0]<->[1]<->[2]<->[3]<-tail'
    print(f"expected: {expected}")
    print(f"\n")

    print(f'front')
    print(f"  result: {ll.front()}")
    expected1 = '7'
    print(f"expected: {expected1}")
    print(f"\n")

    print(f'back')
    print(f"  result: {ll.back()}")
    expected1 = '3'
    print(f"expected: {expected1}")
    print(f"\n")

    print(f'remove_right')
    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]<->[6]<->[5]<->[4]<->[0]<->[1]<->[2]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]<->[6]<->[5]<->[4]<->[0]<->[1]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]<->[6]<->[5]<->[4]<->[0]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]<->[6]<->[5]<->[4]<-tail'
    print(f"expected: {expected1}")
    print(f"\n")

    print(f'remove_left')
    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head->[6]<->[5]<->[4]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head->[5]<->[4]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head->[4]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head-><-tail'
    print(f"expected: {expected1}")
    print(f"\n")

    # your tests here...

if __name__ == "__main__":
    main()
