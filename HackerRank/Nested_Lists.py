Result = {}
for i in range(int(input())):
    name = input()
    grade = input()
    Result[name] = grade
    v = Result.values()
    second = sorted(list(set(v)))
    second_lowest = []
    for key, value in Result.items():
        if value == second:
            second_lowest.append(key)
    second_lowest.sort()
    for name in second_lowest:
        print(name)