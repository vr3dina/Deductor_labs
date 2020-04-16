n = 11
file = open("lines.txt","w+")
file.write("1 2 3 4 5 6 7 8 9 10 11 flag\n")
for i in range(0, 2**n):
    line = '{0:011b}'.format(i)
    line += '1' if (line.count('1') > 5) else '0'
    file.write(" ".join(line) + '\n')