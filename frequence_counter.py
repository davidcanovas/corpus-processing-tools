from collections import Counter
  
input_file = 'sourcefile.txt'
data_set = open(input_file, "r", encoding="utf-8")


parts = data_set.read()  
words = parts.split()

word_counter = Counter(words)
  

most_occur = word_counter.most_common(200)

count_file = open("count.txt", "w", encoding="utf-8")

count_file.write(str(most_occur))