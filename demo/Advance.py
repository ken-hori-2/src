


class Algorithm_advance():

    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]

        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 4 # 5 # 6
        self.COUNT = 0
        self.done = False
        self.TRIGAR = False
        self.TRIGAR_REVERSE = False
        self.BACK = False
        self.BACK_REVERSE = False
        self.on_the_way = False
        self.bf = True
        ########## parameter ##########
        self.STATE_HISTORY = []
        self.BPLIST = []
        self.PROB = []
        self.Arc = []
        self.OBS = []
        # self.next_position = []
            

    def Advance(self, STATE_HISTORY, state, TRIGAR):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR

        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))


            if not self.TRIGAR:
                if self.NODELIST[self.state.row][self.state.column] > 0.0:
                    ################################################1
                    # 本当はここで見つけた時に、現場情報のリストに格納していく
                    # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつ
                    # print("Observation : {}".format(Observation))
                    self.OBS.append(self.Observation[self.state.row][self.state.column])
                    print("OBS : {}".format(self.OBS))
                    # 本当はここで見つけた時に、現場情報のリストに格納していく
                    ################################################
                    
                    print("🪧 NODE : ⭕️")
                    self.BPLIST.append(self.state)

                    self.STATE_HISTORY.append(self.state)
                    self.STATE_HISTORY.append(self.state)
                    
                    # 一個前が1ならpopで削除
                    print("📂 Storage {}".format(self.BPLIST))
                    length = len(self.BPLIST)

                else:
                    print("🪧 NODE : ❌")

                print("Δs = {}".format(self.stress))
                
                if self.total_stress + self.stress >= 0:
                    self.total_stress += self.stress

                if self.total_stress >= self.Stressfull:
                    self.TRIGAR = True
                    print("=================")
                    print("FULL ! MAX! 🔙⛔️")
                    print("=================")
                    self.STATE_HISTORY.append(self.state)
                    # STATE_HISTORY.append(state)
                    self.COUNT += 1
                    self.BPLIST.append(self.state) # Arcを計算する為に、最初だけ必要
                    
                    # continue
                    break

            else:
                print("================\n🤖 何も処理しませんでした\n================")
                break
                
            print(f"🤖 State:{self.state}")
            self.STATE_HISTORY.append(self.state)
            print(f"Total Stress:{self.total_stress}")


            self.action, All_explore, self.Reverse = self.agent.policy_advance(self.state, self.TRIGAR) # , self.TRIGAR_REVERSE)
            # self.next_state, self.stress, self.done = self.env.step(self.action, self.TRIGAR)
            self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR, All_explore, self.Reverse)
            self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            self.state = self.next_state
            
            # self.COUNT += 1
            # print("COUNT : {}".format(self.COUNT))
            # if self.COUNT > 50:
            #     break

        # print("state_history : {}".format(self.STATE_HISTORY))

        return self.total_stress, self.STATE_HISTORY, self.state, self.TRIGAR, self.OBS, self.BPLIST