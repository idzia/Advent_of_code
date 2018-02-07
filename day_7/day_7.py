"""
What is the name of the bottom program?

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

"tknk" is at the bottom of the tower (the bottom program),
and is holding up ugml, padx, and fwft. 
Those programs are, in turn, holding up other programs; in this example, 
none of those programs are holding up any other programs, 
and are all the tops of their own towers.
"""

with open("day7.txt") as file:
    content = file.readlines()
    content = list(map(str.strip, content))
    
    for i in range(len(content)):
        content[i] = content[i].split(" -> ")

all_programs = []
programs_in_other = []

for i in range(len(content)):
    all_programs.append(content[i][0])
    
    if len(content[i]) == 2:
        programs_in_other.append(content[i][1])

for i in range(len(all_programs)):
    all_programs[i] = all_programs[i].split(" ")[0]

programs_in_other = ", ".join(programs_in_other)
programs_in_other = programs_in_other.split(", ")

all_programs = set(all_programs)
programs_in_other = set(programs_in_other)

bottom_program = all_programs.difference(programs_in_other)

print(bottom_program)