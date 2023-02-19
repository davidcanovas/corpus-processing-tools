lines_per_file = 1000000
div = None
with open('sourcefile.txt', encoding="utf-8") as sencer:
    for lineno, line in enumerate(sencer):
        if lineno % lines_per_file == 0:
            if div:
                div.close()
            divfiles = 'div{}.txt'.format(lineno + lines_per_file)
            div = open(divfiles, "w", encoding="utf-8")
        div.write(line)
    if div:
        div.close()