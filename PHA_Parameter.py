import random
import Lib
import Miller_Rabin


def Prime_Parameter():
    prime = Miller_Rabin.Probably_Prime(2,10000)
    g = random.randint(2,prime-1)   # <g>
    x = random.randint(2,int(prime/2))
    h = Lib.mns(g,x,prime)
    order_g = Lib.order(g,prime)
    return (prime,g,x,h,order_g)
    #GF(prime) g^x = h s.t. find x
    '''
    prime = Lib.random_prime(20,200)
    g = random.randint(2,prime-1)   # <g>
    x = random.randint(2,int(prime/2))
    h = Lib.mns(g,x,prime)
    order_g = Lib.order(g,prime)
    return (prime,g,x,h,order_g)
    #GF(prime) g^x = h s.t. find x
    '''

def PHA_Parameter(a,b):
    prime = Miller_Rabin.Probably_Prime(a,b)
    g = random.randint(2,prime-1)   # <g>
    x = random.randint(2,int(prime/5))
    h = Lib.mns(g,x,prime)
    order_g = Lib.order(g,prime)
    return (prime,g,x,h,order_g)
    #GF(prime) g^x = h s.t. find x
    '''
        prime = Lib.random_prime(20,200)
    g = random.randint(2,prime-1)   # <g>
    x = random.randint(2,int(prime/5))
    h = Lib.mns(g,x,prime)
    order_g = Lib.order(g,prime)
    return (prime,g,x,h,order_g)
    #GF(prime) g^x = h s.t. find x
    '''



if __name__=="__main__":
    prime,g,x,h,order_g = PHA_Parameter()
    print("prime,g,x,h,order_g = {}, {}, {}, {}, {}".format(prime,g,x,h,order_g))
    print(Lib.mns(g,x,prime)==h)
    print(Lib.mns(g,order_g,prime)==1)