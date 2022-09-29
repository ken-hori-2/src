from pprint import pprint
import numpy as np
import pprint
from reference_match_rate import Property


class Algorithm_exp():

    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]
        self.refer = Property() # arg[5]
        
        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 8 # 4 #8 # 10 # 4
        self.COUNT = 0
        self.done = False
        self.TRIGAR = False
        ########## parameter ##########
        self.STATE_HISTORY = []

        self.bp_end = False
            

    def Explore(self, STATE_HISTORY, state, TRIGAR): # , PERMISSION):

        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR

        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()
        pprint.pprint(PERMISSION)

        # self.map_unexp_area = map_unexp_area
        self.total_stress = 0
        # 初期
        index = Node.index("s")

        while not self.done:
            print("\n========== 🌟 {}steps ==========".format(self.COUNT+1))
            
            
            self.STATE_HISTORY.append(self.state)
            
            print(f"🤖 State:{self.state}")
            print("stress : {}".format(self.stress))

            # if not self.crossroad:
            self.map_unexp_area = self.env.map_unexp_area(self.state)
            if self.map_unexp_area:
                print("un explore area ! 🤖 ❓❓")
                # Add 0924################################################
                # if self.NODELIST[self.state.row][self.state.column] > 0.0:
                if self.NODELIST[self.state.row][self.state.column] in pre:


                    # ################################################
                    # # 本当はここで見つけた時に、現場情報のリストに格納していく
                    # # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつ
                    # # print("Observation : {}".format(Observation))
                    # self.OBS.append(self.Observation[self.state.row][self.state.column])
                    # print("OBS : {}".format(self.OBS))
                    # # 本当はここで見つけた時に、現場情報のリストに格納していく
                    # ################################################
                    print("🪧 NODE : ⭕️")
                    # self.BPLIST.append(self.state)
                    # self.STATE_HISTORY.append(self.state)
                    # self.STATE_HISTORY.append(self.state)
                    # 一個前が1ならpopで削除
                    # print("📂 Storage {}".format(self.BPLIST))
                # else:
                #     print("🪧 NODE : ❌")
                    
                    
                    
                    
                    # self.TRIGAR = False # ここでFalseにすることでadvance_Algorithmで撮った場所のノードも追加してしまう
                    break # Advanceに移行する？
                # Add 0924################################################

            if self.NODELIST[self.state.row][self.state.column] in pre:
                index = Node.index(self.NODELIST[self.state.row][self.state.column])
                # test = x-sum_test
            
                print("<{}> match !".format(self.NODELIST[self.state.row][self.state.column]))
                print("事前のArc : {}".format(Arc[index]))

            if self.total_stress + self.stress >= 0:
                self.total_stress += self.stress

            print("PERMISSION : {}".format(PERMISSION[index][0]))
            # if self.total_stress >= self.Stressfull:
            if self.total_stress >= PERMISSION[index][0]:
                self.TRIGAR = True
                print("=================")
                print("FULL ! MAX! 🔙⛔️")
                print("=================")
                

            if self.bp_end:

                ############コメントアウト##############
                # self.TRIGAR = False # おそらくここでFalseにしなくてもadvanceで進めなければTrueになるからここはいらない
                ############コメントアウト##############
                pass

            
            print(f"Total Stress:{self.total_stress}")
            print("trigar : {}".format(self.TRIGAR))



            self.action, self.bp_end, self.All_explore, self.TRIGAR, self.Reverse = self.agent.policy_exp(self.state, self.TRIGAR)
            print("All explore : {}".format(self.All_explore))
            if self.All_explore:
                self.env.mark_all(state)
                self.STATE_HISTORY.append(self.state)
                print("終了します")
                self.All_explore = False

                ############コメントアウト##############
                # self.TRIGAR = True
                ############コメントアウト##############
                break
            # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR, self.All_explore, self.Reverse)
            self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            self.state = self.next_state

            if self.COUNT > 150:
                break
            self.COUNT += 1

        # print("state_history : {}".format(self.STATE_HISTORY))
        if self.done:
            print("GOAL")

        return self.total_stress, self.STATE_HISTORY, self.state, self.TRIGAR