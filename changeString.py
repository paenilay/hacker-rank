from numpy import character


'''
input: abcdefghi
task: position 3, character y
output: abydefgh
'''
def mutate_string(string, position, character):
    result = list(string)
    result[position] = character
    result = tuple(result)
    myResult = ''.join(result)
    return myResult

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)