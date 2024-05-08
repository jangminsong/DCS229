'''
Jangmin Song 
Lab 5

No sources used
'''
from __future__ import annotations

from enum import Enum
from typing import NamedTuple

from Queue import Queue
from Stack import Stack
from PriorityQueue import PriorityQueue

import random

###########################################################
class Contents(str, Enum):
    ''' create an enumeration to define what the visual contents 
        of a Cell are; using str as a "mixin" forces all the entries
        to be strings; using an enum means no cell entry can be 
        anything other than the options here '''
    EMPTY   = " "
    START   = "◎"  # "S"
    GOAL    = "◆"  # "G"
    BLOCKED = "░"  # "X"
    PATH    = "★"  # "*"

    def __str__(self) -> str: return self.value

###########################################################
class Position(NamedTuple):
    ''' named tuple that allows us to use .row and .col rather 
        than the less-easy-to-read [0] and [1] for accessing 
        values'''
    row: int
    col: int

    def __str__(self) -> str: return f"({self.row},{self.col})"

###########################################################
class Cell:
    ''' class that allows us to use Cell as a data type -- 
        row, column, & cell contents '''
    __slots__ = ('_position', '_contents', '_parent')

    def __init__(self, row: int, col: int, contents: Contents):
        self._position: Position = Position(row, col)
        self._contents: Contents = contents
        self._parent:   Cell     = None

    def __str__(self) -> str:
        contents = "[EMPTY]" if self._contents == Contents.EMPTY else self._contents
        result = f"({self._position.row},{self._position.col}): {contents}"
        if self._parent is not None: 
            result += f"({self._parent._position.row}, {self._parent._position.col})"
        return result

    def getPosition(self) -> Position:    return self._position
    def getParent(self)   -> Cell | None: return self._parent

    def setParent(self, parent: Cell) -> None:  self._parent = parent 
    def markOnPath(self)              -> None:  self._contents = Contents.PATH
    def markAsBlocked(self)           -> None:  self._contents = Contents.BLOCKED

    def isBlocked(self) -> bool:  return self._contents == Contents.BLOCKED
    def isGoal(self)    -> bool:  return self._contents == Contents.GOAL

    def __eq__(self, other: Cell) -> bool:
        return self._position == other._position and \
               self._contents == other._contents and \
               self._parent   == other._parent
        
