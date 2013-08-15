__author__ = 'gongzhi'
'''
url = http://www.pythonchallenge.com/pc/def/equality.html
'''


if __name__ == "__main__":
	print "Question 4"

	mess = open("4.txt").read()
	binary_mess = ""

	for i in range(len(mess)):
		if mess[i].isupper():
			binary_mess += "1"
		elif mess[i].islower():
			binary_mess += "0"
		elif mess[i] == '\n':
			binary_mess += "2"
		else:
			print "ERROR"
	print len(mess)
	print len(binary_mess)

	res = ''
	start = binary_mess.find("011101110")
	while(start != -1):
		res += mess[start + 4]
		start = binary_mess.find("011101110", start + 4)

	print res


