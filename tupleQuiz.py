if __name__ == '__main__':
    n = int(input())
    input_list = map(int, input().split())
    input_list = [int(x) for x in input_list]

    t = tuple(input_list)
    print(hash(t))