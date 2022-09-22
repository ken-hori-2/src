


class Algorism_bp():

    
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
            

    def BP(self, STATE_HISTORY, state, TRIGAR, OBS, BPLIST):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR
        self.OBS = OBS
        self.BPLIST = BPLIST

        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))


            if self.TRIGAR_REVERSE:
                if self.BACK_REVERSE:
                    try:
                        
                        print(f"🥌 WEIGHT = {self.w}")
                        print("👟 Arc[移動コスト]:{}".format(self.Arc))
                        
                        # callback
                        self.next_position = self.agent.back_position(self.BPLIST, self.w, self.Arc)
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{self.next_position}\n==================================")
                        self.on_the_way = True
                        

                        self.BACK_REVERSE = False
                    except:
                        print("ERROR!")
                        self.STATE_HISTORY.append(self.state)
                        break
                
                if int(self.state.row) < int(self.next_position.row):
                    
                    self.TRIGAR_REVERSE = False
                    
                    # COUNT += 1
                    
                try:
                
                    if self.state == self.next_position:

                        # callback
                        self.BPLIST, self.w, self.Arc = self.agent.back_end(self.BPLIST, self.next_position, self.w)
                        self.BACK_REVERSE =True
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                        print(f"🤖 State:{self.state}")

                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        #     if total_stress + stress >= 0:
                        #         total_stress += stress

                        # 0921 統合テスト
                        print("\n============================\n🤖 🔛　アルゴリズム切り替え\n============================")
                        break
                        COUNT += 1
                        continue
                    # else:
                        
                    #     if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                    #         if total_stress + stress >= 0:
                    #             total_stress += stress

                    
                # except:
                except Exception as e:
                    print('=== エラー内容 ===')
                    print('type:' + str(type(e)))
                    print('args:' + str(e.args))
                    print('message:' + e.message)
                    print('e自身:' + str(e))
                    print("state:{}".format(self.state))
                    print("これ以上戻れません。 終了します。")
                    
                    if self.NODELIST[self.prev_state.row][self.prev_state.column] == 0: # > 0.0:
                        if self.total_stress + self.stress >= 0:
                            self.total_stress += self.stress
                    break

                

            # if self.TRIGAR:
            else:
                if self.BACK or self.bf:
                    try:
                        
                        if self.bf: # ストレスが溜まってから初回
                            # 🔑今は観測されている前提の簡単なやつ
                            self.w = self.OBS
                            print(f"🥌 WEIGHT = {self.w}")
                            # 手動で設定
                            print("手動で設定!!!!!")
                            # print("PROB : {}".format(PROB))
                            self.Arc = [(abs(self.BPLIST[-1].row-self.BPLIST[x].row)) for x in range(len(self.BPLIST))]
                            print("👟 Arc[移動コスト]:{}".format(self.Arc))
                            index = self.Arc.index(0)
                            self.Arc.pop(index)
                            print("👟 Arc(remove 0[現在位置]):{}".format(self.Arc))
                            print("📂 Storage {}".format(self.BPLIST))
                            self.BPLIST.pop(-1)
                            print("📂 Storage(remove) {}".format(self.BPLIST)) 
                        else:
                            print(f"🥌 WEIGHT = {self.w}")
                            print("👟 Arc[移動コスト]:{}".format(self.Arc))
                        self.bf = False
                        self.BACK = False
                        
                        # callback
                        self.next_position = self.agent.back_position(self.BPLIST, self.w, self.Arc)
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{self.next_position}\n==================================")
                        self.on_the_way = True

                        
                    except:
                    # except Exception as e:
                    #     print('=== エラー内容 ===')
                    #     print('type:' + str(type(e)))
                    #     print('args:' + str(e.args))
                    #     print('message:' + e.message)
                    #     print('e自身:' + str(e))
                        print("ERROR!")
                        self.STATE_HISTORY.append(self.state)

                        print("リトライ行動終了！")
                        
                        break
                
                if int(self.state.row) > int(self.next_position.row):
                    
                    self.TRIGAR_REVERSE = True
                    

                try:

                    if self.state == self.next_position:
                        
                        # callback
                        self.BPLIST, self.w, self.Arc = self.agent.back_end(self.BPLIST, self.next_position, self.w)
                        self.BACK =True
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                        print(f"🤖 State:{self.state}")

                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        #     if total_stress + stress >= 0:
                        #         total_stress += stress


                        # 0921 統合テスト
                        print("\n============================\n🤖 🔛　アルゴリズム切り替え\n============================")
                        break

                        COUNT += 1
                        continue

                    else:
                        
                        if self.on_the_way:
                            self.on_the_way = False
                        else:
                            print("🔛 On the way BACK")
                            

                        # if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        #     if total_stress + stress >= 0:
                        #         total_stress += stress
                except:
                # except Exception as e:
                #     print('=== エラー内容 ===')
                #     print('type:' + str(type(e)))
                #     print('args:' + str(e.args))
                #     print('message:' + e.message)
                #     print('e自身:' + str(e))
                    print("state:{}".format(self.state))
                    print("これ以上戻れません。 終了します。")
                    
                    if self.NODELIST[self.prev_state.row][self.prev_state.column] == 0: # > 0.0:
                        if self.total_stress + self.stress >= 0:
                            self.total_stress += self.stress


                    break # expansion 無しの場合は何回も繰り返さない
                
            print(f"🤖 State:{self.state}")
            self.STATE_HISTORY.append(self.state)
            print(f"Total Stress:{self.total_stress}")


            self.action, All_explore, self.Reverse = self.agent.policy_bp(self.state, self.TRIGAR, self.TRIGAR_REVERSE)
            # self.next_state, self.stress, self.done = self.env.step(self.action, self.TRIGAR)
            self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR, All_explore, self.Reverse)
            self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            self.state = self.next_state
            
            self.COUNT += 1
            print("COUNT : {}".format(self.COUNT))
            if self.COUNT > 50:
                break

        # print("state_history : {}".format(self.STATE_HISTORY))

        return self.total_stress, self.STATE_HISTORY, self.state