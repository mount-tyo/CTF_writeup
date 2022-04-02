input_data = [186,249,356,395,303,337,190,393,146,174,446,127,385,400,420,226,76,294,144,90,291,445,137]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)

for num in input_data:
	# 組み込みpow()関数を使用して以下のように、モジュラ逆数を計算できる。
	id = pow(num, 41-2, 41)
	if 1 <= id and id <= 26:
		print(alphabet[id-1], end="")
	elif id <= 36:
		print(id - 27, end="")
	elif id == 37:
		print("_", end="")
	else:
		exit()