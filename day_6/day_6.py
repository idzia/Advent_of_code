"""
How many redistribution cycles must be completed, to repeat the value
For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. 
The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing 
to the first bank, the second bank, and so on, the 7 blocks are spread 
out over the memory banks. The fourth, first, and second banks get 
two blocks each, and the third bank gets one back. 
The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). 
Because there are four memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, 
both of which have three blocks. The first bank wins the tie, 
and its three blocks are distributed evenly over the other three banks, 
leaving it with none: 0 2 3 4. The fourth bank is chosen, and its four blocks 
are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2.
So an answer in this example is 5.
"""
with open("day6.txt") as file:
    row = file.readlines()
    row = list(map(str.strip, row))
    row = row[0].split("\t")
row = list(map(int, row))

list_of_str = []
steps = 0
condition = 1
while condition == 1:
    
    max_value = max(row)
    index = row.index(max_value)
    row[index] = 0
    
    for i in range(0, max_value):
        index += 1
        
        if index == len(row):
            index = 0
        row[index] += 1
    str_to_add = "".join(list(map(str, row)))
    steps += 1 
            
    if (str_to_add in list_of_str):
        condition = 0
    
    list_of_str.append(str_to_add)  

print(steps)  