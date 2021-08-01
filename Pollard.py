import Lib
import random
import Setting

def F(x,n,h,g,p):
    if x[0]%3 == 1:
        return ((x[0]*h)%p,x[1],(x[2]+1)%n)
    if x[0]%3 == 0:
        return ((x[0]*x[0])%p,(2*x[1])%n,(2*x[2]%n))
    if x[0]%3 == 2:
        return ((x[0]*g)%p,(x[1]+1)%n,x[2])


def Pollard(g,h,p,n): # | <g> | = n , GF(p) ,  find x s.t. g^x = h

    cnt = 0
    while cnt < 10:
        x1 = x2 = (1,0,0)
        a= random.randint(0,p)
        b = random.randint(0,p)

        x1 = x2 = ((Lib.mns(g,a,p)*Lib.mns(h,b,p))%p,a,b)
        i=0
        while(1):
            print(i,x1,x2)
            i = i + 1
            x1,x2=F(x1,n,h,g,p),F(F(x2,n,h,g,p),n,h,g,p)
            if x1[0]==x2[0]:
                break

        print(i,x1,x2)
        T1,T2 = (x1[1]-x2[1])%n,(x2[2]-x1[2])%n
        if T2 == 0:
            print("Failure.")
            cnt = cnt + 1
        else:
            T2 = Lib.inverse(T2,n)%n
            root = (T1*T2)%n
            print("x = ", root, "(",Lib.mns(g,root,p)==h, ")")
            return root


if __name__ == "__main__":
    #p,g,n,h,x=Setting.Setting()
    p, g, n, h, x = Setting.Setting()
    print("GF({}) , | <{}> | ={}  find x s.t. {}^x = {} , ".format(p,g,n,g,h))
    print("real x is {}".format(x))
    Pollard(g,h,p,n)
    #Pollard(227,64,383,191)