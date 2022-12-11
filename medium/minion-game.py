'''
Difficulty: Medium
'''
def minion_game(string):
    
    scount = 0
    
    kcount = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(string)):
        if (string[i] in vowel):
            kcount += len(string) - i 
        else:
            scount += len(string) - i
            
    if scount > kcount: 
        print("Stuart",scount)
    elif kcount > scount:
        print("Kevin",kcount)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
