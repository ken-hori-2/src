import numpy as np
from sklearn import preprocessing
import random


class Agent():

    def __init__(self, env, GOAL_STATE, NODE, map, grid):
        self.actions = env.actions
        self.GOAL_REACH_EXP_VALUE = 50 # max_theta # 50
        self.lost = False
        self.goal = GOAL_STATE
        print("GOAL STATE : {}".format(self.goal))

        self.NODE = NODE
        self.test = False

        self.map = map
        self.grid = grid

        self.env = env

    def policy_advance(self, state, TRIGAR):
        
        self.TRIGAR_advance = TRIGAR

        action = self.model_advance(state)
        
        print("Action : {}".format(action))
        
        print("🍎 🍏 🍋 🍊 🍐")
        return action, self.All, self.Reverse

    def policy_bp(self, state, TRIGAR, TRIGAR_REVERSE):
        self.TRIGAR_bp = TRIGAR
        self.TRIGAR_REVERSE_bp = TRIGAR_REVERSE

        # All = False
        # self.All = False
        self.Reverse = False

        action, self.Reverse = self.model_bp(state)
        print("Action : {}".format(action))

        print("🍎 🍏 🍋 🍊 🍐")
        return action, self.All, self.Reverse


    def back_position(self, BPLIST, w, Arc):
        Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
        w = np.round(preprocessing.minmax_scale(w), 3)
        Arc = np.round(preprocessing.minmax_scale(Arc), 3)
        Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
        print("📐正規化 w : {}, Arc : {}".format(w, Arc))
        print("📐 正規化 WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))

        # Arc = [0, 0]の時,Arc = [1, 1]に変更
        if all(elem  == 0 for elem in Arc_INVERSE):
            Arc_INVERSE = [1 for elem in Arc_INVERSE]
            print("   Arc = [0, 0]の時, Arc_INVERSE : {}".format(Arc_INVERSE))
        if all(elem  == 0 for elem in w):
            w = [1 for elem in w]
            print("   WEIGHT = [0, 0]の時, WEIGHT : {}".format(w))


        WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
        print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        if all(elem  == 0 for elem in WEIGHT_CROSS):
            print("WEIGHT CROSSは全部0です。")
            
            Arc = Arc.tolist()
            print("Arc type : {}".format(type(Arc)))
            near_index = Arc.index(min(Arc))
            print("Arc:{}, index:{}".format(Arc, near_index))
            WEIGHT_CROSS[near_index] = 1
            print("⚡️ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        # try:
        #     w = w.tolist()
        # except:
        #     pass
        # next_position = BPLIST[w.index(max(w))]
        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]

        return next_position

    def back_end(self, BPLIST, next_position, w):
        
        bpindex = BPLIST.index(next_position)
        Arc = [(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
        print("👟 Arc[移動コスト]:{}".format(Arc))
        index = Arc.index(0)
        Arc.pop(index)
        print("👟 Arc(remove 0[現在位置]):{}".format(Arc))
        print("📂 Storage {}".format(BPLIST))
        BPLIST.remove(next_position)
        print("📂 Storage(remove) {}".format(BPLIST))
        w = np.delete(w, bpindex)
        print("🥌 WEIGHT(remove):{}".format(w))

        return BPLIST, w, Arc



    def policy_exp(self, state, TRIGAR):
        self.trigar = TRIGAR
        attribute = self.NODE[state.row][state.column]
        next_direction = random.choice(self.actions)
        self.All = False
        bp = False

        self.Reverse = False
        
        try:
            y_n, action, bp = self.model_exp(state)
            
            print("y/n:{}".format(y_n))
            print("Action : {}".format(action))
        except:
            print("このノードから探索できる許容範囲は探索済み\n戻る場所決定のアルゴリズムへ")
            self.All = True
            return self.actions[1], bp, self.All, self.trigar, self.Reverse

        
        return action, bp, self.All, self.trigar, self.Reverse



    def model_exp(self, state):

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
                y_n, action = self.env.expected_move(state, dir, self.trigar, self.All)
                
                if y_n:
                    return y_n, action, bp
                print("y/n:{}".format(y_n))
            if not bp:
                print("==========\nこれ以上進めない状態\n or 次のマスは探索済み\n==========") # どの選択肢も y_n = False
                # lost = True
                self.trigar = True
                for dir in next_diretion:
                    print("\ndir:{}".format(dir))
                    y_n, action = self.env.expected_move_return(state, dir, self.trigar, self.All)

                    if y_n:
                        return y_n, action, bp
                    print("y/n:{}".format(y_n))
        else:
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return(state, dir, self.trigar, self.All)

                if y_n:
                    return y_n, action, bp
                print("y/n:{}".format(y_n))

        print("==========\n迷った状態\n==========") # どの選択肢も y_n = False
        print("= 現在地からゴールに迎える選択肢はない\n")
        lost = True


    def model_advance(self, state):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        y_n = False
        # bp = False
        self.All = False


        self.Reverse = False

        print("========\nAdvance開始\n========")
        if not self.TRIGAR_advance:
            for dir in next_diretion:

                print("dir:{}".format(dir))
                y_n, action = self.env.expected_move(state, dir, self.TRIGAR_advance, self.All)
                
                if y_n:
                    
                    return action
                print("y/n:{}".format(y_n))
            

        print("==========\n迷った【許容を超える】状態\n==========") # どの選択肢も y_n = False
        print("= これ以上先に現在地からゴールに迎える選択肢はない\n= 一旦体制を整える\n= 戻る")
        lost = True

    def model_bp(self, state):

        # next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        
        print("========\nBACK 開始\n========")
        print("TRIGAR : {}".format(self.TRIGAR_bp))
        print("REVERSE : {}".format(self.TRIGAR_REVERSE_bp))
        
        if self.TRIGAR_REVERSE_bp:
            self.Reverse = True
            next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return_reverse(state, dir, self.TRIGAR_REVERSE_bp, self.Reverse)

                if y_n:
                    return action, self.Reverse
                print("y/n:{}".format(y_n))
            print("TRIGAR REVERSE ⚡️🏁")
            
        
        if self.TRIGAR_bp:
            next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return(state, dir, self.TRIGAR_bp, self.All)

                if y_n:
                    return action, self.Reverse
                print("y/n:{}".format(y_n))

        

        print("==========\n戻り終わった状態\n==========") # どの選択肢も y_n = False
        print("= 現在地から次にゴールに迎える選択肢を選ぶ【未探索方向】\n")
        lost = True