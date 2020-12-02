# filepath = 'input_1202.txt'

# Answer 1
def answer1(filepath):
	answer = 0
	with open(filepath, 'r') as input_file:
		for line in input_file:
			line = line.split(' ')
			count = line[2].count(line[1][0])
			cons = line[0].split('-')
			if count >= int(cons[0]) and count <= int(cons[1]):
				answer += 1
	return answer

# Answer 2
def answer2(filepath):
	answer = 0
	with open(filepath, 'r') as input_file:
		for line in input_file:
			line = line.split(' ')
			indices = line[0].split('-')
			if line[2][int(indices[0])-1] != line[2][int(indices[1])-1]:
				if line[2][int(indices[0])-1] == line[1][0] or line[2][int(indices[1])-1] == line[1][0]:
					answer += 1
	return answer
