import Lib
import Miller_Rabin
import random

def Index_Calculus(p,q,g,h):   # q|(p-1) ( p,q : prime ), H = <g> , | H | = q , find x s.t. g^x = h

    S = []
    equation_list = []
    for i in range(7):
        S.append(Miller_Rabin.Probably_Prime(2,p-1))
    while 1:
        k = random.randint(0,q-1)
        g_k = Lib.mns(g,k,p)
        divisor_g_k = Lib.divisor(g_k)
        num_divisor = 0
        for i in divisor_g_k:
            if i in S:
              num_divisor += 1

        if num_divisor == len(divisor_g_k):
            break


    g_k_factor = Lib.factor(g_k)


