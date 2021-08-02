import Lib
import random
import math
import Miller_Rabin



def DSA_Parameter(a,b):
    q = Miller_Rabin.Probably_Prime(a,int(b/4))
    while 1:
        p = Miller_Rabin.Probably_Prime(b/4,b)
        if (p-1)%q == 0:
            break
    while 1:
        h = random.randint(2,p-2)
        g = Lib.mns(h,int((p-1)/q),p)
        if g != 1:
            break
    return p,q,g


if __name__ == "__main__":
    p,q,g=DSA_Parameter(50,500)
    print('p,q,g = {},{},{}'.format(p,q,g))
    print(Lib.order(g,p))