###########################################################
class Maze:
    __slots__ = ('_num_rows', '_num_cols', '_start', '_goal', '_grid','_num_cells_pushed','_path_length')

    def __init__(self, num_rows: int = 10, num_cols: int = 10, \
                       start: Position = Position(0,0), \
                       goal:  Position = Position(9,9), \
                       proportion_blocked: float = 0.2, \
                       debug: bool = False) -> None:
        ''' Maze initializer method
        Parameters:
            num_rows:           number of rows in the grid
            num_cols:           number of columns in the grid
            start:              Position object indicating (row,col) of the start cell
            goal:               Position object indicating (row,col) of the goal cell
            proportion_blocked: proportion of cells to be blocked (between 0.0 and 1.0)
            debug:              whether to use one of the Maze examples from slides
        Raises:
            TypeError if proportion_blocked is not float
            TypeError if start of goal is not Position
            ValueError if proportion_blocked is outside (0,1)
        '''
        if not isinstance(proportion_blocked, float):
            raise TypeError("proportion_blocked argument must be a float")
        if proportion_blocked < 0 or proportion_blocked > 1:
            raise ValueError("proportion_blocked argument must be a float b/w 0 and 1")
        if not isinstance(start, Position) or not isinstance(goal, Position):
            raise TypeError("start and goal must both be Position objects")

        if debug:  # set up 6X5 maze example from course slides
            num_rows = 6; num_cols = 5;
            start = Position(5, 0)
            goal  = Position(0, 4)

        self._num_cells_pushed = 0
        self._path_length = 0
        self._num_rows: int  = num_rows
        self._num_cols: int  = num_cols

        # set up the start and goal Cell objects
        self._start: Cell = Cell(start.row, start.col, Contents.START)
        self._goal:  Cell = Cell(goal.row,  goal.col,  Contents.GOAL)

        # create a 2D list of Cell objects, all initially empty
        self._grid: list[ list[Cell] ] = \
            [ [Cell(r,c, Contents.EMPTY) for c in range(num_cols)] \
              for r in range(num_rows) ]

        # overwrite the appropriate locations with the start and goal Cells
        self._grid[start.row][start.col] = self._start
        self._grid[goal.row][goal.col]   = self._goal

        if debug:
            # for example from slides
            blocked_cells = [(1,1), (1,3), (2,4), (3,2), (5,1), (5,3), (5,4)]
            for pos in blocked_cells:
                p = Position(*pos)  # expand the pos tuple & pass to Position
                self._grid[p.row][p.col].markAsBlocked()
                #self._grid[pos[0]][pos[1]]._contents = Contents.BLOCKED
        else:
            # put blocks at random spots in the grid, using given proportion
            options: list[Cell] = [cell for row in self._grid for cell in row]  # 1D version of our 2D list
            options.remove(self._start)
            options.remove(self._goal)
            how_many: int = round((num_rows * num_cols - 2) * proportion_blocked)
            blocked: list[Cell] = random.sample(options, k = how_many)
            #print(f"type of blocked[0] = {type(blocked[0])}") 
            #print(f"blocked[0] = {blocked[0]}") 
            for cell in blocked:
                cell._contents = Contents.BLOCKED

    def showPath(self, goal: Cell) -> None:
        path = []
        cell = goal
        while cell._parent is not None:
            path.append(cell)
            cell = cell._parent
        path.append(cell)  # should be the start
        self._path_length += len(path)
        assert(cell == self._start)
        path.reverse()  # reverse the path list
        for cell in path:
            if cell not in [self._start, self._goal]:
                cell.markOnPath()

        print(self)  # print the newly marked-up maze


    def getStart(self) -> Cell: return self._start
    def getGoal(self)  -> Cell: return self._goal

    def __str__(self) -> str:
        ''' creates a str version of the Maze, showing contents, with cells
            delimited by vertical pipes
        Returns:
            a str representation of the Maze
        '''
        maze_str = ""
        for row in self._grid:  # row : list[Cell]
            maze_str += "|" + "|".join([cell._contents for cell in row]) + "|\n"
        return maze_str[:-1]  # remove the final \n

    def getSearchLocations(self, cell: Cell) -> list[Cell]:
        ''' returns a list of Cell objects of valid search locations
            (i.e., in the Maze, not already searched, not block) in
            the directions N,S,W,E of the given cell
        Parameters:
            cell: the current cell searching from
        Returns:
            a list of Cell objects of valid Cells to explore
        '''
        searchLocations = []
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(movements)):
            new_row = cell.getPosition().row + movements[i][0]
            new_col = cell.getPosition().col + movements[i][1]
            if 0 <= new_row < self._num_rows and 0 <= new_col < self._num_cols:
                explore = self._grid[new_row][new_col]
                if not explore.isBlocked() and explore != self._start:  
                    searchLocations.append(explore)
        return searchLocations

    def dfs(self) -> Cell | None:
        ''' implements depth-first search (using a Stack)
        Returns:
            a Cell object corresponding to the goal, if a valid path exists 
            from the start to the goal;  or None, if no path exists
        '''
        stack = Stack()
        stack.push(self._start)
        self._num_cells_pushed += 1
        while not stack.is_empty():
            current_cell = stack.pop()
            if current_cell == self._goal:
                return current_cell
            neighbors = self.getSearchLocations(current_cell)
            for i in neighbors:
                if str(i.getParent()) == 'None':
                    stack.push(i)
                    i.setParent(current_cell)
                    self._num_cells_pushed += 1
        return None

    def bfs(self) -> Cell | None:
        '''implements breath-first search (using a queue)
        Returns:
            a Cell object corresponding to the goal, if a valid path exists 
            from the start to the goal;  or None, if no path exists
        '''
        queue = Queue()
        queue.push(self._start)
        self._num_cells_pushed += 1
        while not queue.is_empty():
            current_cell = queue.pop()
            if current_cell == self._goal:
                return current_cell
            neighbors = self.getSearchLocations(current_cell)
            for i in neighbors:
                if str(i.getParent()) == 'None':
                    queue.push(i)
                    i.setParent(current_cell)
                    self._num_cells_pushed += 1
        return None
    
    def a_star(self) -> Cell | None:
        '''implements A* search (using a priority queue)
        Returns:
            a Cell object corresponding to the goal, if a valid path exists 
            from the start to the goal;  or None, if no path exists
        '''
        to_explore = PriorityQueue()
        explored = dict()

        n = self._start
        g_n = 0.0
        h_n = abs((self._goal.getPosition()[0] - self._start.getPosition()[0]) + \
                  (self._goal.getPosition()[1] - self._start.getPosition()[1]))
        f_n = g_n + h_n
        to_explore.insert(f_n, n)
        self._num_cells_pushed += 1
        explored[n.getPosition()] = g_n
        while not to_explore.is_empty():
            e = to_explore.remove_min()
            n = e.value
            if n == self._goal:
                return n
            for m in self.getSearchLocations(n):
                updated_m_cost = f_n + 1
                if m.getPosition() not in explored or updated_m_cost < explored[m.getPosition()]:
                    g_m = updated_m_cost
                    explored[m.getPosition()] = g_m  # set the new/improved cost
                    h_m = abs((self._goal.getPosition()[0] - m.getPosition()[0]) + \
                            (self._goal.getPosition()[1] - m.getPosition()[1]))
                    f_m = g_m + h_m
                    to_explore.insert(f_m, m)
                    self._num_cells_pushed += 1
                    m.setParent(n)
                    explored[m.getPosition()] = updated_m_cost
        return None

    


