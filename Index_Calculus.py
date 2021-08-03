import Lib
import Miller_Rabin
import random
import DSA_Parameter
import quick
import Gauss_Jordan


def Index_Calculus(p,q,g,h):   # q|(p-1) ( p,q : prime ), H = <g> , | H | = q , find x s.t. g^x = h
    cost = 5
    total = 5
    S = []
    equation_list = []
    for i in range(total):
        equation_list.append([0 for i in range(cost+1)])
    S.append(2)
    S.append(3)
    S.append(5)
    for i in range(total-3):
        while 1:
            prime = Miller_Rabin.Probably_Prime(2,p-1)
            if prime not in S:
                S.append(prime)
                break

    quick.quick_sort(S,0,len(S)-1)
    cnt = 0
    k = 0
    list_k = []
    while cnt<total:

        while 1:
            while 1:
                k = random.randint(1,q-1)
                print(".",end="")
                if k not in list_k:
                    list_k.append(k)
                    break
            g_k = Lib.mns(g,k,p)
            divisor_g_k = Lib.divisor(g_k)
            num_divisor = 0
            for i in divisor_g_k:
                if i in S:
                    num_divisor += 1

            if num_divisor == len(divisor_g_k):
                break


        g_k_factor = Lib.factor(g_k)
        for i in g_k_factor:
            num_S = S.index(i[0])
            equation_list[cnt][num_S]=i[1]
        equation_list[cnt][cost] = k

        cnt += 1

    #Step6
    print(1)
    X_sol = Gauss_Jordan.Gauss_Jordan(equation_list,q)

    while 1:
        random_k = random.randint(2,q-1)
        h_g_k = (h*Lib.mns(g,random_k,p))%p

        divisor_h_g_k = Lib.divisor(h_g_k)
        num_divisor = 0
        for i in divisor_h_g_k:
            if i in S:
                num_divisor += 1

        if num_divisor == len(divisor_h_g_k):
            break
    h_g_k_factor = Lib.factor(h_g_k)
    final_x = 0
    for i in h_g_k_factor:
        num_S = S.index(i[0])
        X_j = X_sol[num_S]
        final_x = final_x + X_j*i[1]

    final_x = final_x - random_k
    if final_x<0:
        final_x += q
    return final_x



if __name__ == "__main__":
    p,q,g = DSA_Parameter.DSA_Parameter(10,600)
    x = random.randint(2,q-1)
    h = Lib.mns(g,x,p)

    final_x = Index_Calculus(p,q,g,h)
    print("real x = {}\nsol x = {}".format(x,final_x))


