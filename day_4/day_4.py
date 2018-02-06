"""
How many passphrases are valid?
passphrase must contain no duplicate words.

For example:
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
"""
with open("day4.txt") as file:
    passphrases = file.readlines()
    passphrases = list(map(str.strip, passphrases))
    
    for i in range(len(passphrases)):
        passphrases[i] = passphrases[i].split(" ")

passed = 0
for i in range(len(passphrases)):
    check_list = []

    for j in range(len(passphrases[i])-1):

        for k in range((j+1), len(passphrases[i])):
            
            if passphrases[i][j] == passphrases[i][k]:
                check_list.append("1")

    if len(check_list) == 0:
        passed += 1

print(passed)
