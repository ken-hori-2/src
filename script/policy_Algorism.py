import random



class Agent():

    def __init__(self, env, GOAL_STATE, NODE, map, grid):
        self.actions = env.actions
        self.GOAL_REACH_EXP_VALUE = 50 # max_theta # 50
        self.lost = False
        # self.prev_index = 0
        self.goal = GOAL_STATE
        print("GOAL STATE : {}".format(self.goal))

        self.NODE = NODE
        self.test = False

        self.map = map
        self.grid = grid

        self.env = env # Environment(self.grid, self.NODE, self.map)

    def policy(self, state, TRIGAR):
            self.trigar = TRIGAR
            attribute = self.NODE[state.row][state.column]

            next_direction = random.choice(self.actions)
            # y_n, next_state = self.model(state, depth=0)
            All = False
            bp = False
            
            try:
                y_n, action, bp = self.model(state, depth=0)
                
                print("y/n:{}".format(y_n))
                print("Action : {}".format(action))
            except:
                print("このノードから探索できる許容範囲は探索済み\n戻る場所決定のアルゴリズムへ")
                All = True
                return self.actions[1], bp, All, self.trigar
            
            return action, bp, All, self.trigar



    def model(self, state, depth):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        y_n = False
        bp = False

        if self.NODE[state.row][state.column] == 1: # 2:
                print("========\n探索終了\n========")
                self.trigar = False
                bp = True
        print("========\n探索開始\n========")
        if not self.trigar:
            for dir in next_diretion:

                print("dir:{}".format(dir))
                y_n, action = self.env.expected_move(state, dir, self.trigar)
                
                if y_n:
                    return y_n, action, bp
                print("y/n:{}".format(y_n))
            if not bp:
                print("==========\nこれ以上進めない状態\n==========") # どの選択肢も y_n = False
                # lost = True
                self.trigar = True
                for dir in next_diretion:
                    print("\ndir:{}".format(dir))
                    y_n, action = self.env.expected_move_return(state, dir, self.trigar)

                    if y_n:
                        return y_n, action, bp
                    print("y/n:{}".format(y_n))
                
        else:
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return(state, dir, self.trigar)

                if y_n:
                    return y_n, action, bp
                print("y/n:{}".format(y_n))

            print("==========\n迷った状態\n==========") # どの選択肢も y_n = False
            lost = True