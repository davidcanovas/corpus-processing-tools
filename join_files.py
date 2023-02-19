def merge_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f1.read())
        outfile.write(f2.read())

merge_files('file1.txt', 'file2.txt', 'joinedfile.txt')