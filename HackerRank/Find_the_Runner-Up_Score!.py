if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    lenth = max(array)
    count = 0
    for i in range(count, n):
        if n > count:
            if lenth == max(array):
                array.remove(max(array))
            count+=1
    print(max(array))