
import math

class Algorithm_bp():

    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]

        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 8 # 10 # 4
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
            

    def BP(self, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR
        self.OBS = OBS
        self.BPLIST = BPLIST
        self.Advance_action = action
        # test
        # self.lost = False
        self.bf = True
        self.Add_Advance = Add_Advance

        # if self.Advance_action == self.env.actions[1]:
        #     print("Advance action : {}".format(self.Advance_action))

        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))


            if self.TRIGAR_REVERSE:
                if self.BACK_REVERSE:
                    try:
                        
                        print(f"๐ฅ WEIGHT = {self.w}")
                        print("๐ Arc[็งปๅใณในใ]:{}".format(self.Arc))

                        print("๐ Storage {}".format(self.BPLIST))
                        
                        # callback
                        self.next_position = self.agent.back_position(self.BPLIST, self.w, self.Arc)
                        print(f"========Decision Next State=======\nโ ๏ธ  NEXT POSITION:{self.next_position}\n==================================")
                        self.on_the_way = True
                        

                        self.BACK_REVERSE = False
                    except:
                        print("ERROR!")
                        self.STATE_HISTORY.append(self.state)
                        break
                
                # if int(self.state.row) < int(self.next_position.row):
                    
                #     self.TRIGAR_REVERSE = False
                if self.Advance_action == self.env.actions[0]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.row) < int(self.next_position.row):
                        self.TRIGAR_REVERSE = False
                elif self.Advance_action == self.env.actions[1]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.row) > int(self.next_position.row):
                        self.TRIGAR_REVERSE = False
                elif self.Advance_action == self.env.actions[2]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.column) < int(self.next_position.column):
                        self.TRIGAR_REVERSE = False
                elif self.Advance_action == self.env.actions[3]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.column) > int(self.next_position.column):
                        self.TRIGAR_REVERSE = False

                
                    
                try:
                
                    if self.state == self.next_position:

                        # callback
                        self.BPLIST, self.w, self.Arc, self.OBS = self.agent.back_end(self.BPLIST, self.next_position, self.w, self.OBS)
                        self.BACK_REVERSE =True
                        print("๐ ARRIVE AT BACK POSITION (ๆปใ็ตใใใพใใใ)")
                        print(f"๐ค State:{self.state}")

                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        
                        
                        # 0921 ็ตฑๅใในใ
                        print("\n============================\n๐ค ๐ใใขใซใดใชใบใ ๅใๆฟใ\n============================")
                        break
                        
                except:
                # except Exception as e:
                #     print('=== ใจใฉใผๅๅฎน ===')
                #     print('type:' + str(type(e)))
                #     print('args:' + str(e.args))
                #     print('message:' + e.message)
                #     print('e่ช่บซ:' + str(e))
                    print("state:{}".format(self.state))
                    print("ใใไปฅไธๆปใใพใใใ ็ตไบใใพใใ")
                    
                    if self.NODELIST[self.prev_state.row][self.prev_state.column] == 0: # > 0.0:
                        if self.total_stress + self.stress >= 0:
                            self.total_stress += self.stress
                    break

                

            # if self.TRIGAR:
            else:
                if self.BACK or self.bf:
                    try:
                        
                        if self.bf: # ในใใฌในใๆบใพใฃใฆใใๅๅ
                            # ๐ไปใฏ่ฆณๆธฌใใใฆใใๅๆใฎ็ฐกๅใชใใค
                            self.w = self.OBS
                            print(f"๐ฅ WEIGHT = {self.w}")
                            # ๆๅใง่จญๅฎ
                            print("ๆๅใง่จญๅฎ!!!!!")
                            # print("PROB : {}".format(PROB))
                            # self.Arc = [(abs(self.BPLIST[-1].row-self.BPLIST[x].row)) for x in range(len(self.BPLIST))]

                            if self.Add_Advance:
                                # add 0923 ็ด็ท่ท้ข
                                self.Arc = [math.sqrt((self.BPLIST[-1].row - self.BPLIST[x].row) ** 2 + (self.BPLIST[-1].column - self.BPLIST[x].column) ** 2) for x in range(len(self.BPLIST))]


                                print("๐ Arc[็งปๅใณในใ]:{}".format(self.Arc))
                                index = self.Arc.index(0)
                                self.Arc.pop(index)
                                print("๐ Arc(remove 0[็พๅจไฝ็ฝฎ]):{}".format(self.Arc))
                                print("๐ Storage {}".format(self.BPLIST))


                                # if self.Add_Advance:
                                self.BPLIST.pop(-1) # advanceใขใใใณในใง่ฟฝๅ ใใ็พๅจๅฐใฎๆใๅ้ค
                                # ใงใใadvanceใง่ฟฝๅ ใใฆใชใๆใฏๆถใใกใใใใชใ
                                # ใใใใใขใผใฏใๆถใใฆใใพใฃใฆใใ๏ผ๏ผ

                            
                                print("๐ Storage(remove) {}".format(self.BPLIST))

                            print("๐ Arc[็งปๅใณในใ]:{}".format(self.Arc))
                            print("๐ Arc(remove 0[็พๅจไฝ็ฝฎ]):{}".format(self.Arc))
                            print("๐ Storage {}".format(self.BPLIST))

                            
                        else:
                            print(f"๐ฅ WEIGHT = {self.w}")
                            print("๐ Arc[็งปๅใณในใ]:{}".format(self.Arc))

                            print("๐ Storage {}".format(self.BPLIST))
                        self.bf = False
                        self.BACK = False
                        
                        # callback
                        self.next_position = self.agent.back_position(self.BPLIST, self.w, self.Arc)
                        print(f"========Decision Next State=======\nโ ๏ธ  NEXT POSITION:{self.next_position}\n==================================")
                        self.on_the_way = True

                        
                    except:
                    # except Exception as e:
                    #     print('=== ใจใฉใผๅๅฎน ===')
                    #     print('type:' + str(type(e)))
                    #     print('args:' + str(e.args))
                    #     print('message:' + e.message)
                    #     print('e่ช่บซ:' + str(e))
                        print("ERROR!")
                        self.STATE_HISTORY.append(self.state)

                        print("ใชใใฉใค่กๅ็ตไบ๏ผ")
                        
                        break
                
                # if int(self.state.row) > int(self.next_position.row):
                    
                #     self.TRIGAR_REVERSE = True

                if self.Advance_action == self.env.actions[0]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.row) > int(self.next_position.row):
                        self.TRIGAR_REVERSE = True
                elif self.Advance_action == self.env.actions[1]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.row) < int(self.next_position.row):
                        self.TRIGAR_REVERSE = True
                elif self.Advance_action == self.env.actions[2]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.column) > int(self.next_position.column):
                        self.TRIGAR_REVERSE = True
                elif self.Advance_action == self.env.actions[3]:
                    print("Advance action : {}".format(self.Advance_action))
                    if int(self.state.column) < int(self.next_position.column):
                        self.TRIGAR_REVERSE = True
                    

                try:

                    if self.state == self.next_position:

                        # self.lost = False
                        
                        # callback
                        self.BPLIST, self.w, self.Arc, self.OBS = self.agent.back_end(self.BPLIST, self.next_position, self.w, self.OBS)
                        self.BACK =True
                        print("๐ ARRIVE AT BACK POSITION (ๆปใ็ตใใใพใใใ)")
                        print(f"๐ค State:{self.state}")
                        print("OBS : {}".format(self.OBS))

                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        
                        # if NODELIST[prev_state.row][prev_state.column] == 0: # > 0.0:
                        #     if total_stress + stress >= 0:
                        #         total_stress += stress


                        # 0921 ็ตฑๅใในใ
                        print("\n============================\n๐ค ๐ใใขใซใดใชใบใ ๅใๆฟใ\n============================")
                        break

                        COUNT += 1
                        continue

                    else:
                        
                        if self.on_the_way:
                            self.on_the_way = False
                        else:
                            print("๐ On the way BACK")

                    # if self.lost:
                    #     print("==========\nใใไปฅไธๆปใใชใ็ถๆ\n==========")
                        
                        
                except:
                # except Exception as e:
                #     print('=== ใจใฉใผๅๅฎน ===')
                #     print('type:' + str(type(e)))
                #     print('args:' + str(e.args))
                #     print('message:' + e.message)
                #     print('e่ช่บซ:' + str(e))
                    print("state:{}".format(self.state))
                    print("ใใไปฅไธๆปใใพใใใ ็ตไบใใพใใ")
                    
                    if self.NODELIST[self.prev_state.row][self.prev_state.column] == 0: # > 0.0:
                        if self.total_stress + self.stress >= 0:
                            self.total_stress += self.stress


                    break # expansion ็กใใฎๅ ดๅใฏไฝๅใ็นฐใ่ฟใใชใ
                
            print(f"๐ค State:{self.state}")
            self.STATE_HISTORY.append(self.state)
            print(f"Total Stress:{self.total_stress}")

            print("TRIGAR : {}".format(self.TRIGAR))


            # self.action, All_explore, self.Reverse = self.agent.policy_bp(self.state, self.TRIGAR, self.TRIGAR_REVERSE)
            self.action, self.Reverse   , self.lost = self.agent.policy_bp(self.state, self.TRIGAR, self.TRIGAR_REVERSE)

            # self.next_state, self.stress, self.done = self.env.step(self.action, self.TRIGAR)

            # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR, All_explore, self.Reverse)
            self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            self.prev_state = self.state # 1ใคๅใฎในใใใใไฟๅญ -> ๅพใงในใใฌในใฎๆธๅฐใซไฝฟใ
            self.state = self.next_state
            
            
            print("COUNT : {}".format(self.COUNT))
            if self.COUNT > 150:
                break
            self.COUNT += 1

        # print("state_history : {}".format(self.STATE_HISTORY))

        return self.total_stress, self.STATE_HISTORY, self.state, self.OBS