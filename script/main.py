from enum import Enum
from pprint import pprint
from tkinter import FIRST
import numpy as np
import random

# import sys
# sys.path.append("/Users/ken/Desktop/model/src/Oneroad/explore/agent")

from sklearn import preprocessing

# from Env_full import Environment
from environment import Environment

from BP_Algorism import Algorism_bp
from EXP_Algorism import Algorism_exp

# from policy_bp import Agent_bp
# from policy_Algorism import Agent_exp
from agent import Agent

from setting import Setting

import pprint





def main():

    set = Setting()

    NODELIST, ARCLIST, Observation, map, grid = set.Infomation()

    GOAL_STATE = [0, 2]
    
    env = Environment(grid, NODELIST, map)
    
    agent = Agent(env, GOAL_STATE, NODELIST, map, grid)

    # Try 10 game.
    for i in range(1):
        
        # Initialize position of agent.
        state = env.reset()

        demo = [state, env, agent, NODELIST, Observation]

        back_position = Algorism_bp(*demo)

        explore_action = Algorism_exp(*demo)

        STATE_HISTORY = []
        
        for i in range(4):
            print("===================\n🐬🍏🍋test 0921 : {}\n===================".format(i))

            total_stress, STATE_HISTORY, state = back_position.BP(STATE_HISTORY, state)
            
            print("============\n=🤖　🌟　⚠️ =\n============")
            print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent policy\n============================")

            total_stress, STATE_HISTORY, state = explore_action.Explore(STATE_HISTORY, state)

        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

        # total_stress, STATE_HISTORY = explore_action.Explore()

if __name__ == "__main__":
    main()
