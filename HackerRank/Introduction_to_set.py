def average(array):
    heights = set(array)
    avg = sum(heights) / len(heights)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)