###########################################################
def main() -> None:

    #getSearchLocations
    print('Testing .getSearchLocations():')
    print('-'*30)
    g = Maze(debug = True)
    c = Cell(1,1, Contents.EMPTY)
    result = g.getSearchLocations(c)
    print(f'expected: [<__main__.Cell object at 0x16f479100>, <__main__.Cell object at 0x16f479700>, <__main__.Cell object at 0x16f479380>, <__main__.Cell object at 0x16f479480>]')
    print(f'  result: {result}')
    b = Cell(2,2, Contents.EMPTY)
    result = g.getSearchLocations(b)
    print(f'expected: [<__main__.Cell object at 0x16f479480>, <__main__.Cell object at 0x16f479700>, <__main__.Cell object at 0x16f4797c0>]')
    print(f'  result: {result}')
    print()

   
    print('5x5:')
    m = Maze(debug = True)
    print(m)
    print()
    
    dfs = m.dfs()
    if dfs:
        print("dfs:")
        m.showPath(dfs)
        print(f'Path length: {m._path_length}')
        print(f'Number of cells pushed: {m._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    m2 = Maze(debug = True)
    bfs = m2.bfs()
    if bfs:
        print("bfs:")
        m2.showPath(bfs)
        print(f'Path length: {m2._path_length}')
        print(f'Number of cells pushed: {m2._num_cells_pushed}')
    else:
        print("No path found")

    print()
    m3 = Maze(debug = True)
    a_star = m3.a_star()
    if a_star:
        print("A*:")
        m3.showPath(a_star)
        print(f'Path length: {m3._path_length}')
        print(f'Number of cells pushed: {m3._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    
    print('10x10:')
    m = Maze(num_rows= 10, num_cols=10, start= Position(4,3), goal= Position(0,0), debug = False)
    print(m)
    print()
    
    dfs = m.dfs()
    if dfs:
        print("dfs:")
        m.showPath(dfs)
        print(f'Path length: {m._path_length}')
        print(f'Number of cells pushed: {m._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    m2 = Maze(num_rows= 10, num_cols=10, start= Position(4,3), goal= Position(0,0), debug = False)
    bfs = m2.bfs()
    if bfs:
        print("bfs:")
        m2.showPath(bfs)
        print(f'Path length: {m2._path_length}')
        print(f'Number of cells pushed: {m2._num_cells_pushed}')
    else:
        print("No path found")

    print()
    m3 = Maze(num_rows= 10, num_cols=10, start= Position(4,3), goal= Position(0,0), debug = False)
    a_star = m3.a_star()
    if a_star:
        print("A*:")
        m3.showPath(a_star)
        print(f'Path length: {m3._path_length}')
        print(f'Number of cells pushed: {m3._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    
    print('25x25:')
    m = Maze(num_rows= 25, num_cols=25, start= Position(20,13), goal= Position(0,0), debug = False)
    print(m)
    print()
    
    dfs = m.dfs()
    if dfs:
        print("dfs:")
        m.showPath(dfs)
        print(f'Path length: {m._path_length}')
        print(f'Number of cells pushed: {m._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    m2 = Maze(num_rows= 25, num_cols=25, start= Position(20,13), goal= Position(0,0), debug = False)
    bfs = m2.bfs()
    if bfs:
        print("bfs:")
        m2.showPath(bfs)
        print(f'Path length: {m2._path_length}')
        print(f'Number of cells pushed: {m2._num_cells_pushed}')
    else:
        print("No path found")

    print()
    m3 = Maze(num_rows= 25, num_cols=25, start= Position(20,13), goal= Position(0,0), debug = False)
    a_star = m3.a_star()
    if a_star:
        print("A*:")
        m3.showPath(a_star)
        print(f'Path length: {m3._path_length}')
        print(f'Number of cells pushed: {m3._num_cells_pushed}')
    else:
        print("No path found")

    print()

    print('50x50:')
    m = Maze(num_rows= 50, num_cols=50, start= Position(1,49), goal= Position(49,0), debug = False)
    print(m)
    print()
    
    dfs = m.dfs()
    if dfs:
        print("dfs:")
        m.showPath(dfs)
        print(f'Path length: {m._path_length}')
        print(f'Number of cells pushed: {m._num_cells_pushed}')
    else:
        print("No path found")
        
    print()
    m2 = Maze(num_rows= 50, num_cols=50, start= Position(1,49), goal= Position(49,0), debug = False)
    bfs = m2.bfs()
    if bfs:
        print("bfs:")
        m2.showPath(bfs)
        print(f'Path length: {m2._path_length}')
        print(f'Number of cells pushed: {m2._num_cells_pushed}')
    else:
        print("No path found")

    print()
    m3 = Maze(num_rows= 50, num_cols=50, start= Position(1,49), goal= Position(49,0), debug = False)
    a_star = m3.a_star()
    if a_star:
        print("A*:")
        m3.showPath(a_star)
        print(f'Path length: {m3._path_length}')
        print(f'Number of cells pushed: {m3._num_cells_pushed}')
    else:
        print("No path found")

if __name__ == "__main__":
    main()