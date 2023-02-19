# corpus-processing-tools
Multiple Python scripts to process and clean corpora.

## join_files.py
This script merges multiple files into one.

## random_extract.py
This script extracts a number of random lines from a text. In this script, the number is 200.

## split_file.py
This script splits a file into smalle ones. In this script, each new file will contain 1000000 lines.

## cleaner.py
This scripts removes lines which contain a forbidden word. In this script, the taboo words are "sample" and "example". The script is case sensitive and considers periods as part of the word. Therefore, "sample." will not be flagged.

## frequence_counter.py
This scripts lists the most frequent words in a file. In this script, it lists the 200 most common words, complete with the number of occurrences.

## remove_duplicates.py
This script removes duplicate lines from a file.
