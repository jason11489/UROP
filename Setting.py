import Lib
import random

def Setting():
    while (1):
        p = Lib.random_prime(400, 600)
        g = random.randint(2, p)
        n = Lib.order(g, p)
        if Lib.is_prime(n) == True:
            break
    x = random.randint(2, p)
    h = Lib.mns(g, x, p)
    return(p,g,n,h,x)

def Setting_Prime_Power():
    while (1):
        p = Lib.random_prime(3,20)
        n = random.randint(2,4)
        order = Lib.mns_n(p,n)
        g = Lib.generator(order)

    x = random.randint(2, order)
    h = Lib.mns(g, x, order)

    return(p,n,g,x,h)