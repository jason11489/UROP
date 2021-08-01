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

    print(1)
    while(1):
        num = random.randint(int(len(prime_list)/1.5), len(prime_list) - 1)
        q = prime_list[num]
        power = random.randint(2,20)
        for i in prime_list[:num]:
            p_n = Lib.mns(i,power,q)
            if (q-1)%p_n==0:
                break
        h = random.randint(2,q-2)
        g = Lib.mns(h,int(q/p_n),q)
        if g!=1:
            return (i,power,g,q)



 def PPO_Parameter():
    p,power,g,q = random_prime(3, 200)
    x = random.randint(2,Lib.mns_n(p,power)-1)
    h = Lib.mns(g,x,q)
    return p,power,g,h,q,x

if __name__ == "__main__":
    p,n,g,h,q,x=PPO_Parameter()
    print('p,n,g,h,q,x = {},{},{},{},{},{}'.format(p,n,g,h,q,x))