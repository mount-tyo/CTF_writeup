input_data = [128, 63, 242, 87, 151, 147, 50, 369, 239, 248, 205, 346, 299, 73, 335, 189, 105, 293, 37, 214, 333, 137]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)

for num in input_data:
	id = num % 37
	if 0 <= id and id <= 25:
		print(alphabet[id], end="")
	elif id <= 35:
		print(id - 26, end="")
	elif id == 36:
		print("_", end="")
	else:
		exit()