__author__ = 'gongzhi'
'''
url = http://www.pythonchallenge.com/pc/def/ocr.html
view source and save the mess string in a txt file.
'''

data = {}
import sys


def char_count(input_string):
	for i in range(len(input_string)):
		char = input_string[i]

		if (data.has_key(char) == False):
			data[char] = 1
		else:
			data[char] += 1


def get_smallest_count():
	small_value = sys.maxint
	for i in dict(data).values():
		if small_value > i:
			small_value = i
	return small_value


def get_smallest_list(small_value):
	res = []
	for (k, v) in dict(data).items():
		if v == small_value:
			res += k
	return res


if __name__ == "__main__":
	print "question 3"

	mess = open("3.txt").read()
	char_count(mess)

	res = get_smallest_list(get_smallest_count())

	ret = ''
	for i in range(len(mess)):
		if mess[i] in res:
			ret += mess[i]

	print ret



