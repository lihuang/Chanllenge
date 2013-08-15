__author__ = 'gongzhi'
'''
url = http://www.pythonchallenge.com/pc/def/map.html
'''

def translate(org):
	res = ""
	for i in range(len(org)):

		if(org[i] == " "):
			res += org[i]
		elif(org[i] == "."):
			res += org[i]
		elif(org[i] == "'"):
			res += org[i]
		elif(org[i] == "("):
			res += org[i]
		elif(org[i] == ")"):
			res += org[i]
		elif(org[i] == "y"):
			res += "a"
		elif(org[i] == "z"):
			res += "b"
		else:
			int_a = ord(org[i])
			res += chr(int_a + 2)

	return res

if __name__ == "__main__":
	print 'Question 2'
	org = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	print translate(org)

	url = "map"
	print translate(url)
