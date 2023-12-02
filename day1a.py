import re
total_sum = 0
with open('advent1.txt','r') as file:
    for line in file:
        linenumber = int((lambda match: match.group(1) if match else 0)(re.search(r'^.*(\d)', line)))
        linenumber += int((lambda match: match.group(1) if match else 0)(re.search(r'^\D*(\d)', line))) *10
        total_sum += linenumber
print(total_sum)
