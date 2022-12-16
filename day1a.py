print ("Hello World")
sval = 2020

myfile = open('day1_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

lines = list(map(str.strip,lines))
numlist = list(map(int, lines))

print(numlist)
for i in range(len(numlist)):
    val_needed = sval-numlist[i]
    if (val_needed) in numlist:
        print(f"Found {val_needed}, {numlist[i]} * {val_needed} = {numlist[i]*val_needed}")
