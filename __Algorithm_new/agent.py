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

        

    def policy_advance(self, state, TRIGAR, action):
        
        self.TRIGAR_advance = TRIGAR
        self.prev_action = action
        print("Prev Action : {}".format(action))

        # try:
        action = self.model_advance(state)
        self.Advance_action = action
    
        print("Action : {}".format(action))
        print("Advance action : {}".format(self.Advance_action))
        
        print("๐ ๐ ๐ ๐ ๐")
        # return action, self.All, self.Reverse
        # except:
        if action == None:
            print("ERROR ๐ค")
            self.TRIGAR_advance = True
            # return self.actions[1], self.Reverse, self.TRIGAR_advance # ใใฎaction[1]ใใจใฉใผใฎๅๅ 
            return self.prev_action, self.Reverse, self.TRIGAR_advance
            
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
        # except:
        except Exception as e:
            print('=== ใจใฉใผๅๅฎน ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('e่ช่บซ:' + str(e))
            print("agent / policy_bp ERROR")

            # if NOT_MOVE:
            #     self.All = True
            return self.actions[1], self.Reverse    , self.lost

        print("๐ ๐ ๐ ๐ ๐")
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
            print("ใใฎใใผใใใๆข็ดขใงใใ่จฑๅฎน็ฏๅฒใฏๆข็ดขๆธใฟ\nๆปใๅ ดๆๆฑบๅฎใฎใขใซใดใชใบใ ใธ")
            self.All = True
            return self.actions[1], bp, self.All, self.trigar, self.Reverse

        
        return action, bp, self.All, self.trigar, self.Reverse



    def model_exp(self, state):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        y_n = False
        bp = False

        if self.NODELIST[state.row][state.column] == 1: # 2: # ไปใฏใใใซๅฅใฃใฆbp_algorithmใซ้ท็งปใใฆใใ
                print("========\nๆข็ดข็ตไบ\n========")
                self.trigar = False
                bp = True
        print("========\nๆข็ดข้ๅง\n========")
        if not self.trigar:
            for dir in next_diretion:

                print("dir:{}".format(dir))
                y_n, action = self.env.expected_move(state, dir, self.trigar, self.All)
                
                if y_n:
                    return y_n, action, bp
                print("y/n:{}".format(y_n))
            if not bp:
                print("==========\nใใไปฅไธ้ฒใใชใ็ถๆ\n or ๆฌกใฎใในใฏๆข็ดขๆธใฟ\n==========") # ใฉใฎ้ธๆ่ขใ y_n = False
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

        print("==========\n่ฟทใฃใ็ถๆ\n==========") # ใฉใฎ้ธๆ่ขใ y_n = False
        print("= ็พๅจๅฐใใใดใผใซใซ่ฟใใ้ธๆ่ขใฏใชใ\n")
        lost = True


    def model_advance(self, state):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        # next_diretion = self.advance_direction_decision(next_diretion)
        # ่ฉฆใใซใณใกใณใใขใฆใ0923
        # advanceใฎ่กๅใฎๅชๅๅบฆใใใใใใ่จญๅฎ

        
        print("next dir : {}".format(next_diretion))

        y_n = False
        # bp = False
        self.All = False


        self.Reverse = False

        print("========\nAdvance้ๅง\n========")
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
            

        print("==========\n่ฟทใฃใใ่จฑๅฎนใ่ถใใใ็ถๆ\n==========") # ใฉใฎ้ธๆ่ขใ y_n = False
        print("= ใใไปฅไธๅใซ็พๅจๅฐใใใดใผใซใซ่ฟใใ้ธๆ่ขใฏใชใ\n= ไธๆฆไฝๅถใๆดใใ\n= ๆปใ")

        print("\n ใจใใใใใฏในใใฌในใๆบใพใๅใๅใซใใไปฅไธ้ฒใใชใใชใฃใฆใจใฉใผใๅบใ")
        self.TRIGAR_advance = True
        # # self.trigar = True
        # print("prev action2 : {}".format(self.prev_action))
        # lost = True
        # return self.prev_action

    def model_bp(self, state):

        # next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        
        print("========\nBACK ้ๅง\n========")
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
            print("TRIGAR REVERSE โก๏ธ๐")

            
            
        
        if self.TRIGAR_bp:
            # next_diretion = self.next_direction_trigar_reverse() # [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion = self.next_direction_decision("trigar")
            print("TEST!!!!!")
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
                print("==========\nใใไปฅไธๆปใใชใ็ถๆ\n or ๆฌกใฎใในใฏไปฅๅๆปใฃใๅ ดๆ\n==========") # ใฉใฎ้ธๆ่ขใ y_n = False
                # self.lost = False
                # self.trigar = True
                for dir in next_diretion:
                    print("\ndir:{}".format(dir))
                    y_n, action = self.env.expected_not_move(state, dir, self.trigar, self.All)

                    if y_n:
                        return action, self.Reverse # , self.lost
                    print("y/n:{}".format(y_n))

        

        print("==========\nๆปใ็ตใใฃใ็ถๆ\n==========") # ใฉใฎ้ธๆ่ขใ y_n = False
        print("= ็พๅจๅฐใใๆฌกใซใดใผใซใซ่ฟใใ้ธๆ่ขใ้ธใถใๆชๆข็ดขๆนๅใ\n")
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
        print("๐ๆญฃ่ฆๅ w : {}, Arc : {}".format(w, Arc))
        print("๐ ๆญฃ่ฆๅ WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))

        # Arc = [0, 0]ใฎๆ,Arc = [1, 1]ใซๅคๆด
        if all(elem  == 0 for elem in Arc_INVERSE):
            Arc_INVERSE = [1 for elem in Arc_INVERSE]
            print("   Arc = [0, 0]ใฎๆ, Arc_INVERSE : {}".format(Arc_INVERSE))
        if all(elem  == 0 for elem in w):
            w = [1 for elem in w]
            print("   WEIGHT = [0, 0]ใฎๆ, WEIGHT : {}".format(w))


        WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
        print("โก๏ธ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        if all(elem  == 0 for elem in WEIGHT_CROSS):
            print("WEIGHT CROSSใฏๅจ้จ0ใงใใ")
            
            Arc = Arc.tolist()
            print("Arc type : {}".format(type(Arc)))
            near_index = Arc.index(min(Arc))
            print("Arc:{}, index:{}".format(Arc, near_index))
            WEIGHT_CROSS[near_index] = 1
            print("โก๏ธ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        # try:
        #     w = w.tolist()
        # except:
        #     pass
        # next_position = BPLIST[w.index(max(w))]
        next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))]

        return next_position

    def back_end(self, BPLIST, next_position, w, OBS):
        
        bpindex = BPLIST.index(next_position)
        Arc = [(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
        print("๐ Arc[็งปๅใณในใ]:{}".format(Arc))
        index = Arc.index(0)
        Arc.pop(index)
        print("๐ Arc(remove 0[็พๅจไฝ็ฝฎ]):{}".format(Arc))
        print("๐ Storage {}".format(BPLIST))
        BPLIST.remove(next_position)
        print("๐ Storage(remove) {}".format(BPLIST))
        w = np.delete(w, bpindex)
        print("๐ฅ WEIGHT(remove):{}".format(w))

        print("๐ฅ OBS:{}".format(OBS))
        # OBS = np.delete(OBS, bpindex)
        OBS.pop(bpindex)
        print("๐ฅ OBS(remove):{}".format(OBS))

        return BPLIST, w, Arc, OBS



    def next_direction_trigar(self):
        # pass
        # advanceๆใฎ่กๅใใ bp, exp ใฎ่กๅใฎๅชๅๅบฆใฎๆฑบๅฎ

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
        # advanceๆใฎ่กๅใใ bp, exp ใฎ่กๅใฎๅชๅๅบฆใฎๆฑบๅฎ

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

        else:
            next_diretion_trigar, next_diretion_trigar_reverse = self.next_direction_decision_prev_action()

        if trigar__or__reverse == "trigar":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar
        if trigar__or__reverse == "reverse":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar_reverse

    def next_direction_decision_prev_action(self):
        if self.prev_action == self.actions[0]: # Action.UP:
            self.BP_action = self.actions[1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.prev_action == self.actions[1]: # Action.DOWN:
            self.BP_action = self.actions[0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.prev_action == self.actions[2]: # Action.LEFT:
            self.BP_action = self.actions[3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.prev_action == self.actions[3]: # Action.RIGHT:
            self.BP_action = self.actions[2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        return next_diretion_trigar, next_diretion_trigar_reverse


    def advance_direction_decision(self, dir):

        
        test = random.sample(dir, len(dir))
        print("test dir : {}, dir : {}".format(test, dir))

        # test = [(self.actions[3]), (self.actions[1]), (self.actions[0]), (self.actions[1])]
        test = [(self.actions[2]), (self.actions[1]), (self.actions[3]), (self.actions[0])]
        return test # random.shuffle(dir)


        #  [<Action.RIGHT: -2>, <Action.DOWN: -1>, <Action.UP: 1>, <Action.LEFT: 2>]
