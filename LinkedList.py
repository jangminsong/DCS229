from __future__ import annotations

class EmptyError(Exception):
    def __init__(self, message) -> None:
        self.message = message

class Node[T]:
    def __init__(self, data: T):
        self.data: T      = data
        self.next: Node[T] = None  # eventually another Node

class LinkedList[T]:
    __slots__ = ('_head', '_tail', '_size')

    def __init__(self) -> None:
        self._head: Node[T] = None   # the head pointer in the linked list
        self._tail: Node[T] = None   # the tail pointer in the linked list
        self._size: int     = 0

    def __len__(self) -> int:  return self._size

    def add_left(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the left
            of the linked list... remember to reset the head pointer, and, when
            appropriate, the tail pointer
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''
        new_node = Node(item)  # constructs a Node object with data == item
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1


    def add_right(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the right 
            of the linked list... remember to reset the tail pointer, and, when
            appropriate, the head pointer
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''
        new_node = Node(item)  # constructs a Node object with data == item
        if self._head is None:
            # list is currently empty
            self._head = self._tail = new_node
        else:
            # list is not empty so append to the end 
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove_left(self) -> T:
        ''' removes the first Node in the linked list, returning the data item
            inside that Node...  Remember to handle the special case of an 
            empty list (what should the head and tail pointers be in that case?)
            and remember to update the head & tail pointer(s) when appropriate.
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
        self._size -= 1
        return value

    def remove_right(self) -> T:
        ''' removes the last Node in the linked list, returning the data item
            inside that Node...  Remember to handle the special case of an 
            empty list (what should the head and tail pointers be in that case?)

            Note: This one is trickier because you always have to walk (almost)
            all the way through the list in order to know what the new tail
            should be.

            Remember to update the head & tail pointer(s) when appropriate.
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        if self._size == 0:
            raise EmptyError("cannot remove_right from an empty list")
        '''
        NOTE: The code below, as implemented in class, ultimately
            fails with the following error.  Part of your HW assignment
            is to fix this error and make remove_right work correctly.

        File ".../LinkedList.py", line 102, in remove_right
        while ptr.next != self._tail:
              ^^^^^^^^
        AttributeError: 'NoneType' object has no attribute 'next'
        '''
        value: T = self._tail.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            ptr: Node[T] = self._head
            while ptr.next != self._tail:
                ptr = ptr.next
            ptr.next = None
            self._tail = ptr
        self._size -= 1
        return value

    def __str__(self):
        ''' returns a str representation of the linked list data
        Returns:
            an str representation of the linked list, showing head pointer
                and data tiems
        '''
        str_ = "head->"

        # start out at the head Node, and walk through Node by Node until we
        # reach the end of the linked list (i.e., the ._next entry is None)
        ptr_ = self._head
        while ptr_ is not None:
            str_ += "[" + str(ptr_.data) + "]->" 
            ptr_ = ptr_.next  # move ptr_ to the next Node in the linked list

        if self._head != None: str_ = str_[:-2]
        str_ += "<-tail"
        return str_

        
def main():
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
    expected = 'head->[0]->[1]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_right(2)
    print(f"  result: {ll}")
    expected = 'head->[0]->[1]->[2]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_right(3)
    print(f"  result: {ll}")
    expected = 'head->[0]->[1]->[2]->[3]<-tail'
    print(f"expected: {expected}")
    print(f"\n")


    print('add_left')
    ll.add_left(4)
    print(f"  result: {ll}")
    expected = 'head->[4]->[0]->[1]->[2]->[3]<-tail'
    print(f"expected: {expected}")
    print("")

    ll.add_left(5)
    print(f"  result: {ll}")
    expected = 'head->[5]->[4]->[0]->[1]->[2]->[3]<-tail'
    print(f"expected: {expected}")
    print("")

    ll.add_left(6)
    print(f"  result: {ll}")
    expected = 'head->[6]->[5]->[4]->[0]->[1]->[2]->[3]<-tail'
    print(f"expected: {expected}")
    print()

    ll.add_left(7)
    print(f"  result: {ll}")
    expected = 'head->[7]->[6]->[5]->[4]->[0]->[1]->[2]->[3]<-tail'
    print(f"expected: {expected}")
    print(f"\n")

    print(f'remove_right')
    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]->[6]->[5]->[4]->[0]->[1]->[2]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]->[6]->[5]->[4]->[0]->[1]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]->[6]->[5]->[4]->[0]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_right()
    print(f"  result: {ll}")
    expected1 = 'head->[7]->[6]->[5]->[4]<-tail'
    print(f"expected: {expected1}")
    print(f"\n")

    print(f'remove_left')
    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head->[6]->[5]->[4]<-tail'
    print(f"expected: {expected1}")
    print()

    ll.remove_left()
    print(f"  result: {ll}")
    expected1 = 'head->[5]->[4]<-tail'
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

if __name__ == "__main__":
    main()
