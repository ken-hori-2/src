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

from BP_Algorithm import Algorithm_bp
from EXP_Algorithm import Algorithm_exp

from agent import Agent

# from setting import Setting
from setting_large import Setting

import pprint

from advance_Algorithm import Algorithm_advance





def main():

    set = Setting()

    NODELIST, ARCLIST, Observation, map, grid = set.Infomation()

    GOAL_STATE = [0, 2]

    test = [grid, map, NODELIST, GOAL_STATE]
    
    # env = Environment(grid, NODELIST, map)
    env = Environment(*test)
    
    # agent = Agent(env, GOAL_STATE, NODELIST, map, grid)
    agent = Agent(env, *test)

    # Try 10 game.
    for i in range(1):
        
        # Initialize position of agent.
        state = env.reset()

        demo = [state, env, agent, NODELIST, Observation]

        Advance_action = Algorithm_advance(*demo)

        back_position = Algorithm_bp(*demo)

        explore_action = Algorithm_exp(*demo)

        STATE_HISTORY = []
        TRIGAR = False
        
        for i in range(6): # 4 戻るノードの個数以上は回す
            print("===================\n🐬🍏🍋test 0921 : {}\n===================".format(i))

            total_stress, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action = Advance_action.Advance(STATE_HISTORY, state, TRIGAR)

            print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Back position\n============================")

            total_stress, STATE_HISTORY, state = back_position.BP(STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action)
            
            print("============\n=🤖　🌟　⚠️ =\n============")
            print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Explore\n============================")

            total_stress, STATE_HISTORY, state = explore_action.Explore(STATE_HISTORY, state)

            print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Advance\n============================")

        print("Episode {}: Agent gets {} stress.".format(i, total_stress))
        print("state_history : {}".format(STATE_HISTORY))

        # total_stress, STATE_HISTORY = explore_action.Explore()

if __name__ == "__main__":
    main()
