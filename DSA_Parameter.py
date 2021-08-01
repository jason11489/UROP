import Lib
import random
import math

def random_prime(a,b):
    prime_list = []
    for sub_num in range(a,b+1):
        flag = True
        for n in range(2,int(math.sqrt(sub_num))):
            if sub_num % n == 0:
                flag = False

        if flag:
            prime_list.append(sub_num)


    while(1):
        num = random.randint(0, len(prime_list) - 1)
        q = prime_list[num]
        for i in prime_list[num:]:
            if (i-1)%q==0:
                return i,q



def DSA_Parameter():
    p,q = random_prime(40, 200)
    while 1:
        h = random.randint(2,p-2)
        g= Lib.mns(h,int((p-1)/q),p)
        if g != 1:
            break
    return p,q,g


if __name__ == "__main__":
    p,q,g=DSA_Parameter()
    print('p,q,g = {},{},{}'.format(p,q,g))