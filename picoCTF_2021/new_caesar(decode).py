import string

LOWERCASE_OFFSET = ord("a")
# ALPHABET = string.ascii_lowercase[:16]
ALPHABET = string.ascii_lowercase[:16]
# print('ALPHA : {}'.format(ALPHABET))


def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		# print('binary:{}'.format(binary))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
		# print('enc:{}'.format(enc))
	return enc

def b16_decode(code):
	dec = ''
	for i in range(0, len(code), 2):
		# print('i={}:'.format(i))
		left = ALPHABET.find(code[i])
		right = ALPHABET.find(code[i+1])
		# print('    left={}, rigth={}'.format(left, right))
		left_bin = '{0:04b}'.format(int(left))
		right_bin = '{0:04b}'.format(int(right))
		# print('    left={}, rigth={}'.format(left_bin, right_bin))
		char_bin = left_bin + right_bin
		# print('    char_bin={}'.format(char_bin))
		char_int = int(char_bin, 2)
		# print('    char_int={}'.format(char_int))
		# print('    chr()={}'.format(chr(char_int)))
		dec += chr(char_int)
		# print('dec={}'.format(dec))
	return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	# print('  t2 = {}'.format(t2))
	# print('  t1={}, t2={}, index={}'.format(t1,t2,(t1 + t2) % len(ALPHABET)))
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def rev_shift(c, k):
	fbin = 0							# t1 + t2 < 16
	t2 = ord(k) - LOWERCASE_OFFSET
	index = ALPHABET.find(c)
	if t2 > index:
		fbin = 1
	t1 = fbin * len(ALPHABET) + index - t2
	
	# print('  t1={}, t2={}, index={}'.format(t1,t2,(t1 + t2) % len(ALPHABET)))
	asc_code = t1 + LOWERCASE_OFFSET
	char = chr(asc_code)

	return char



# flag = "redacted"
# key = "redacted"
# flag = 'apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna'
# key = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

'''
# ENCODE
b16 = b16_encode(flag)
print('flag = {}'.format(flag))
print('b16 = {}'.format(b16))
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print('encode = {}'.format(enc))

'''

# keys に {a ~ p}　までのkeyを配置
keys = []
for i in range(16):
	keys.append(chr(ord('a') + i))

for key in keys:
	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	enc = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

	# DECODE
	# 1st, reverse shift
	dec = ''
	for i, c in enumerate(enc):
		dec += rev_shift(c, key[i%len(key)])
	# print('rev_shift = {}'.format(dec))
	# 2nd, b16 => b26
	plain = b16_decode(dec)
	print('{} : {}'.format(key, plain))





