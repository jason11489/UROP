import Lib


def line_change(list,a,b):
    list[a],list[b]=list[b],list[a]

def find_addition_inverse(num1,num2,p):
    for i in range(0,p):
        sub_num = num1*i
        if (sub_num + num2)%p ==0:
            return i
    return 0

def addi_operation(list,a,b,num,p):
    sub_num = 0
    for i in range(len(list[a])):
        sub_num = list[a][i]*num
        list[b][i] = (list[b][i]+sub_num)%p
        sub_num = 0

def line_multi(list,i,num,p):
    for cnt in range(len(list[i])):
        list[i][cnt] = (list[i][cnt]*num)%p


def Gauss_Jordan(list,p):
    cost = 5
    total = 5

    if list[0][0] == 0:
        for i in range(total):
            if list[i][0] != 0:
                break
        line_change(list,0,i)

    for i in range(total):

        if list[i][i] == 0:
            for k in range(i,total):
                if list[k][i] != 0:
                    break
            line_change(list,i,k)

        if list[i][i] != 0:
            inverse_num = Lib.inverse(list[i][i],p)
            line_multi(list,i,inverse_num,p)
            for j in range(i+1,total):
                if list[j][i] != 0:
                    num = find_addition_inverse(list[i][i],list[j][i],p)
                    addi_operation(list,i,j,num,p)




    for i in range(0,total):
        for j in range(i+1,total):
            num = find_addition_inverse(list[4-i][4-i],list[4-j][4-i],p)
            addi_operation(list,4-i,4-j,num,p)

    final_list = []
    for i in list:
        final_list.append(i[cost])
    return final_list



if __name__ == "__main__":
    list = [[2,2,1,0,0,180],[4,0,0,0,1,176],[0,1,1,0,1,165],[1,0,0,1,1,154],[1,2,0,0,1,198],[1,1,1,1,0,210]]
    sol_list = Gauss_Jordan(list,228)
    print(sol_list)


