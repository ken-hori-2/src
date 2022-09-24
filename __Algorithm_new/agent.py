from cgi import test
from tkinter.messagebox import NO
import numpy as np
from sklearn import preprocessing
import random


class Agent():

    # def __init__(self, env, GOAL_STATE, NODELIST, map, grid):
    def __init__(self, env, *arg):
        self.env = env
        self.actions = env.actions
        self.GOAL_REACH_EXP_VALUE = 50 # max_theta # 50
        self.lost = False
        self.test = False
        self.grid = arg[0]
        self.map = arg[1]
        self.NODELIST = arg[2]
        self.goal = arg[3]

        # self.actions = self.env.actions
        # self.goal = GOAL_STATE
        # self.NODELIST = NODELIST
        # self.map = map
        # self.grid = grid
        # print("GOAL STATE : {}".format(self.goal))

        

    def policy_advance(self, state, TRIGAR):
        
        self.TRIGAR_advance = TRIGAR

        # try:
        action = self.model_advance(state)
        self.Advance_action = action
    
        print("Action : {}".format(action))
        print("Advance action : {}".format(self.Advance_action))
        
        print("🍎 🍏 🍋 🍊 🍐")
        # return action, self.All, self.Reverse
        # except:
        if action == None:
            print("ERROR 🤖")
            self.TRIGAR_advance = True
            return self.actions[1], self.Reverse, self.TRIGAR_advance
            
        return action, self.Reverse, self.TRIGAR_advance

    def policy_bp(self, state, TRIGAR, TRIGAR_REVERSE):
        self.TRIGAR_bp = TRIGAR
        self.TRIGAR_REVERSE_bp = TRIGAR_REVERSE

        # All = False
        self.All = False
        self.Reverse = False
        # self.lost = False

        try:
            # self.lost = False
            action, self.Reverse = self.model_bp(state)
            print("Action : {}".format(action))
        except:
            print("agent / policy_bp ERROR")

            # if NOT_MOVE:
            #     self.All = True
            return self.actions[1], self.Reverse    , self.lost

        print("🍎 🍏 🍋 🍊 🍐")
        # return action, self.All, self.Reverse
        return action, self.Reverse , self.lost


    



    def policy_exp(self, state, TRIGAR):
        self.trigar = TRIGAR
        attribute = self.NODELIST[state.row][state.column]
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

        if self.NODELIST[state.row][state.column] == 1: # 2: # 今はここに入ってbp_algorithmに遷移している
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

        # next_diretion = self.advance_direction_decision(next_diretion)
        # 試しにコメントアウト0923
        # advanceの行動の優先度をあらかじめ設定

        
        print("next dir : {}".format(next_diretion))

        y_n = False
        # bp = False
        self.All = False


        self.Reverse = False

        print("========\nAdvance開始\n========")
        if not self.TRIGAR_advance:
            for dir in next_diretion:

                print("dir:{}".format(dir))
                y_n, action = self.env.expected_move(state, dir, self.TRIGAR_advance, self.All)
                # self.prev_action = action
                # print("prev action : {}".format(self.prev_action))
                
                if y_n:
                    self.prev_action = action
                    # print("prev action : {}".format(self.prev_action))
                    
                    return action
                print("y/n:{}".format(y_n))
            

        print("==========\n迷った【許容を超える】状態\n==========") # どの選択肢も y_n = False
        print("= これ以上先に現在地からゴールに迎える選択肢はない\n= 一旦体制を整える\n= 戻る")

        print("\n というよりはストレスが溜まり切る前にこれ以上進めなくなってエラーが出る")
        # # self.trigar = True
        # print("prev action2 : {}".format(self.prev_action))
        # lost = True
        # return self.prev_action

    def model_bp(self, state):

        # next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        
        print("========\nBACK 開始\n========")
        print("TRIGAR : {}".format(self.TRIGAR_bp))
        print("REVERSE : {}".format(self.TRIGAR_REVERSE_bp))
        
        if self.TRIGAR_REVERSE_bp:
            self.Reverse = True
            # next_diretion = self.next_direction_trigar() # [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion = self.next_direction_decision("reverse")
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return_reverse(state, dir, self.TRIGAR_REVERSE_bp, self.Reverse)

                if y_n:
                    self.lost = False
                    return action, self.Reverse
                print("y/n:{}".format(y_n))
            print("TRIGAR REVERSE ⚡️🏁")

            
            
        
        if self.TRIGAR_bp:
            # next_diretion = self.next_direction_trigar_reverse() # [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion = self.next_direction_decision("trigar")
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return(state, dir, self.TRIGAR_bp, self.All)

                if y_n:
                    self.lost = False
                    return action, self.Reverse
                print("y/n:{}".format(y_n))

            # add 0924
            # if not bp:
            if self.lost:
                print("==========\nこれ以上戻れない状態\n or 次のマスは以前戻った場所\n==========") # どの選択肢も y_n = False
                # self.lost = False
                # self.trigar = True
                for dir in next_diretion:
                    print("\ndir:{}".format(dir))
                    y_n, action = self.env.expected_not_move(state, dir, self.trigar, self.All)

                    if y_n:
                        return action, self.Reverse # , self.lost
                    print("y/n:{}".format(y_n))

        

        print("==========\n戻り終わった状態\n==========") # どの選択肢も y_n = False
        print("= 現在地から次にゴールに迎える選択肢を選ぶ【未探索方向】\n")
        self.lost = True







    def back_position(self, BPLIST, w, Arc):
        # try:
        Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
        # except:
        #     # Arc_INVERSE = [round(Arc[x],2) for x in range(len(Arc))]
        #     print("ERROR")
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



    def next_direction_trigar(self):
        # pass
        # advance時の行動から bp, exp の行動の優先度の決定

        if self.Advance_action == self.actions[0]: # Action.UP:
            self.BP_action = self.actions[1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[1]: # Action.DOWN:
            self.BP_action = self.actions[0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[2]: # Action.LEFT:
            self.BP_action = self.actions[3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.Advance_action == self.actions[3]: # Action.RIGHT:
            self.BP_action = self.actions[2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        return next_diretion_trigar

    def next_direction_trigar_reverse(self):
        # pass
        # advance時の行動から bp, exp の行動の優先度の決定

        if self.Advance_action == self.actions[0]: # Action.UP:
            self.BP_action = self.actions[1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[1]: # Action.DOWN:
            self.BP_action = self.actions[0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[2]: # Action.LEFT:
            self.BP_action = self.actions[3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.Advance_action == self.actions[3]: # Action.RIGHT:
            self.BP_action = self.actions[2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        return next_diretion_trigar_reverse



    def next_direction_decision(self, trigar__or__reverse):
        if self.Advance_action == self.actions[0]: # Action.UP:
            self.BP_action = self.actions[1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[1]: # Action.DOWN:
            self.BP_action = self.actions[0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[2]: # Action.LEFT:
            self.BP_action = self.actions[3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.Advance_action == self.actions[3]: # Action.RIGHT:
            self.BP_action = self.actions[2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        if trigar__or__reverse == "trigar":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar
        if trigar__or__reverse == "reverse":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar_reverse


    def advance_direction_decision(self, dir):

        
        test = random.sample(dir, len(dir))
        print("test dir : {}, dir : {}".format(test, dir))

        # test = [(self.actions[3]), (self.actions[1]), (self.actions[0]), (self.actions[1])]
        test = [(self.actions[2]), (self.actions[1]), (self.actions[3]), (self.actions[0])]
        return test # random.shuffle(dir)


        #  [<Action.RIGHT: -2>, <Action.DOWN: -1>, <Action.UP: 1>, <Action.LEFT: 2>]
