import re
total_sum = 0
with open('advent1.txt', 'r') as file:
    for line in file:
        line = line.replace("one","one1one")
        line = line.replace("two","two2two")
        line = line.replace("three","three3three")
        line = line.replace("four","four4four")
        line = line.replace("five","five5five")
        line = line.replace("six","six6six")
        line = line.replace("seven","seven7seven")
        line = line.replace("eight","eight8eight")
        line = line.replace("nine","nine9nine")
        linenumber = int((lambda match: match.group(1) if match else 0)(re.search(r'^.*(\d)', line)))
        linenumber += int((lambda match: match.group(1) if match else 0)(re.search(r'^\D*(\d)', line))) *10
        total_sum += linenumber
print(total_sum)
