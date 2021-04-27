# code to take an input of binary and fli at a certain index
thelist = [0]*64



def flip(List, Index):
    if List[Index] == 0:
        List[Index] = 1
    elif List[Index] == 1:
        List[Index] = 0
    else:
        print('error')
    return List

Index = int(input('enter bit to flip'))
print(flip(thelist, Index))
