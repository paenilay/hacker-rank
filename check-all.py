from curses.ascii import isalnum


'''
Task

You are given a string .
Your task is to find out if the string  contains:
 alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
'''
if __name__ == '__main__':
    s = input()
    print(len(s))
    if len(s) > 0 or len(s) < 1000:
        print(any(s.isalnum() for s in s))
        print(any(s.isalpha() for s in s))
        print(any(s.isdigit() for s in s))
        print(any(s.islower() for s in s))
        print(any(s.isupper() for s in s))
    else:
        print("False")