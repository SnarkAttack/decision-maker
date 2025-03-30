from copy import deepcopy

from decision_maker.base import BaseAgent, BaseAction, BaseState

class TicTacToeState(BaseState):
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.curr_player = 1

    def get_current_player(self):
        return self.curr_player
    
    def get_possible_actions(self):
        possibleActions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    possibleActions.append(TicTacToeAction(player=self.currentPlayer, x=i, y=j))
        return possibleActions
    
    def take_action(self, action):
        new_state = deepcopy(self)
        new_state.board[action.x][action.y] = action.player
        new_state.curr_player = self.player * -1
        return new_state
    
    def get_reward(self):
        for row in self.board:
            if abs(sum(row)) == 3:
                return sum(row) / 3
        for column in list(map(list, zip(*self.board))):
            if abs(sum(column)) == 3:
                return sum(column) / 3
        for diagonal in [[self.board[i][i] for i in range(len(self.board))],
                         [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]]:
            if abs(sum(diagonal)) == 3:
                return sum(diagonal) / 3
        return 0
    
class TicTacToeAction(BaseAction):
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    def __str__(self):
        return f"Player: {self.player}, ({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()