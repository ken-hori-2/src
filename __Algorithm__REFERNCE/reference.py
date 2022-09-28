
from lib2to3.pytree import Node
from sre_parse import State
import numpy as np
from itertools import count
import pprint




class Property():
    def __init__(self, *arg):

        self.Pre = arg[0]
        self.Act = arg[1]
        self.env = arg[2]
        self.Arc = arg[3]

    
    def callback(self):
        
        Node = self.Pre[:, 1]
        Arc = self.Pre[:, 0]
        print(Node)
        print(len(Node))
        print(Arc)
        sum_test = 0

        Node = Node.tolist()
        Arc = Arc.tolist()

        # for x, Act in enumerate(reversed(self.env)):
        State = 13
        stress = 0

        # Arc = int(Arc[0])
        # print(type(Arc))
        num = [int(i) for i in Arc]
        print(type(num))
        Arc_sum = sum(num)

        # print(self.env[State-10][0])
        for x in range (len(self.env)):
        
            print("=========== {} step ============".format(x))
            # print("permission : {}".format(Arc_sum-x))
            

            if self.env[State] in self.Pre:

                stress = 0
                
                index = Node.index(self.env[State][0])
                
                test = x-sum_test
                
                print("<{}> match !".format(self.env[State][0]))
                print("事前のArc : {}".format(Arc[index]))
                print("実際のArc : {}".format(test))

                sum_test += test

                # print("Arc sum : {}  == x : {}".format(Arc_sum-x, x))
                permission = Arc_sum-x
                print("----\n今の permission : {} 以内に発見\n----".format(permission))

                standard = []
                
                try:
                    standard.append(round(test/int(Arc[index]), 2))
                except:
                    standard.append(0)


                print("standard【基準距離】 : {}".format(standard[0]))

                if standard[0] != 0:
                    arc_s = round(abs(1.0-standard[0]), 2)
                else:
                    arc_s = 0.0
                print("arc stress【基準ストレス】 : {}".format(arc_s))  #このままだとArcが大きくなるとストレス値も大きくなってしまい、ストレス値の重みが変わってしまうので、基準[1]にする 
            else:
                print("no match!")
                stress += 1


            print("stress : {}".format(stress))
            print("------------\npermission : {}\n------------".format(permission))

            if stress >= permission:
                print("Stress Max")
                break


            State -= 1

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

    env = [
            ["g"],
            [""],
            [""],
            [""],
            ["C"],
            [""],
            [""],
            [""],
            ["B"],
            [""],
            ["A"],
            [""],
            [""],
            ["s"],
            # ["g"],
            # [0],
            # [0],
            # ["C"],
            # [0],
            # [0],
            # [0],
            # [0],
            # ["B"],
            # [0],
            # ["A"],
            # [0],
            # [0],
            # ["s"],
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
                # [2, "g"],
                # [3, "C"],
                # [1, "B"],
                # [2, "A"],
                # [0, "s"]
                [5, "g"],
                [6, "C"],
                [3, "B"],
                [2, "A"],
                [0, "s"]
                ])

    
    demo = [pre, act, env, pre2]

    node = Property(*demo)

    # node.callback()

    
    node.callback2()


if __name__ == "__main__":
    main()


    