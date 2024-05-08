class Matrix:

    __slots__ = ('_num_rows', '_num_cols', '_data')

    def __init__(self, num_rows: int, num_cols: int, data: list[int]) -> None:
        #Instance var should be treated as private -- i.e., they should not
        #accessed outside of the class Matrix
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        #self._data: list[int] = data
        self._data: list[int] = data.copy()
        print(f"id of self._data = {id(self._data)}")

    def __str__(self)-> str:
        result = "| "
        for r in range(self._num_rows):
            for c in range(self._num_cols):
                idx = (r*self._num_cols)+ c
                result += str(self._data[idx]) + " "
            result += " |\n| "
        return result[:-3]
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        # can access self's instant var
        # can access other's instant var
        new_matrix = Matrix(3, 3, [1]) #stores the added matrix of m1 and m2 FIX!
        return new_matrix
    
    def setValue(self, row: int, col: int, new_value: int) -> None:
        if new_value < 0:
            raise ValueError(f"Cannot set Using negative value {new_value}")
        idx = (row*self._num_cols) + col
        self._data[idx] = new_value


def main() -> None:
    m1 = Matrix(3,3,[11,19,7,21,4,6,1,2,3])
    print(m1)
    # m1._data[-1] = 123 #breaks all rules of data encapsulation

    #m1.setValue(2,2, 999)
    data[-1] = 999
    print()
    print(m1)


if __name__ == "__main__":
    main()
