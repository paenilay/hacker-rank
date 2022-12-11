from itertools import permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    '''
    i = 0
    
    myList = []
    

    
    while (i <= x ):
        j = 0
        while (j <= y ):
            k = 0
            while (k <= z ):
                if (i + j + k) != n:
                    perm = permutations([i, j, k])
                    for a in list(perm):
                        b = list(a)
                        if b not in myList:
                            myList.append(b)
                       
                k = k + 1
            j = j + 1
        i = i + 1
   
    #print(myList)
    SortedLists = sorted(myList, key = lambda a: (len(a), a))
    
    print(SortedLists)
    '''
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))