
def count_substring(string, sub_string):
    lenth_m = len(string)
    lenth_n = len(string)
    c = 0
    for i in range(lenth_m-lenth_n):
        if(string[i:(i+lenth_n)]== sub_string ):
            c += 1


    return string.find(sub_string)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
