"""
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
"""
import math

def get_square_number(digit):

    square_number = 0
    value_from_previous_squer = 1
    a = 0
    while a == 0:      
        
        square_number += 1
        digit_in_square = square_number * 8
        min_value_in_square = value_from_previous_squer + 1
        max_value_in_square = value_from_previous_squer + digit_in_square

        if digit >= min_value_in_square and digit <= max_value_in_square:
            a = 1
        
        value_from_previous_squer = max_value_in_square

    return square_number

digit = input("Please enter a number: ")
digit = int(digit)
square_number = get_square_number(digit)

max_value_in_square = (2 * square_number + 1)**2

number_in_corner4 = max_value_in_square
number_in_corner3 = number_in_corner4 - (2 * square_number)
number_in_corner2 = number_in_corner3 - (2 * square_number)
number_in_corner1 = number_in_corner2 - (2 * square_number)

middle_between_43 = number_in_corner4 - square_number
middle_between_32 = number_in_corner3 - square_number
middle_between_21 = number_in_corner2 - square_number
middle_between_14 = number_in_corner1 - square_number

if digit < number_in_corner4 and digit > number_in_corner3:
    horizont_step = math.fabs(middle_between_43 - digit)

elif digit < number_in_corner3 and digit > number_in_corner2:
    horizont_step = math.fabs(middle_between_32 - digit)

elif digit < number_in_corner2 and digit > number_in_corner1:
    horizont_step = math.fabs(middle_between_21 - digit)

elif digit < number_in_corner1:
    horizont_step = math.fabs(middle_between_14 - digit)

vertical_step = square_number
steps = int(horizont_step + vertical_step)

print(steps)