from enum import Enum
from pprint import pprint
import pprint
from random import random

import random


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        
        return "[{}, {}]".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
        
class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2

class Environment():

    def __init__(self, grid, NODELIST, map):
        
        self.agent_state = State()
        self.reset()

        self.grid = grid

        self.NODELIST = NODELIST

        self.default_stress = 1

        # self.s = s

        self.map = map

    @property
    def row_length(self):
        return len(self.grid)

    @property
    def column_length(self):
        return len(self.grid[0])

    @property
    def actions(self):
        return [Action.UP, Action.DOWN,
                Action.LEFT, Action.RIGHT]

    def reset(self):
        # self.agent_state = State(6, 2)
        self.agent_state = State(5, 2)
        # self.agent_state = State(6, 0)
        return self.agent_state

    def can_action_at(self, state):
        if self.grid[state.row][state.column] == 0:
            return True
        else:
            # self.s += 1
            return False

    def _move(self, state, action, TRIGAR, All, Reverse):

        if Reverse:
            self.mark_reverse(state)
        else:
            self.mark(state, TRIGAR, All)


        if not self.can_action_at(state):
            
            raise Exception("Can't move from here!")

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.LEFT:
            next_state.column -= 1
        elif action == Action.RIGHT:
            next_state.column += 1

        # Check whether a state is out of the grid.
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            # self.s += 1
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            # self.s += 1
            

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            # self.s += 1

        stress, done = self.stress_func(next_state, TRIGAR) # 上だと沼る
        
        
        # self.mark(state, TRIGAR) # 0920コメントアウト
        # self.mark(next_state, TRIGAR)
        # 0920 追加
        pprint.pprint(self.map)

        

        return next_state, stress, done # , self.s

    def stress_func(self, state, TRIGAR):
       
        done = False

        # Check an attribute of next state.
        attribute = self.NODELIST[state.row][state.column]

        if attribute == 7:
            done = True

        if TRIGAR:
            stress = -self.default_stress
        else:
            
            if attribute > 0.0:
                # Get reward! and the game ends.
                stress = 0 # -1 # 0                              # ここが reward = None の原因 or grid の 1->0 で解決
            else:
                stress = self.default_stress


        return stress, done

    def mark(self, state, TRIGAR, All): # , Reverse):

        attribute = self.NODELIST[state.row][state.column]

        self.map[state.row][state.column] = 1

        # if not Reverse:
        if TRIGAR:
            self.map[state.row][state.column] = 2 # こっちが先でないとノードの場所に戻ってもmapに1を上書きできない
            
        # if not All:
        #     if attribute == 1:
        #         self.map[state.row][state.column] = 1 # 5
        # elif attribute == 2:
        #     self.map[state.row][state.column] = 1

        # if Reverse:
        #     self.map[state.row][state.column] = 1

        if All:
            self.mark_all(state)

        
        
        
    def mark_all(self, state): # , All):

        # if All:
        self.map[state.row][state.column] = 2

        pprint.pprint(self.map)

    def mark_reverse(self, state): # , All):

        # if All:
        self.map[state.row][state.column] = 1

        pprint.pprint(self.map)

    def expected_move(self, state, action, TRIGAR, All):
        
        next_state = state.clone()

        test = True

        # 0920
        self.mark(state, TRIGAR, All)

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.LEFT:
            next_state.column -= 1
        elif action == Action.RIGHT:
            next_state.column += 1
        
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            test = False
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            test = False

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            test = False
        
        if self.map[next_state.row][next_state.column] >= 1: # == 1:
            next_state = state
            test = False

        return test, action # , next_state

    def expected_move_return(self, state, action, TRIGAR, All):
        
        next_state = state.clone()

        test = False

        # 0920
        self.mark(state, TRIGAR, All)


        # self.map[state.row][state.column] = 2

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.LEFT:
            next_state.column -= 1
        elif action == Action.RIGHT:
            next_state.column += 1
        
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            test = False
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            test = False

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            test = False
        
        if self.map[next_state.row][next_state.column] == 1:
            next_state = state
            print("🌟 ⚠️")
            # pprint.pprint(self.map)
            test = True

        return test, action # , next_state

    def expected_move_return_reverse(self, state, action, TRIGAR, REVERSE): # All):
        
        next_state = state.clone()

        test = False

        # 0920
        # self.mark(state, TRIGAR, All)
        self.mark_reverse(state) # , REVERSE)


        # self.map[state.row][state.column] = 2

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.LEFT:
            next_state.column -= 1
        elif action == Action.RIGHT:
            next_state.column += 1
        
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            test = False
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            test = False

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state
            test = False
        
        if self.map[next_state.row][next_state.column] == 1:
            next_state = state
            # print("🌟 ⚠️")
            # pprint.pprint(self.map)
            test = False # True
        if self.map[next_state.row][next_state.column] == 2:
            next_state = state
            print("🌟 ⚠️")
            # pprint.pprint(self.map)
            test = True

        return test, action # , next_state