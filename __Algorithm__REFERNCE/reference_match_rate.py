
from lib2to3.pytree import Node
from sre_parse import State
import numpy as np
from itertools import count
import pprint




class Property():
    def __init__(self, *arg):

        # self.Pre = arg[0]
        # self.Act = arg[1]
        # self.env = arg[2]
        # self.Arc = arg[3]
        self.pre = np.array([
                            # [2, "g"],
                            # [3, "C"],
                            # [1, "B"],
                            # [2, "A"],
                            # [0, "s"]
                            [2, "g"],
                            [3, "C"],
                            [2, "B"],
                            [3, "A"],
                            [0, "s"]
                            # [5, "g"],
                            # [6, "C"],
                            # [3, "B"],
                            # [2, "A"],
                            # [0, "s"]
                            ])

    
    def reference(self):
        
        
        Node = self.pre[:, 1]
        Arc = self.pre[:, 0]
        print(Node)
        print(Arc)
        Node = Node.tolist()
        Arc = Arc.tolist()
        num = [int(i) for i in Arc]
        print(type(num))
        Arc_sum = sum(num)
        print(Arc_sum)

        PERMISSION = [
                # [0],
                # [2],
                # [5],
                # [7],
                # [10]
                [Arc_sum-int(Arc[3])-int(Arc[2])-int(Arc[1])-int(Arc[0])],
                [Arc_sum-int(Arc[3])-int(Arc[2])-int(Arc[1])],
                [Arc_sum-int(Arc[3])-int(Arc[2])],
                [Arc_sum-int(Arc[3])],
                [Arc_sum]
        ]

        return self.pre, Node, Arc, Arc_sum, PERMISSION