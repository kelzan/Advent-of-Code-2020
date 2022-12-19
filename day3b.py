import numpy as np
import sys
from functools import reduce


structure = []

def find_trees(xoff, yoff):
    global map
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

    print(f"For slope right {xoff}, down {yoff}, trees is {treecnt}")
    return(treecnt)


myfile = open('day3_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

#print_map()
gridy = len(lines)
gridx = len(lines[0].strip())

# Initialize map
map = np.full(((gridy,gridx)),".",dtype=str)

# Populate map
y = 0
x = 0
print(map.shape)
for row in lines:
    x = 0
    for col in row.strip():
        map[y,x] = col
        x += 1
    y += 1

#print(map)

slopevals = []
slopevals.append(find_trees(1,1))
slopevals.append(find_trees(3,1))
slopevals.append(find_trees(5,1))
slopevals.append(find_trees(7,1))
slopevals.append(find_trees(1,2))

#product = np.prod(slopevals)
#print(product)
product = reduce((lambda x, y: x * y), slopevals)

print(map)
print(f"Tree Count: {product}")
