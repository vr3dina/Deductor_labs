import random

file = open("examples.txt","w+")
file.write('x y flag\n')
for i in range(0, 1000):
    x = random.uniform(0.0, 5.0)
    y = random.uniform(0.0, 5.0)
    f = (1 <= x <= 4 and 0 <= y <= 5) and not(2 < x < 3 and 1 < y < 4)
    file.write(f'{x} {y} {f}\n')

file.close()