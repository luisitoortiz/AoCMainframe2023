import re
total_sum = 0
with open('advent1.txt', 'r') as file:
    for line in file:
        line = line.replace("one","o1e")
        line = line.replace("two","t2o")
        line = line.replace("three","t3e")
        line = line.replace("four","f4r")
        line = line.replace("five","f5e")
        line = line.replace("six","s6x")
        line = line.replace("seven","s7n")
        line = line.replace("eight","e8t")
        line = line.replace("nine","n9e")
        linenumber = int((lambda match: match.group(1) if match else 0)(re.search(r'^.*(\d)', line)))
        linenumber += int((lambda match: match.group(1) if match else 0)(re.search(r'^\D*(\d)', line))) *10
        total_sum += linenumber
print(total_sum)
