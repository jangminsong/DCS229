from Board import *
from math import inf

################################################################################
def minimax(current_board:      Board, \
            is_maximizing:      bool, \
            originating_player: Player, \
            current_depth:      int, \
            debug:              bool = False) -> int:
    ''' method to implement the minimax algorithm, recursively exploring
        the tic-tac-toe board's options for the originating player at this
        step
    Parameters:
        current_board: a Board object, in the state _before_ originating_player
            makes its next move
        is_maximizing: whether the originating_player should be trying to
            maximize the outcome (in the case of X, who is trying to win) or
            should be trying to minimize the outcome (in the case of O, who
            is trying to prevent X from winning)
        originating_player: the Player who is kicking off this particular 
            board-state decision tree exploration of possible future moves
        current_depth: integer corresponding to the current depth in the
            board-state exploration decision tree
        debug: if True, prints debugging information
    Returns:
        integer corresponding to the best evaluation if maximizing (i.e.,
            Player.X) or the worst evaluation if minimizing (i.e., Player.O)
    '''
    if current_board.isWin() or current_board.isDraw():
        return current_board.evaluate(originating_player)
    if is_maximizing:
        best_result = -inf
        for move in current_board.getLegalMoves():
            is_maximizing = False
            result = minimax(current_board.getNewBoardWithMove(move), is_maximizing, originating_player,current_depth+1)
            if result > best_result:
                best_result = result
        return best_result
    else:
        worst_result = inf
        for move in current_board.getLegalMoves():
            is_maximizing = True
            result = minimax(current_board.getNewBoardWithMove(move), is_maximizing, originating_player,current_depth+1)
            if result < worst_result:
                worst_result = result
        return worst_result

################################################################################
def findBestMove(current_board: Board, debug: bool = False) -> int:
    ''' Function for the computer (which we assume to be O, going second) to
        find its best possible move among all remaining moves.  This is
        accomplished by calling the recursive minimax, which will alternate
        player turns, with those players alternating minimizing and maximizing
        (i.e., O is trying to minimize X's outcome, while X is trying to
        maximize X's outcome).
    Parameters:
        current_board: a Board object, the current board state
        debug: boolean -- if True, prints debugging info
    Returns:
        the evaluation of the best move for the computer (typically computer is
        O and the user/player is X) -- 1 if leading to a win, -1 if leading to
        a loss, 0 if leading to a draw
    '''
    best_result = -inf
    best_move   = None
    for move in current_board.getLegalMoves():
        if debug: print(f"{current_board.getCurrentPlayer()} exploring {move}")
        # determine the eventual outcome when O tries the current move,
        # by exploring all possible outcomes along the decision tree when
        # O tries that move
        updated_board      = current_board.getNewBoardWithMove(move)
        originating_player = current_board.getCurrentPlayer()
        is_maximizing      = False  # O will attempt to minimize X's outcome
        current_depth      = 0      # depth at start of this exploration
        result = minimax(current_board      = updated_board, \
                         is_maximizing      = False, \
                         originating_player = originating_player, \
                         current_depth      = current_depth, \
                         debug              = debug)
        # keep track of best outcome that can occur across all O's possible moves
        if result > best_result:
            best_result = result
            best_move   = move
    return best_move

################################################################################
def getPlayerMove(board: Board) -> int | None:
    ''' ask the user for a valid board space, returning that integer 
    Parameters:
        board: the current state of the board
    Returns:
        a valid integer in [0,8] corresponding to an open square,
        or None if user interrupts game
    '''
    player_move = None
    while player_move not in board.getLegalMoves():
        try:
            player_move = int(input("Enter a legal square (0-8): "))
        except KeyboardInterrupt:
            # control-C to kill, returning None back to play()
            return None
        except:
            pass  # ignore and loop back if input is invalid

    return player_move

################################################################################
def checkForEnd(board: Board, player: Player) -> bool:
    ''' checks whether game is over, whether win, lose, or draw, and
        prints a corresponding message if so
    Parameters:
        board:  the current state of the game board
        player: the Player making the current move
    Returns:
        True if game is over; False o/w
    '''
    if board.isWin():
        print(f"{player} wins!")
        return True
    elif board.isDraw():
        print("It's a draw!")
        return True
    return False

################################################################################
def play(debug: bool = False) -> None:
    ''' function to control game play for Tic Tac Toe
    Parameters:
        debug: boolean; prints debugging output if True
    '''
    board = Board()
    print(board)

    # main game loop
    while True:
        # assume the human player goes first as 'X'
        human_move = getPlayerMove(board)
        if human_move is None: return  # ctrl-C to exit

        board = board.getNewBoardWithMove(human_move)
        print(board)
        if checkForEnd(board, Player.X):
            # game is over -- bail out
            break

        # then the computer gets to determine its best move via minimax,
        # trying to maximize its own score by minimizing user's score
        computer_move = findBestMove(board, debug)
        print(f"Computer's move is {computer_move}")
        board = board.getNewBoardWithMove(computer_move)
        print(board)
        if checkForEnd(board, Player.O):
            # game is over -- bail out
            break

################################################################################
if __name__ == "__main__":
    #play(debug = True)
    play()
