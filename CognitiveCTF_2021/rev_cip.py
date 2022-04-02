flag = "CognitiveCTF{p8t8px1=c80ga7c}"
a = ""

for i in range(13, len(flag)-1, 1):
    if (i & 1) == 0:
        a += chr(ord(flag[i]) - 5)
    else:
        a += chr(ord(flag[i]) + 2)

print(a)