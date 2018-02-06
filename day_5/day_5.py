"""
Positive jumps ("forward") move downward; 
negative jumps move upward. 
The following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
In this example, the exit is reached in 5 steps.
"""
with open("day5.txt") as file:
    list_ = file.readlines()
    list_ = list(map(str.strip, list_))

list_ = list(map(int, list_))

index = 0
steps = 0
while True:

    if index >= len(list_):
        break
    else:
        value = list_[index]
        list_[index] += 1
        index += value
        steps += 1

print(steps)