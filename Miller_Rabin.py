import Lib
import random

# p = (2^l)*q + 1
def get_l(a):
    cnt = 0
    while 1:
        if (a&1) == 0:
            a,cnt = a>>1,cnt+1
        else:
            return cnt

def is_composite(n,q,l,a):
    a = Lib.mns(a,q,n)
    #print("a^(q) = {}".format(a))
    if (a%n) == 1:
        return "NOT Composite"
    for j in range(l):
        #print("a^(2^{}*q) = {}".format(j,a))
        if a%n == n-1:
            return "NOT Composite"
        a = Lib.mns(a,2,n)
    return "Composite"

def is_prime_by_miller_rabin(n,k):
    l = get_l(n-1)
    q = (n-1)>>1
    #print("l = {}, q = {}".format(l,q))
    while k>0:
        a = random.randint(2,n-2)
        #print("a = {}".format(a))
        ret = is_composite(n,q,l,a)
        if ret == "Composite":
            return "Composite"
        k = k-1
    return "Probably Prime"

def Probably_Prime(a,b):
    while 1:
        while 1:
            n = random.randint(a, b)
            if n % 2 == 1:
                break
        if is_prime_by_miller_rabin(n,20) == "Probably Prime":
            return n

if __name__ == "__main__":
    prime = Probably_Prime()
    print("===================")
    print("n = {}".format(prime))