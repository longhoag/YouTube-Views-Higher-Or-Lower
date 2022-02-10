import fileinput

filename = "Testing.rtf"

replacement_text = ''

f1 = open('Testing.rtf', 'r')
f2 = open('result.rtf', 'w')

for line in f1:
    for i in range(1, 301):
        f2.write(line.replace('=' + i, ''))

f1.close()
f2.close()
