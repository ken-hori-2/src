


class Algorism_exp():

    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]
        
        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 4 # 10
        self.COUNT = 0
        self.done = False
        self.TRIGAR = False
        ########## parameter ##########
        self.STATE_HISTORY = []

        self.bp_end = False
            

    def Explore(self, STATE_HISTORY, state):

        self.STATE_HISTORY = STATE_HISTORY
        self.state = state

        while not self.done:
            print("\n========== 🌟 {}steps ==========".format(self.COUNT+1))
            
            
            self.STATE_HISTORY.append(self.state)
            
            print(f"🤖 State:{self.state}")
            print("stress : {}".format(self.stress))

            if self.total_stress + self.stress >= 0:
                self.total_stress += self.stress

            if self.total_stress >= self.Stressfull:
                self.TRIGAR = True
                print("=================")
                print("FULL ! MAX! 🔙⛔️")
                print("=================")
                

            if self.bp_end:
                self.TRIGAR = False

            
            print(f"Total Stress:{self.total_stress}")
            print("trigar : {}".format(self.TRIGAR))



            self.action, self.bp_end, self.All_explore, self.TRIGAR = self.agent.policy_exp(self.state, self.TRIGAR)
            if self.All_explore:
                # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
                self.STATE_HISTORY.append(self.state)
                print("終了します")
                break
            self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            self.state = self.next_state
            # if self.All_explore:
            #     # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            #     self.STATE_HISTORY.append(self.state)
            #     print("終了します")
            #     break

            if self.COUNT > 40: # 26: # 18: # 0:
                break
            self.COUNT += 1

        # print("state_history : {}".format(self.STATE_HISTORY))
        if self.done:
            print("GOAL")

        return self.total_stress, self.STATE_HISTORY, self.state