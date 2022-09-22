from enum import Enum
from tkinter import FIRST
import numpy as np
import random

# import sys
# sys.path.append("/Users/ken/Desktop/model/src/Oneroad/explore/agent")

from sklearn import preprocessing

# from Env_full import Environment
from environment import Environment

from BP_Algorism import Algorism

from policy_bp import Agent





def main():

    NODELIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0.7, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0.9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0] # start
    ]

    ARCLIST = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0.8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0] # start
    ]
    
    Observation = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0.7, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0.9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0] # start
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
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
    ]
    # env = Environment(grid, NODELIST)
    # agent = Agent(env)

    GOAL_STATE = [0, 2]
    
    env = Environment(grid, NODELIST, map)
    
    agent = Agent(env, GOAL_STATE, NODELIST, map, grid)

    # Try 10 game.
    for i in range(1):
        
        # Initialize position of agent.
        state = env.reset()

        demo = [state, env, agent, NODELIST, Observation]

        back_position = Algorism(*demo)
        
        for i in range(3):
            print("===================\n🐬🍏🍋test 0921 : {}\n===================".format(i))

            total_stress, STATE_HISTORY = back_position.BP()
            
            print("============\n=🤖　🌟　⚠️ =\n============")
            print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent policy\n============================")

        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

if __name__ == "__main__":
    main()
