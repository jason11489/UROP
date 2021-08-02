import Lib
import Miller_Rabin
import random
import DSA_Parameter
import quick
import Gauss_Jordan


def Index_Calculus(p,q,g,h):   # q|(p-1) ( p,q : prime ), H = <g> , | H | = q , find x s.t. g^x = h
    cost = 5
    S = []
    equation_list = []
    for i in range(cost):
        equation_list.append([0 for i in range(cost+1)])
    S.append(2)
    S.append(3)
    S.append(5)
    for i in range(cost-3):
        while 1:
            prime = Miller_Rabin.Probably_Prime(2,p-1)
            if prime not in S:
                S.append(prime)
                break

    quick.quick_sort(S,0,len(S)-1)
    cnt = 0
    k = 0
    list_k = []
    while cnt<cost:

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



if __name__ == "__main__":
    #p,q,g = DSA_Parameter.DSA_Parameter(40,200)
    p,q,g = 83,41,10
    x = random.randint(2,q)
    h = Lib.mns(g,x,p)

    Index_Calculus(p,q,g,h)


