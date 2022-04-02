s = [int(x) for x in input().split()]

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for si in s:
    print(f"{alph[si-1]}", end="")