import numpy as np
from sklearn import preprocessing


class Agent():

    def __init__(self, env, GOAL_STATE, NODE, map, grid):
        self.actions = env.actions

    def policy(self, state, TRIGAR, TRIGAR_REVERSE):
        # return random.choice(self.actions)
        
        if TRIGAR_REVERSE:
            print("UP")
            return (self.actions[0])
        
        elif TRIGAR:
            print("DOWN")
            return (self.actions[1])
        elif not TRIGAR:
            return (self.actions[0])


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