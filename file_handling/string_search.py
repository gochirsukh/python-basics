# Searches a string in a file

file = open("<file>", "r")
term = "<string to search>"

for line in file:
    line.strip().split('/n')
    if term in line:
        print(line)
file.close()



