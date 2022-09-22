from enum import Enum
from pprint import pprint
import pprint
from random import random

import random
from turtle import done

# import sys
# sys.path.append("/Users/ken/Desktop/model/src/Oneroad/explore/agent")

from environment import Environment

from EXP_Algorism import Algorism

from policy_Algorism import Agent

# mark を env の中に移動

# Action_agent copy.py
                
    

def main():


    GOAL_STATE = [0, 2]

    NODELIST = [
            [0, 9, 7, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 0, 1 ,0, 0, 0],
            [9, 9, 0, 9, 9, 9] # start
    ]

    map = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0] # start
    ]
    
    grid = [
            [0, 9, 7, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 9, 0, 9, 9, 0],
            [0, 0, 0 ,0, 0, 0],
            [9, 9, 0, 9, 9, 9] # start
    ]


    env = Environment(grid, NODELIST, map)
    
    agent = Agent(env, GOAL_STATE, NODELIST, map, grid)
    
    state = env.reset()

    demo = [state, env, agent, NODELIST]

    explore_action = Algorism(*demo)

    
    
    
    for i in range(1):
        print("===================\n🐬🍏🍋test 0921 : {}\n===================".format(i))
        
        total_stress, STATE_HISTORY = explore_action.Explore()

        print("============\n=🤖　🌟　⚠️ =\n============")
        print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent bp\n============================")
        
    print("Episode {}: Agent gets {} stress.".format(0, total_stress))
    print("state_history : {}".format(STATE_HISTORY))

main()