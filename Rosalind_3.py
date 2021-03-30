input1 = open('input_1.txt', 'r')

i = 1
for line in input1:
    if i % 2 == 0:
        print(line)
    i = i+1
