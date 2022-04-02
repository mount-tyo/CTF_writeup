flag = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B"
b1 = flag[:18]
b2 = flag[18:36]
b3 = flag[36:]
a = [2,0,1,5,3,4,8,6,7,11,9,10,14,12,13,17,15,16]

for ai in a:
	print(b1[ai], end="")
for ai in a:
	print(b2[ai], end="")
for ai in a:
	print(b3[ai], end="")