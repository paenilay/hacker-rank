def check_match(str1,str2):
    if len(str1) < 0 or len(str2) < 0:
        return False
    else:
        match = False
        p1=""
        p2 = 0
        for i in range(0,len(str1)-1):
            if (str1[i]==str1[i+1]) and (str2[i]==str2[i+1]):
                print("match")
                p1 += str('0')
            else:
                print(ord(str1[i]))
                print(ord(str1[i+1]))
                print(ord(str2[i]))
                print(ord(str2[i+1]))
                diff1 = abs(ord(str1[i]) - ord(str1[i+1]))
                print("Diff 1", diff1)
                
                diff2 = abs(ord(str2[i]) - ord(str2[i+1]))
                print("Diff 2", diff2)
                if diff1 == diff2:
                    print("OK")
                    p1 += str('1')

                else:
                    p2 = 1
                    break

                
    
        '''
        for i in range(0,len(str2)-1):
            if (str2[i]==str2[i+1]):
                print("match")
                p2 += str('0')
            else:
                p2 += str('1')
        '''

        if p2 == 1: return False
        else: return True

    

result = check_match("abcd","jklm")
print(result)
#p = ""
#print(len(p))