# from enum import Enum
# from pprint import pprint
# from tkinter import FIRST
from cgi import test
from lib2to3.pytree import Node
import numpy as np
# import random
# from sklearn import preprocessing
# from environment import Environment
# from bp_Algorithm import Algorithm_bp
# from exp_Algorithm import Algorithm_exp
# from agent import Agent
# from setting import Setting
from itertools import count
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
        self.node_list = arg[2]
        self.Arc = arg[3]

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

    def callback2(self):
        # for Act in self.node_list:
        #     print(Act)
        count = 4
        # for Act in reversed(self.node_list):
        # for Act in (self.node_list):
        for x, Act in enumerate(reversed(self.node_list)):
            print(x, Act)

            # if self.Pre[count][1] == Act[0]:
            #     print("<{}> match".format(Act[0]))
            
            #     count -= 1

            # if Act in self.Pre:
            #     print("<{}> match".format(Act[0]))


            #     # try:
            #     #     standard = [round(Act[0]/Pre[0],2)] #  for x in range(len(Act))]
            #     # except:
            #     #     print("ERROR")
            #     standard = []
            #     # for x in (Act):
            #     try:
            #         standard.append(round(Act[0]/Pre[0],2))
            #     except:
            #         standard.append(0)
            #     print("standard【基準ストレス】 : {}".format(standard))

            #     # arc_s = round(abs(Pre[0]-Act[0]), 2)
            #     arc_s = round(abs(1.0-standard[0]), 2)
            #     print("arc stress : {}".format(arc_s))  #このままだとArcが大きくなるとストレス値も大きくなってしまい、ストレス値の重みが変わってしまうので、基準[1]にする 
            # else:
            #     print("no match!")


        # print(self.Pre)
        # print(r[0] for r in self.Pre)

        Node = self.Pre[:, 1]
        Arc = self.Pre[:, 0]
        print(Node)
        print(len(Node))
        print(Arc)
        sum = 0

        # self.Pre_list = self.Pre.tolist()
        Node = Node.tolist()
        Arc = Arc.tolist()

        for x, Act in enumerate(reversed(self.node_list)):
        # for Pre, Act in zip(self.Pre, self.Act):
        # for x, Act in enumerate(reversed(self.node_list)):
        # for Act, arc in zip(reversed(self.node_list), reversed(Arc)):
            # test = x-sum
            print("=========== {} step ============".format(x))

            if Act in self.Pre:
                # index = self.Pre_list.index(Act[0])
                index = Node.index(Act[0])
                # index = np.where(Act)


                # print("Index : {}".format(index))

                
                test = x-sum
                # print(test)
                # print("{} <{}> match".format(x, Act[0]))
                print("<{}> match !".format(Act[0]))
                print("事前のArc : {}".format(Arc[index]))
                print("実際のArc : {}".format(test))

                sum += test

                standard = []
                # for x in (Act):
                # print(type(test), type(Arc[index]))
                # print(Arc[index])
                try:
                    standard.append(round(test/int(Arc[index]),2))
                except:
                    standard.append(0)

                # print("事前のArc : {}".format(Arc[index]))
                print("standard【基準距離】 : {}".format(standard[0]))

                if standard[0] != 0:
                    arc_s = round(abs(1.0-standard[0]), 2)
                else:
                    arc_s = 0.0
                print("arc stress【基準ストレス】 : {}".format(arc_s))  #このままだとArcが大きくなるとストレス値も大きくなってしまい、ストレス値の重みが変わってしまうので、基準[1]にする 
            else:
                print("no match!")

        print("=========== 終了します ============")

        
                
            




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

    node_list = [
            ["g"],
            [""],
            [""],
            ["C"],
            [""],
            [""],
            [""],
            [""],
            ["B"],
            [""],
            ["A"],
            [""],
            [""],
            ["s"],
    ]

    pre = [
         # [arc, node]
            [2, "g"],
            [3, "C"],
            [1, "B"],
            [2, "A"],
            [0, "s"] # start
            # ["g"],
            # ["C"],
            # ["B"],
            # ["A"],
            # ["s"] # start

            # [8, "g"],
            # [6, "C"],
            # [3, "B"],
            # [2, "A"],
            # [0, "s"] # start
        ]
    
    pre2 = [
         # [arc, node]
            [2],
            [3],
            [1],
            [2],
            [0] # start
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
    # demo = [pre, act]

    # import numpy as np

    pre = np.array([
                [2, "g"],
                [3, "C"],
                [1, "B"],
                [2, "A"],
                [0, "s"]
                ])

    # a0 = pre[:, 0]
    # a1 = pre[:, 1]
    # # a2 = A[:, 2]

    # print(a0)  # [7 2 1]
    # print(a1)  # [-3  5  4]
    # # print(a2)  # [4 8 9]
    demo = [pre, act, node_list, pre2]

    node = Property(*demo)

    # node.callback()



    # print("len:{}".format(len(node_list)))
    
    node.callback2()


if __name__ == "__main__":
    main()


    