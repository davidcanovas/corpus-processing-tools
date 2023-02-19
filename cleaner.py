file = 'sourcefile.txt'
input_file = open(file, "r", encoding="utf-8")
lines = input_file.readlines()
cleanfile = 'cleanfile.txt'
output_file = open(cleanfile, "w", encoding="utf-8")

for line in lines:
	flag = False
	words = line.split(' ')
	for word in words:
		if(word == 'sample' or word == 'example'):
			flag = True
			break
	if not flag:
		output_file.write(line)
		
	