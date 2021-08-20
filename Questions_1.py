mac = "EC:B0:8T:E4"
mapper = {
"E": 0,
"T": 0
}

final_string = []


for i in mac:
    if i in mapper:
        final_string.append(mapper[i])
    else:
        final_string.append(i)

print("".join([str(x) for x in final_string]))








