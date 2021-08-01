import BSGS
import Lib
import PPO_Parameter
import Pollard



def PPO(p,n,g,h,M):   # GF(M) , | <g> | = p^n , g^x = h , DLP(find x)
    print("\nPrime Power Order Algorithm Start")

    order = Lib.mns_n(p,n)

    w = Lib.mns(g,int(order/p),M)
    x_list = []
    for i in range(0,n):
        sub_x = 0
        for j in range(len(x_list)):
            sub_x+=x_list[j]*(Lib.mns_n(p,j))
        sub_h = h
        sub_g = Lib.mns(g,sub_x,M)
        sub_inverse_g = Lib.inverse(sub_g,M)
        sub_h *= sub_inverse_g

        sub_p = order
        for k in range(i+1):
            sub_p = int(sub_p/p)
        sub_h = Lib.mns(sub_h,sub_p,M)
        #x_list.append(Pollard.Pollard(w,sub_h,M,p))
        x_list.append(BSGS.dlp_bsgs(M,w,sub_h))

    x=0
    for j in range(len(x_list)):
        x += x_list[j] * (Lib.mns_n(p, j))
    return x


if __name__ =="__main__":
    #x=PPO(5,4,5448,6909,11251)

    x= PPO(2,3,38,3,41)

    #p,n,g,h,q,real_x=PPO_Parameter.PPO_Parameter()
    #x = PPO(p,n,g,h,q)
    print('x = {}'.format(x))
    #print('real x = {}'.format(real_x))
    #print(x==real_x)