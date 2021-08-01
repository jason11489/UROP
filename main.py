import HASH as H



def Small_space():
    start = 'appleappleappleapple'
    x = [start, start]
    while True:
        print('.',end='')
        x[0], x[1] = H.hash_function(x[0]), H.hash_function(H.hash_function(x[1]))
        if x[0] == x[1]:
            print('find k ( xk = x2k )\n{},{}'.format(x[0],x[1]))
            break
    x[1], x[0] = x[0], start

    while True:
        if H.hash_function(x[0]) == H.hash_function(x[1]):
            return [x[0], x[1]]
        else:
            x[0],x[1]=H.hash_function(x[0]),H.hash_function(x[1])

if __name__ =='__main__':

    Collision = Small_space()
    print('Collision = ({},{}) -> ({},{})'.format(Collision[0],Collision[1],H.hash_function(Collision[0]),H.hash_function(Collision[1])))