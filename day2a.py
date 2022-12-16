import re
import sys

pws = []

def good_pw(pw):
    #print(pw)
    return ((pw[3][pw[0]-1] == pw[2]) ^ (pw[3][pw[1]-1] == pw[2]))
#    cnt = pw[3].count(pw[2])
#    return((cnt >= pw[0]) and (cnt <= pw[1]))


with open('day2_input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^(.*)-(.*) (.*): (.*)", line.strip())
        if match:
            pws.append((int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)))
        else:
            "BAD"
            sys.exit()


print(pws)
result = list(filter(good_pw, pws))
print(result)
print(f"Valid passwords found: {len(result)}")
