import random
compt = 1
sample_file = 'sample_200.txt'
sample = open(sample_file, "w", encoding="utf-8")

with open('sourcefile.txt', encoding="utf-8") as es:
    lines = es.read().splitlines()
    for compt in range(200):
        idx = random.randint(0,len(lines))
        line = lines[idx]
        sample.write(line + '\n')