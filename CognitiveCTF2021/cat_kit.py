with open('./kitters.jpg', 'rb') as f:
  kitters = f.read()

with open('./cattos.jpg', 'rb') as f:
  cattos = f.read()

flag = ''
for i in range(min(len(kitters), len(cattos))):
  if kitters[i] != cattos[i]:
    flag += chr(cattos[i])
print(flag)
