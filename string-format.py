def print_formatted(number):
    if number >= 1 or number <= 99:
        x = len(format(number, 'b'))
        for i in range(1,n+1):
            print(
            format(i).rjust(x),  # number
            format(i, 'o').rjust(x),  # octal 
            format(i, 'X').rjust(x),  # hex
            format(i, 'b').rjust(x)   # binary
            )
            
            
            
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)