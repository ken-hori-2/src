# from enum import Enum
# from pprint import pprint
# from tkinter import FIRST
# import numpy as np
# import random
# from sklearn import preprocessing
# from environment import Environment
# from bp_Algorithm import Algorithm_bp
# from exp_Algorithm import Algorithm_exp
# from agent import Agent
# from setting import Setting
import pprint
# from advance_Algorithm import Algorithm_advance





from re import A


class Property():
    def __init__(self, *arg):

        # # self.state = arg[0] # state
        # # self.env = arg[1] # env
        # # self.agent = arg[2] # agent
        # self.NODELIST = arg[0] # [3] # NODELIST
        # self.ARCLIST = arg[1]
        # self.Observation = arg[2] # [4]
        # self.TEST = arg[3]
        self.Pre = arg[0]
        self.Act = arg[1]

    def callback(self):
        

        for Pre, Act in zip(self.Pre, self.Act):
            
            print("\nPre: {}".format(Pre))
            print("Act: {}".format(Act))
            if Pre[1] == Act[1]:
                
                print("<{}> match".format(Act[1]))

                try:
                    standard = [round(Act[0]/Pre[0],2)] #  for x in range(len(Act))]
                except:
                    print("ERROR")
                    standard = []
                    # for x in (Act):
                    try:
                        standard.append(round(Act[0]/Pre[0],2))
                    except:
                        standard.append(0)
                print("standard【基準ストレス】 : {}".format(standard))

                # arc_s = round(abs(Pre[0]-Act[0]), 2)
                arc_s = round(abs(1.0-standard[0]), 2)
                print("arc stress : {}".format(arc_s))  #このままだとArcが大きくなるとストレス値も大きくなってしまい、ストレス値の重みが変わってしまうので、基準[1]にする 
            else:
                print("no match!")
            # print(Pre, Act)
                
            




def main():

    # set = Setting()

    # NODELIST, ARCLIST, Observation, map, grid = set.Infomation()

    test = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0] # start
        ]

    pre = [
         # [arc, node]
            [2, "g"],
            [3, "C"],
            [1, "B"],
            [2, "A"],
            [0, "s"] # start

            # [8, "g"],
            # [6, "C"],
            # [3, "B"],
            # [2, "A"],
            # [0, "s"] # start
        ]

    act = [
         # [arc, node]
            [2.2, "g"],
            [3.1, "x"],
            [1.3, "B"],
            [2.1, "A"],
            [0, "s"] # start
        ]
    # demo = [NODELIST, ARCLIST, Observation, test]
    demo = [pre, act]

    node = Property(*demo)

    node.callback()


if __name__ == "__main__":
    main()


    