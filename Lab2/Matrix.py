'''
Jangmin Song
DCS229 Lab2 
1/26/24


No resource used
'''
class Matrix:

    __slots__ = ('_num_rows', '_num_cols', '_data') #wont add anymore instant variables other than this

    def __init__(self, num_rows: int, num_cols: int, data: list[int]) -> None:
        '''
        This function gets the information and stores the information
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
            num_cols: an integer that has the number of cols of the matrix
            num_rows: an integer that has the number of rows of the matrix
            data: a list that contains the data of the matrix 
        Returns:
            returns none
        '''
        self._num_rows: int = num_rows #assigns the number of rows
        self._num_cols: int = num_cols #assigns the number of columns
        self._data: list[int] = data.copy() #copy the so that it doesn't get overwritten 
        if self._num_rows*self._num_cols != len(self._data): #if the dimensions and the data given does not match
            #raise value error
            raise ValueError(f"Provided number of rows and number of columns does not match with the given data: {self._num_rows}x{self._num_cols} and {self._data}")
    
    def getNumRows(self) -> int:
        '''
        This function gets the number of rows from the instant variable and returns the number of rows. 
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
        Returns:
            returns an integer that contains the number of columns
        '''
        numRows = self._num_rows #gets the number of rows from the self
        return numRows 


    def getNumCols(self) -> int:
        '''
        This function gets the number of columns from the instant variable and returns the number of columns. 
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
        Returns:
            returns an integer that contains the number of columns
        '''
        numCols = self._num_cols #gets the number of columns from the self
        return numCols


    def __str__(self) -> str:
        '''
        This function gets the information from self, and visualize the matrix data. 
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
        Return:
            returns a string that is visualized
        '''
        result = "|  " #matrix box is covered with "|", every numbers in the matrix is written inside "|"
        for r in range(self._num_rows): #for loops to run all the values
            for c in range(self._num_cols):
                idx = (r*self._num_cols)+ c #formula to find the index
                sortedList = sorted(self._data) #sort the data in the value order
                if len(str(sortedList[-1])) >= len(str(sortedList[0])): #if the first number in the list's length is bigger than the last number in the list's length
                    result += f'{self._data[idx]:>{len(str(sortedList[-1]))}}  ' #the number will be right adjusted, but with the last number in the list's length
                else:  #if the first number in the list's length is not bigger than the last number in the list's length
                    result += f'{self._data[idx]:>{len(str(sortedList[0]))}}  ' #the number will be right adjusted with the first number in the list's length
            result += "|\n|  " #the rows of the matrix end with "|" and go to the next line and start with "|"
        visualization = result[:-4] #cuts the last three characters of the result
        return visualization

    def __getitem__(self, row_col: tuple[int]) -> int:
        '''
        This function gets the number of columns from the instant variable and returns the number of columns. 
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
        Returns:
            returns an integer that contains the number of columns
        '''
        r = row_col[0] #the first number that appears in the parentheses in the tuple
        c = row_col[1] #the second number that appears in the parentheses in the tuple
        if r >= self._num_cols and c >= self._num_rows: #if the give location is not in the list
            raise IndexError(f"Provided tuple has invalid indices: {row_col}") #raise an index error
        else: 
            idx = (r*self._num_cols)+ c #find the index with the give row and column
            value = self._data[idx] #the index in the list is the value we are looking for
        return value
    
    def __eq__(self, other: 'Matrix') -> bool:
        '''
        This function gets two matrices and compares whether they are equal or not
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
            other: a matrix that gets comapared with self matrix
        Returns:
            returns a boolean that tells whether the they are equal or not equal
        '''
        equal = False 
        if isinstance(other,Matrix): #if the type object of "other" is matrix #if the type object of "other" is matrix
            if self._num_rows == other._num_rows and self._num_cols == other._num_cols: #if the number of rows and columns of two matricies are equal
                if self._data == other._data: #if the data of self and other are equal
                    equal = True #they are equal
                else: 
                    equal = False #they are not equal
        else:  #if the number of rows and columns are not equal
            raise TypeError(f"Second given information is not type Matrix. It is {type(other)}") #raise type error saying 
        return equal
    def __add__(self, other: 'Matrix') -> 'Matrix':
        '''
        This function adds two matricies
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
            other: a matrix that gets added to self matrix
        Returns:
            returns matrix that are the sum of two matricies
        '''
        if not isinstance(other,Matrix): #if the type object of "other" is matrix #if the type object of "other" is matrix
            raise TypeError(f"Second given information is not type Matrix. It is {type(other)}") #raise type error saying
        else:
            if self._num_rows == other._num_rows and self._num_cols == other._num_cols: #if the number of rows and columns of two matricies are equal
                addedData = [] #new list for the summed data
                for i in range(len(self._data)): #run the for loop with the length of data
                    newValue = self._data[i] + other._data[i] #calculation
                    addedData.append(newValue) #new data added to the list
                    newValue = 0 #resets the value
                new_matrix = Matrix(self._num_rows, self._num_cols, addedData) #forms a new matrix and prints out in return 
            else: #if the number of rows and columns of two matricies are not equal
                raise ValueError(f"Cannot add different matrix dimensions {self._num_rows}x{self._num_cols} and {other._num_rows}x{other._num_cols}") #raise a value error for having different dimensions
        return new_matrix
    
    def transpose(self) -> 'Matrix':
        '''
        This function transposes the given matrix
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
        Returns:
            returns a matrix that is being transposed
        '''
        transposedData = [] #an empty list for the new data
        col = 0 #counts what current column location
        while col != self._num_cols: #while col counter does not equal matrix column
            for i in range(0 ,len(self._data), self._num_cols): #for loop for only the division of number of columns
                #the first column becomes the first row if col = 0 if col is added, then the second column becomes the second row
                #that number gets appended to the new transposed list
                transposedData.append(self._data[i+col]) 
            col += 1 #the column shifts to the right
        new_matrix = Matrix(self._num_cols, self._num_rows, transposedData) #column and row switches when transposed and makes a new transposed matrix
        return new_matrix
    
    def __mul__(self, other: 'Matrix') -> 'Matrix':
        '''
        This function multiplies two matrices
        Parameters:
            self: the main parameter that is shared among the class and in this case, it's a matrix
            other: a matrix that gets multiplied to self matrix
        Returns:
            returns a matrix that is multiplied
        '''
        multipliedData = [] #a new list of data
        multipliedValue = 0 #the multiplied value gets to be added to the new list of data
        idx = 0 #saves the current location of self matrix
        col = 0 #saves what current column location
        counter = 0 #a counter that counts how many times the first matrix rows to be reapeated to be multiplied with all the columns in other matrix
        if not isinstance(other,Matrix): #if the type object of "other" is matrix
            raise TypeError(f"Second given information is not type Matrix. It is {type(other)}") #raise type error saying
        else:
            if self._num_cols != other._num_rows:
                raise ValueError(f"The dimensions are not suitable for multiplying: {self._num_rows}x{self._num_cols} and {other._num_rows}x{other._num_cols}")
            else:
                while counter < len(self._data)*other._num_cols: #if the matrix is less than the total of numbers of multiplications of two matrices
                    while col != other._num_cols: #while col counter does not equal matrix column
                        for i in range(0 ,len(other._data), other._num_cols): #for loop for only the division of number of columns
                            multipliedValue += (self._data[idx] * other._data[i+col]) #self data and other data (other data moves to the next number in the column) gets multiplied and added to the other multiplied values from the same row and the column 
                            idx += 1 #moves on to the next number in the row
                            counter +=1 #counter gets added
                        col += 1 #moves on to the next column
                        idx -= self._num_cols #index moves back to the original place because the same row has to be multiplied with rest of the columns
                        multipliedData.append(multipliedValue) #the value is added to the list of data
                        multipliedValue = 0 #resets the value for the next secion
                    col = 0 #column resets to go over the matrix in horizontal way again
                    idx += self._num_cols #index added to move on to the next row
                new_matrix = Matrix(self._num_rows, other._num_cols, multipliedData) #forms a new matrix
                return new_matrix
        
