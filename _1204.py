''' filepath="inputs/input_1204.txt"
make sure to add blank lines to end of input file
or else answer returned will be 1 off correct answer'''

def answer1(filepath="inputs/input_1204.txt"):
	answer = 0
	count = 0
	refs = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
	with open(filepath, 'r') as input_file:
		for line in input_file:
			if line == '\n':
				if count == len(refs):
					answer += 1
				count = 0
			else:
				for ref in refs:
					if ref in line:
						count += 1
	return answer

def answer2(filepath="inputs/input_1204.txt"):
	answer = 0
	count = 0
	with open(filepath, 'r') as input_file:
		for line in input_file:
			if line == '\n':
				if count == 7:
					answer += 1
				count = 0
			else:
				line = line.strip()
				line = line.split(' ')
				line = ':'.join(line)
				line = line.split(':')
				for i in range(len(line)):
					if line[i] == 'byr':
						if int(line[i+1]) >= 1920 and int(line[i+1]) <= 2002:
							count += 1
					elif line[i] == 'iyr':
						if int(line[i+1]) >= 2010 and int(line[i+1]) <= 2020:
							count += 1
					elif line[i] == 'eyr':
						if int(line[i+1]) >= 2020 and int(line[i+1]) <= 2030:
							count += 1
					elif line[i] == 'hgt':
						if line[i+1][-2:] == 'cm':
							if int(line[i+1][:-2]) >= 150 and int(line[i+1][:-2]) <= 193:
								count += 1
						elif line[i+1][-2:] == 'in':
							if int(line[i+1][:-2]) >= 59 and int(line[i+1][:-2]) <= 76:
								count += 1
					elif line[i] == 'hcl':
						if line[i+1][0] == '#' and line[i+1][1:].isalnum():
							count += 1
					elif line[i] == 'ecl':
						if line[i+1] in 'amb blu brn gry grn hzl oth':
							count += 1
					elif line[i] == 'pid':
						if line[i+1].isnumeric and len(line[i+1]) == 9:
							count+=1
	return answer

if __name__ == "__main__":
	print("Answer 1:", answer1())
	print()
	print("Answer 2:", answer2())
	print()
	print("Merry Christmas!")
