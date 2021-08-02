import Lib


def line_change(list,a,b):
    list[a],list[b]=list[b],list[a]

def find_addition_inverse(num1,num2,p):
    for i in range(0,p):
        sub_num = num1*i
        if (sub_num + num2)%p ==0:
            return i

def addi_operation(list,a,b,num,p):
    sub_num = 0
    for i in range(len(list[a])):
        sub_num = list[a][i]*num
        list[b][i] = (list[b][i]+sub_num)%p

def line_multi(list,i,num,p):
    if num == 0:
        return
    for i in range(len(list[i])):
        list[i] = (list[i]*num)%p

def Gauss_Jordan(list,p):
    size = len(list)

    if list[0][0] == 0:
        for i in range(size):
            if list[i][0] != 0:
                break
        line_change(list,0,i)
    for i in range(0,size):
        for j in range(i+1,size):
            num = find_addition_inverse(list[i][i],list[j][i],p)
            addi_operation(list,i,j,num,p)

        inverse_num = Lib.inverse(list[i+1][i+1],p)
        line_multi(list,i+1,inverse_num,p)


    for i in range(0,size):
        for j in range(i,size):
            num = find_addition_inverse(list[size-1][size-1-i],list[size-1-j][size-1-i],p)
            addi_operation(list,size-1-i,size-2-i)

    final_list = []
    for i in list:
        final_list.append(i[size])
    return final_list






