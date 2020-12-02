# filepath = 'input_1202.txt'

# Answer 1
def answer1(filepath):
	answer = 0
	with open(filepath, 'r') as input_file:
		for line in input_file:
			cons, char, password = line.split(' ')
			count = password.count(char[0])
			cons = cons.split('-')
			if count >= int(cons[0]) and count <= int(cons[1]):
				answer += 1
	return answer

# Answer 2
def answer2(filepath):
	answer = 0
	with open(filepath, 'r') as input_file:
		for line in input_file:
			indices, char, password = line.split(' ')
			a, b = indices.split('-')
			if (password[int(a)-1] == char[0]) ^ (password[int(b)-1] == char[0]):
				answer += 1
	return answer
