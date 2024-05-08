from __future__ import annotations

import random
from enum import Enum
from copy import deepcopy
from termcolor import colored

######################################################################
class Player(Enum):
    X    = "X"
    O    = "O"
    NONE = " "
    
    def __str__(self) -> str: return self.value

######################################################################
class Square:
    __slots__ = ('_player')

    def __init__(self) -> None:
        self._player: Player = Player.NONE

    def getPlayer(self) -> Player:
        return self._player

    def setPlayer(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError(f"cannot set player to object of type {type(player).__name__}")
        self._player = player

######################################################################
class Board:
    __slots__ = ('_board','_current_player')

    def __init__(self, board: list[Square] = [Square() for i in range(9)], 
                       current_player: Player = Player.X) -> None:
        ''' initializer for a TicTacToe board
        Parameters:
            board: a list of Square objects (default is all empty)
            current_player: the player to make the next move (default is X)
        '''
        self._board          : list[Square] = board
        self._current_player : Player       = current_player

    def __str__(self) -> str:
        ''' draws the Board object in traditional Tic-Tac-Toe 3x3 form 
        Returns:
            a string representation of the Board
        '''
        board_str = "\n"
        for s in range(len(self._board)):
            if self._board[s].getPlayer() == Player.NONE:
                pos_num = colored(str(s), "blue")
                board_str += f" {pos_num} "  # display the valid position number
            else:
                occupant = colored(str(self._board[s].getPlayer()), "red")
                board_str += f" {occupant} " # display the occupant
            if s % 3 < 2: board_str += '|'
            if s == 2 or s == 5: board_str += '\n' + str('-' * 11) + '\n'
        return board_str + "\n"

    @property
    def oppositePlayer(self) -> Player:
        ''' property (can treat as a variable rather than function call) to
            return the opposite of the current player
        Returns:
            Player.X if current player is O; o/w Player.O
        '''
        if self._current_player is Player.X: return Player.O
        if self._current_player is Player.O: return Player.X
        return Player.NONE

    def getCurrentPlayer(self) -> Player:
        ''' who has the current turn
        Returns:
            the current player, either Player.X or Player.O
        '''
        return self._current_player

    def getLegalMoves(self) -> list[int]:
        ''' returns a list of the still-valid moves to make
        Returns:
            a list of integers corresponding to valid moves, corresponding
            to values in [0,8] from upper-left moving in row-major order
        '''
        moves = [s for s in range(len(self._board)) \
                    if self._board[s].getPlayer() == Player.NONE]

        # randomly shuffle moves so as not to always bias toward early squares
        return random.sample(moves, len(moves))

    def getNewBoardWithMove(self, square: int) -> Board:
        ''' create a new copy of the Board that includes a given move by
            the current player at the indicated square
        Parameters:
            square: integer in [0,8] corresponding to desired Square
        Returns:
            a new Board with the current player taking the given square
        '''
        if square not in self.getLegalMoves():
            raise ValueError(f"Invalid move to square {square}")

        # create a copy of the board
        board_copy = deepcopy(self._board)

        # current player takes indicated square
        board_copy[square].setPlayer(self._current_player)

        # return a new board updated with the current move, and swap
        # to indicate opposite player as the current player
        return Board(board = board_copy, \
                     current_player = self.oppositePlayer)

    def isWin(self) -> bool:
        ''' check whether the state of this Board is a win
        Returns:
            True if the current state is with an X or O win; False o/w
        '''
        # list of possible wins in horizontal, vertical, diagonal
        possible_wins = [(0,1,2), (3,4,5), (6,7,8), \
                         (0,3,6), (1,4,7), (2,5,8), \
                         (0,4,8), (2,4,6)]
        board = self._board # just for brevity below
        for win in possible_wins:
            # check if the squares @ ordered triple locations match and aren't empty
            if board[win[0]].getPlayer() == \
               board[win[1]].getPlayer() == \
               board[win[2]].getPlayer() != Player.NONE:
                return True
        return False

    def isDraw(self) -> bool:
        ''' check whether the state of this Board is a draw
        Returns:
            True if the current board state is a draw; False o/w
        '''
        return not self.isWin() and len(self.getLegalMoves()) == 0

    def evaluate(self, originating_player: Player) -> int:
        ''' evaluates the current board state, returning 0 on a draw, 1 on a
            win, or -1 on a loss
        Parameters:
            originating_player: the player kicking off this decision-tree
                exploration to determine what that player should do
        Returns:
            1 if the tree leaf corresponds to a win for the moving player,
            -1 if the leaf corresponds to a loss, and 0 if a draw
        '''
        # this method is called at the top of minimax before the next potential
        # turn/move by the opposite player is considered -- therefore, if the
        # board is in a winning state right now (when this method is called), 
        # that means:
        #   - a loss for originating_player if the current player is the
        #       originating_player (other player won on previous move)
        #   - a win for originating_player if the current player is _not_ the
        #       originating_player (current player won on previous move)
        if self.isWin() and self._current_player == originating_player:
            return -1   # originating_player loses (other won on prev move)
        elif self.isWin() and self._current_player != originating_player:
            return 1    # originating_player wins (on prev move)
        else:
            return 0    # not (yet) a win

######################################################################
def main() -> None:
    b = Board()
    print(b)
    print(f"legal moves: {b.getLegalMoves()}")  # remember, randomly shuffled

    # simulate a game with:
    #   (a) X @ 3
    #   (b) O @ 4
    #   (c) X @ 1
    #   (d) O @ 8
    #   (e) X @ 2
    #   (f) O @ 0
    # in which O wins across NW-to-SE diagonal
    b = b.getNewBoardWithMove(3)  # X moves
    b = b.getNewBoardWithMove(4)  # O moves
    b = b.getNewBoardWithMove(1)  # X moves
    b = b.getNewBoardWithMove(8)  # O moves
    b = b.getNewBoardWithMove(2)  # X moves
    b = b.getNewBoardWithMove(0)  # O moves
    print(b)
    print(f"Is this board a win? {b.isWin()}")

    ###########
    b = Board()
    print(b)
    print(f"legal moves: {b.getLegalMoves()}")  # remember, randomly shuffled

    # simulate a game with:
    #   (a) X @ 4
    #   (b) O @ 1
    #   (c) X @ 8
    #   (d) O @ 2
    #   (e) X @ 0
    # in which X wins across NW-to-SE diagonal
    b = b.getNewBoardWithMove(4)  # X moves
    b = b.getNewBoardWithMove(1)  # O moves
    b = b.getNewBoardWithMove(8)  # X moves
    b = b.getNewBoardWithMove(2)  # O moves
    b = b.getNewBoardWithMove(0)  # X moves
    print(b)
    print(f"Is this board a win? {b.isWin()}")

if __name__ == "__main__":
    main()
