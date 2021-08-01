import Lib
import math

def dlp_bsgs(p,g,h):
    print("\nBig Step Giant Step Algorithm Start")
    m = 1+math.floor(math.sqrt(p-1))
    #print("m = {} = 0x{:x}".format(m,m))
    L,t = [],1

    for j in range(m):
        L = L + [[j,t]]
        t = (t*g)%p

    #print("L1 ="); Lib.show_list(L)
    Lib.quick_sort(L,0,len(L)-1,1)
    #print("Sorted L1 = "); Lib.show_list(L)

    inv_g = Lib.inverse(g,p)
    w,t=Lib.mns(inv_g,m,p),h
    root = "UNKNOWN"
    L2 = []
    for j in range(m):
        L2 = L2 + [[j,t]]
        i = Lib.bin_search(L,t)
        if i != Lib.NO_ELEMENT:
            #print("L2 = "); Lib.show_list(L2)
            #print("(i,g^i) = ({},{})".format(i,Lib.mns(g,i,p)))
            #print("(j,hg^(-jm)) = ({},{})".format(j,t))
            root = (i+m*j)%(p-1)   # p-1 : group order
            break
        t = (t*w)%p

    #print("x =",root);print(Lib.mns(g,root,p)==h)
    return root

if __name__ =="__main__":
    p = 499
    g = 7
    h = 387
    print("[Problem] {}^x = {} over GF({})".format(g,h,p))
    dlp_bsgs(p,g,h)