def main() -> None:
    m1 = Matrix(2,2,[0,2,-2,-5])
    m2 = Matrix(2,2,[0,2,-2,-5])
    m3 = Matrix(2,1,[6,-3])
    m4 = Matrix(1,2,[-5,4])
    m5 = Matrix(2,3,[5,3,5,1,5,0])
    m6 = Matrix(3,2,[-4,2,-3,4,3,-5])
    m7 = Matrix(3,3,[4,22,65,123,8,4,0,3,11])
    m8 = Matrix(4,3,[-1,1,-1,5,2,-5,6,-5,1,-5,6,0])
    m9 = Matrix(2,1,[5,3])
    m10 = Matrix(2,3,[-4,2,-3,4,3,-5])

    print()
    print()
    print("Test for __init(self, num_rows, num_cols, data)__:")
    try:
        print(Matrix(1,1,[1,1,1,1,1,1,1,1,1,1]))
    except Exception as e:
        print("Error handling:")
        print(f"  Result: {e}")
        print(f"Expected: Provided number of rows and number of columns does not match with the given data: 1x1 and [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]")

    print()
    print()

    print("Test for getNumRows(self) and getNumCols(self):")
    print(f"  Result: {m1.getNumRows()}")
    print(f"Expected: 2")
    print()
    print(f"  Result: {m5.getNumRows()}")
    print(f"Expected: 2")
    print()
    print(f"  Result: {m8.getNumRows()}")
    print(f"Expected: 4")
    print()
    print(f"  Result: {m2.getNumCols()}")
    print(f"Expected: 2")
    print()
    print(f"  Result: {m9.getNumCols()}")
    print(f"Expected: 1")
    print()
    print(f"  Result: {m10.getNumCols()}")
    print(f"Expected: 3")

    print()
    print()

    print("Test for __str__(self):")
    print(f"Result:\n{m1}")
    print(f"Expected:\n|   0   2  |\n|  -2  -5  |")
    print()
    print(f"Result:\n{m3}")
    print(f"Expected:\n|   6  |\n|  -3  |")
    print()
    print(f"Result:\n{m5}")
    print(f"Expected:\n|  5  3  5  |\n|  1  5  0  |")
    print()
    print(f"Result:\n{m8}")
    print(f"Expected:\n|  -1   1  -1  |\n|   5   2  -5  |\n|   6  -5   1  |\n|  -5   6   0  |")
    
    print()
    print()

    print("Test for __getitem__(self, tuple):")
    try:
        print(f"  Result: {m1.__getitem__((1,1))}")
        print(f"Expected: -5")
        print()
        print(f"  Result: {m3.__getitem__((0,1))}")
        print(f"Expected: -3")
        print()
        print(f"  Result: {m7.__getitem__((0,0))}")
        print(f"Expected: 4")
        print()
        print(m8.__getitem__((10,10)))
    except Exception as e:
        print("Error handling:")
        print(f"  Result: {e}")
        print(f"Expected: Provided tuple has invalid indices: (10, 10)")

    print()
    print()

    print("Test for __eq__(self, other):")
    try:
        print(f"  Result: {m1==m2}")
        print(f"Expected: True")
        print()
        print(f"  Result: {m3==m4}")
        print(f"Expected: False")
        print()
        print(f"  Result: {m5==m8}")
        print(f"Expected: False")
        print()
        print(f"  Result: {m1.__eq__(m2)}")
        print(f"Expected: True")
        print()
        print(m8.__eq__("Not Matrix"))
    except Exception as e:
        print("Error handling:")
        print(f"  Result: {e}")
        print(f"Expected: Second given information is not type Matrix. It is <class 'str'>")
        
    print()
    print()

    print("Test for __add__(self, other):")
    try:
        print(f"Result:\n{m1+m2}")
        print(f"Expected:\n|    0    4  |\n|   -4  -10  |")
        print()
        print(f"Result:\n{m3+m9}")
        print(f"Expected:\n|  11  |\n|   0  |")
        print()
        print(f"Result:\n{m5+m10}")
        print(f"Expected:\n|   1   5   2  |\n|   5   8  -5  |")
        print()
        print(m8.__add__(m2))
    except Exception as e:
        print("Error handling:")
        print(f"  Result: {e}")
        print(f"Expected: Cannot add different matrix dimensions 4x3 and 2x2")

    print()
    print()

    print("Test for transpose(self):")
    print(f"Result:\n{m1.transpose()}")
    print(f"Expected:\n|   0  -2  |\n|   2  -5  |")
    print()
    print(f"Result:\n{m5.transpose()}")
    print(f"Expected:\n|  5  1  |\n|  3  5  |\n|  5  0  |")
    print()
    print(f"Result:\n{m8.transpose()}")
    print(f"Expected:\n|  -1   5   6  -5  |\n|   1   2  -5   6  |\n|  -1  -5   1   0  |")
    
    print()
    print()

    print("Test for __mul__(self, other):")
    try:
        print(f"Result:\n{m5*m6}")
        print(f"Expected:\n|  -14   -3  |\n|  -19   22  |")
        print()
        print(f"Result:\n{m8*m7}")
        print(f"Expected:\n|   119   -17   -72  |\n|   266   111   278  |\n|  -591    95   381  |\n|   718   -62  -301  |")
        print()
        print(f"Result:\n{m7*m7}")
        print(f"Expected:\n|  2722   459  1063  |\n|  1476  2782  8071  |\n|   369    57   133  |")
        print()
        print(m8.__mul__(m1))
    except Exception as e:
        print("Error handling:")
        print(f"  Result: {e}")
        print(f"Expected: The dimensions are not suitable for multiplying: 4x3 and 2x2")

if __name__ == "__main__":
    main()
