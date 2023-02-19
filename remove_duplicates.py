def write_unique_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        unique_lines = set(lines)
        with open("cleanfile.txt", "w", encoding="utf-8") as outfile:
            for line in unique_lines:
                outfile.write(line)
        return len(lines) - len(unique_lines)

file_path = "sourcefile.txt"
duplicate_lines = write_unique_lines(file_path)
print("Duplicate lines:", duplicate_lines, end=".")