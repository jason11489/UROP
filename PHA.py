import Lib
import PPO
import PHA_Parameter

def PHA(n,g,h,M):
    list_M = []
    list_A = []
    num_n = 1
    for i in n:
        num_n = num_n * (Lib.mns_n(i[0],i[1]))

    for i in range(len(n)):
        sub_order = Lib.mns_n(n[i][0],n[i][1])
        power_g_i = sub_order
        power_g_i = int(num_n/power_g_i)
        g_i = Lib.mns(g,power_g_i,M)
        h_i = Lib.mns(h,power_g_i,M)
        list_M.append(sub_order)

        x_i = PPO.PPO(n[i][0],n[i][1],g_i,h_i,M)
        list_A.append(x_i)

    final_x = Lib.chinese_remainder(list_A,list_M)
    return final_x




if __name__ =="__main__":
    prime,g,x,h,order_g = PHA_Parameter.PHA_Parameter()
    print("GF({}) , G = <{}> , |G| = {} , {}^{} = {}".format(prime,g,order_g,g,x,h))
    #n = [(2,4),(104729,8),(224737,8),(350377,4)]
    #PHA_sol = int(PHA(n,71,210,251))
    n = Lib.factor(order_g)
    print("|G| = ",end="")
    for k in n:
        print("{}^{} ".format(k[0],k[1]),end="")
    print("\n===============================")
    PHA_sol = int(PHA(n,g,h,prime))
    print("\n===============================")
    real_x=x
    print("PHA_sol = {}".format(PHA_sol))
    print('real_x = {}'.format(real_x))