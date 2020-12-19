#!/usr/bin/env python3

# Just being real honest here. The recursive solution in b_old.py returns the right answer,
# but for the input set it would have run FOREVER and my memoization storage wouldn't have fit in memory.
#
# So that's a fail right there.
#
# As I was on the verge of giving up on AoC 2020 entirely, I decided to just google answers in Python so I
# could at least study and learn from them. Not sure why ilopez told me the final answer was over 3 million -
# more like 518 TRILLION. Same difference, I guess.
#
# Found this at https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
#

with open("input.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in fp.readlines()]

one_jolt = 0
two_jolt = 0
three_jolt = 0 
outlet_rating = 0
lines.append(max(lines)+3) # because max jolt is added


while True:
    #print(1 in lines)
    if (outlet_rating + 1) in lines:
        one_jolt+=1
        outlet_rating += 1
    elif outlet_rating+2 in lines:
        two_jolt+=1
    elif (outlet_rating + 3) in lines:
        three_jolt += 1
        outlet_rating+=3
    else:
        break
print("Part 1 answer is ", one_jolt*three_jolt)

print(sorted(lines))
sol = {0:1}
for line in sorted(lines):
    sol[line] = 0
    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
        sol[line]+=sol[line-3]
    print(sol[line])

print(sol[max(lines)])