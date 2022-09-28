    
class Setting():

    def __init__(self, *arg):
        
        self.NODELIST = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] # start
        ]

        self.ARCLIST = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] # start
        ]
        
        self.Observation = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0.2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0.8, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0.1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] # start
        ]

        self.map = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0] # start
        ]
        
        self.grid = [
                [0, 9, 0, 9, 9, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 9, 0, 9, 9, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 9, 0, 9, 9, 0],
                [0, 0, 0 ,0, 0, 0],
                [9, 9, 0, 9, 9, 9]
        ]
        

    def call(self, *args):

        self.env_set = [self.NODELIST, self.ARCLIST, self.Observation, self.map, self.grid]

        return self.env_set

    def Infomation(self):
        
        return self.NODELIST, self.ARCLIST, self.Observation, self.map, self.grid