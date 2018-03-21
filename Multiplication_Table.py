# First interval, that is header's column:
a = int(input())
b = int(input())

# Second interval, that is header's row:
c = int(input())
d = int(input())

# Creating the empty cell 0/0 and not allowing to move to the next line by adding end=''
print('\t', end='')

# Creating header's row and separating numbers with '\t'
for i in range(c, d):
    print(i, end='\t')

# Sowing the last number in the interval [c, d]
print(d)

# Creating the header's column
for i in range(a, b + 1):
    print(i, end='')  # Creating first cell in the row and not allowing to move to the next line by adding end=''
    print('\t', end='')  # Separating numbers with '\t' and not allowing to move to the next line by adding end=''
    # Creating results of multiplication in the current line
    for j in range(c, d + 1):
        print(i * j, end='\t')  # Separating results with the '\t'
    print()  # Moving to the next line