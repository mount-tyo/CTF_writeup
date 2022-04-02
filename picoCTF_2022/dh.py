def createDHSecret():
	"""
	DH秘密鍵を計算する関数
	"""
	p = 13
	# g = 5
	x = 5
	a = 7
	b = 3
	
	E = x ** a % p
	F = x ** b % p
	Ga = F ** a % p
	Gb = E ** b % p
	print(f"Ga = {Ga}")
	print(f"Gb = {Gb}")
	if Ga == Gb:
		return Ga
	else:
		print("no matching")
		exit()
	
	
def decryptMessage(ciphertext, shift):
	"""
	AliceとBobの暗号メッセージを解読する関数
	
	ciphertext (str) : 暗号文
	shift          (int) : シフト量
	"""
	alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabet = list(alphabet)
	number = "あ"
	number = list(number)
	cipher_list = list(ciphertext)
	
	for chara in cipher_list:
		if chara in alphabet:
			id = alphabet.index(chara) + shift
			if id >= len(alphabet): 
				id = id - len(alphabet)
			if id < 0:
				id = len(alphabet) + id
			print(alphabet[id], end="")
		elif chara == "_":
			print("_", end="")
		else:
			id = number.index(chara) + shift
			if id >= len(number): 
				id = id - len(number)
			if id < 0:
				id = len(number) + id
			print(number[id], end="")	
	
	
if __name__ == "__main__":
	shift = createDHSecret()
	decryptMessage("H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_DI9D987F", -shift)
	