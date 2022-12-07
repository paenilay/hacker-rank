def split_and_join(a):
    a = a.split(" ")
    print(a)
    a = tuple(a)
    b = "-".join(a)
    print(b)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#string.join(iterable)