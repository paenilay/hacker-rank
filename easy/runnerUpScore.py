'''


Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max = arr[0]
    runner = -100

    if (n >= 2 and n <= 10):
    
        for i in range (1,n):
        
            if (arr[i] >= -100 and arr[i] <= 100):
                if arr[i] > max:
                    max = arr[i]
                    
            i += 1
        for i in range (0,n):
        
            if (arr[i] >= -100 and arr[i] <= 100):
                if arr[i] < max and arr[i] > runner:
                    runner = arr[i]
                     
            i += 1
        print(runner)
