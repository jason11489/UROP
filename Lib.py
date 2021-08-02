import math
import random

def int2list(n):
    out_list = []
    out_list.append( (n >> 24) & 0xff )
    out_list.append( (n >> 16) & 0xff )
    out_list.append( (n >>  8) & 0xff )
    out_list.append( (n      ) & 0xff )

    return out_list
def list2int(l):
    n = 0
    num_byte = len(l)
    for i in range(len(l)):
        n += l[i] << 8 * (num_byte - i - 1)

    return n
def partition(A,low,high,r):
    pivot = A[high][r]
    i = low - 1
    for j in range(low,high):
        if A[j][r]<pivot:
            i += 1
            A[i],A[j]=A[j],A[i]
            #if i!= j:
             #   print(A)
    A[i+1],A[high]=A[high],A[i+1]
    #if i+1 != high:
        #print(A)
    return i+1
def quick_sort(A,low,high,r=0):
    if low<high:
        m = partition(A,low,high,r)
        #print('m = ',m)
        quick_sort(A,low,m-1,r)
        quick_sort(A,m+1,high,r)


if __name__=="__main__":
    A = [[0, 1], [1, 3], [2, 9], [3, 27], [5, 10], [4, 81], [6, 30], [7, 90], [8, 37], [9, 111], [10, 100], [11, 67], [12, 201], [13, 137], [14, 178], [15, 68]]

    print(A)
    quick_sort(A, 0, len(A) - 1,1)
    print(A)
def mns(g, n, M):
    t = [1, g]

    l = len(bin(n)) - 2 # l: bit length
    n = list(map(int, str(bin(n)[2:]))) # n을 이진수로 변환 후 리스트에 저장.

    for j in range(0, l):
        t[1-n[j]] = (t[0] * t[1]) % M
        t[n[j]] = (t[n[j]] ** 2) % M

    return t[0]
def mns_n(g, n):
    t = [1, g]

    l = len(bin(n)) - 2 # l: bit length
    n = list(map(int, str(bin(n)[2:]))) # n을 이진수로 변환 후 리스트에 저장.

    for j in range(0, l):
        t[1-n[j]] = (t[0] * t[1])
        t[n[j]] = (t[n[j]] ** 2)

    return t[0]
def show_list(list):
    cnt = 0
    while cnt<len(list):
        print("{}, ".format(list[cnt]), end = '')
        cnt = cnt + 1
        if cnt%5 == 0:
            print("\n",end = '')
    print("\n")
NO_ELEMENT = 'NO_ELEMENT'
def bin_search(list,target):
    size = len(list)
    if size < 1:
        return NO_ELEMENT
    mid =  (size-1) >> 1
    if list[mid][1] == target:
        return list[mid][0]
    if list[mid][1] < target:
        return bin_search(list[mid+1:],target)
    else:
        return bin_search(list[:mid],target)

def inverse(a,p):
    t0, t1 = a,p
    u0,u1 = 1,0
    while t1 != 0:
        t2,t0 = t0,t1
        q,t1 = t2//t1,t2%t1
        u2,u0 = u0,u1
        u1 = u2-q*u1
    if u0 < 0:
        u0 = u0 + p
    return u0


def random_prime(a,b):
    prime_list = []
    for sub_num in range(a,b+1):
        flag = True
        for n in range(2,int(math.sqrt(sub_num))+1):
            if sub_num % n == 0:
                flag = False

        if flag:
            prime_list.append(sub_num)

    return prime_list[random.randint(0,len(prime_list)-1)]

def order(g,p):
    for i in range(1,p):
        if mns(g,i,p)==1:
            return i

def is_prime(p):
    if p == 2:
        return True
    if p%2 ==0:
        return False
    for i in range(2,int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True


def chinese_remainder(A, M):
    total_M = 1
    for j in M:
        total_M *= j
    x = 0
    for i in range(len(A)):
        sub_M = total_M/M[i]
        sub_a = inverse(sub_M,M[i])
        x += sub_a*sub_M*A[i]
    x = x%total_M
    return x

def factor(N):
    list =[]
    for i in range(2,N+1):
        if is_prime(i):
            sub_num = 0
            sub_N = N
            while 1:
                if sub_N%i != 0:
                    break
                sub_N = int(sub_N/i)
                sub_num+=1
            if N%i ==0:
                list.append((i,sub_num))

    return list

def divisor(N):
    list = []
    for i in range(2, N + 1):
        if is_prime(i):
            sub_N = N
            if N % i == 0:
                list.append(i)

    return list


if __name__=="__main__":
    print("===================")
    print(factor(8100))
    print("===================")
    print(order(6,229))
