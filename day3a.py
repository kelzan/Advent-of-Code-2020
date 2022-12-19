import numpy as np
import sys


structure = []

# def print_map():
#     global map
#     #print(map)
#     for row in map:
#         for col in row:
#             print(col,end="")
#         print()
#     print()
#         #print(len(str(row[0])))
#         #print(''.join(str(row)))



myfile = open('day3_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

#print_map()
gridy = len(lines)
gridx = len(lines[0].strip())

map = np.full(((gridy,gridx)),".",dtype=str)

y = 0
x = 0
#print(map.shape)
for row in lines:
#    print(row)
    x = 0
#    print(f"len: {len(row)}")
    for col in row.strip():
        #print(col)
#        print(f"map[{y},{x}]")
        map[y,x] = col
        x += 1
    y += 1

#print(map)

xoff = 3
yoff = 1

xpos = 0
ypos = 0

treecnt = 0

while (ypos < gridy-1):
    xpos += xoff
    ypos += yoff
    if (xpos >= gridx):
        xpos = (xpos - gridx)
    if (map[ypos,xpos] == '#'):
        treecnt += 1


print(map)
print(f"Tree Count: {treecnt}")
