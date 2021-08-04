import Lib
import Miller_Rabin
import random
import DSA_Parameter
import quick
import Gauss_Jordan


def Index_Calculus(p,q,g,h):   # q|(p-1) ( p,q : prime ), H = <g> , | H | = q , find x s.t. g^x = h
    cost = 8
    total = 8
    equation_list = []
    for i in range(total):
        equation_list.append([0 for i in range(cost+1)])

    S = [2,3,5,7,11]
    for i in range(total-5):
        while 1:
            prime = Miller_Rabin.Probably_Prime(2,p-1)
            if prime not in S:
                S.append(prime)
                break
    quick.quick_sort(S,0,len(S)-1)

    print("(Step 1) \nS = {}\n".format(S))
    print('(Step 2,3) ')
    cnt = 0
    k = 0
    list_k = []
    while cnt<total:
        while 1:
            while 1:
                k = random.randint(1,q-1)
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

        print("k = {} , g^k = {} = ".format(k,g_k),end="")
        for i in g_k_factor:
            print("{}^{} ".format(i[0],i[1]),end="")
        print()

        cnt += 1

    print("\n(Step 4,5) ")
    for i in equation_list:
        print("{} = {}*X(0) + {}*X(1) + {}*X(2) + {}*X(3) + {}*X(4)"
              "+ {}*X(5) + {}*X(6) + {}*X(7)".format(i[8],i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    #Step6

    X_sol = Gauss_Jordan.Gauss_Jordan(equation_list,q)
    print("\n(Step 6)")
    for i in range(len(S)):
        print("X({}) = {}".format(i,X_sol[i]))

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
    print("\n(Step 7,8)")
    print("k = {} , hg^k = {} = ".format(random_k,h_g_k),end="")

    h_g_k_factor = Lib.factor(h_g_k)

    for i in h_g_k_factor:
        print("{}^{} ".format(i[0], i[1]), end="")

    final_x = 0
    for i in h_g_k_factor:
        num_S = S.index(i[0])
        X_j = X_sol[num_S]
        final_x = final_x + X_j*i[1]

    final_x = final_x - random_k
    if final_x<0:
        final_x += q

    print("\n\n(Step 9) \nx = {}".format(final_x))

    return final_x%q




if __name__ == "__main__":

    p,q,g = DSA_Parameter.DSA_Parameter(100,1000)
    x = random.randint(2,q-1)
    h = Lib.mns(g,x,p)
    '''
    p,q,g = 2447,1223,25
    x = 9999
    h = 811
    '''
    print("GF({}) , G = <{}> , |G| = {} , {}^{} = {}".format(p,g,q,g,x,h))
    print("=======================\nIndex-Calculus Algorithm\n=======================")

    final_x = Index_Calculus(p,q,g,h)
    print("\nreal x = {}\nsol x = {}".format(x,final_x))








