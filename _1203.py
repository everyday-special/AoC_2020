# filepath = 'inputs/input_1203.txt'

# Answer 1
def answer1(filepath, right = 3):
	answer = 0
	counter = 0
	linecount = 0
	pattern = []
	with open(filepath, 'r') as input_file:
		for line in input_file:
			pattern.append(line)
	for line in pattern:
		line = line.strip('\n')
		if line[counter] == '#':
			answer += 1
		counter = (counter + right) % len(line)
	return answer

def answer2(filepath):
	answer = 1
	down2 = 0
	for i in [1,3,5,7]:
		answer *= answer1(filepath, i)
	counter = 0
	linecount = 0
	pattern = []
	with open(filepath, 'r') as input_file:
		for line in input_file:
			pattern.append(line)
	for line in pattern:
		if linecount % 2 == 0:
			line = line.strip('\n')
			if line[counter] == '#':
				down2 += 1
			counter = (counter + 1) % len(line)
		linecount += 1
	return answer * down2

