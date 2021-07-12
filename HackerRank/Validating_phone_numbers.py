import re
phone_number = int(input())
for i in range(phone_number):
    recent_number = input().strip()
    if len(re.findall(r'^[7-9]\d{9}$', recent_number)) != 0:
        print("YES")
    else:
        print("NO")