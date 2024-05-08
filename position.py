from __future__ import annotations
from enum import Enum
from typing import NamedTuple

################################################################################

class Contents(str, Enum):
    EMPTY = " "
    START = "۞"
    GOAL = "🥅"
    BLOCKED = "🌚"
    PATH = "★"

    def __str__(self) -> str: 
        return self.value
        
################################################################################

class Position(NamedTuple):
    row: int
    col: int

    def __str__(self) -> str:
        return f'({self.col},{self.row})'
    
################################################################################

class Cell:
    __slots__ = ('_position', '_contents', '_parent')

    def __init__(self, row: int, col: int, contents: Contents) -> None:
        self._position: Position = Position(row, col)
        self._contents: Contents = contents
        self._parent: Cell = None

    def __str__(self) -> str: 
        contents = "[EMPTY]" if self._contents == Contents.EMPTY else self._contents
        result = f"({self._position.row}, {self._position.col}): {contents}"
        return result

    def getPosition(self) -> Position: 
        return self._position
    
    def getParent(self) -> Cell | None: 
        return self._parent

    def setParent(self, parent: Cell) -> None: 
        self._parent = parent

    def markOnPath(self) -> None: 
        self._contents = Contents.PATH

    def isBlocked(self) -> bool: 
        return self._contents == Contents.BLOCKED
    
    def isGoal(self) -> bool:
        return self._contents == Contents.GOAL
    
    def __eq__(self, other: Cell) -> bool:
        return self._position == other._position and \
               self._contents == other._contents and \
               self._parent == other._parent
        

################################################################################
class Maze:
    __slots__ = ('_num_rows', '_num_cols', '_start', '_goal', '_grid')

    def __init__(self, prop_block: float, num_rows: int = 10, num_cols: int = 10, \
                 start: Position = Position(0,0), goal: Position = Position(9,9)) -> None:
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._start: Cell = Cell(start.row, start.col, Contents.START)
        self._goal: Cell = Cell(goal.row, goal.col, Contents.GOAL)

        self._grid = [ [Cell(r ,c, Contents.EMPTY) for c in range(num_cols)] for r in range(num_rows) ]

        # This is the same thing as the code above
        # self.grid = []
        # for r in range(num_rows):
        #     row = []
        #     for c in range(num_cols):
        #         row.append(Cell(r,c,Contents.EMPTY))

        self._grid[start.row][start.col] = self._start
        self._grid[goal.row][goal.col] = self._goal


################################################################################

def main() -> None:

    start = Cell(0,0, Contents.START)
    goal = Cell(9,9, Contents.GOAL)
    empty = Cell(4,4, Contents.EMPTY)
    block = Cell(2,2, Contents.BLOCKED)
    path = Cell(9,8, Contents.PATH)

    for c in [start,goal,empty,block,path]:
        print(c)
    print('-' * 40)

    print(f'before: {empty}')
    empty.markOnPath()
    print(f'after: {empty}')
    
    # print('-' * 40)

    # p1 = Position(3,4)
    # p2 = Position(9,8)
    # p3 = (7,7)
    # print(f"row for p1 is: {p1.row}")
    # print(f"col for p1 is: {p1.col}")
    # print(f"row for p3 is: {p3[0]}")
    # print(f"col for p3 is: {p3[1]}")
    # print(f"ps is: {p2}")

if __name__ == "__main__":
    main()