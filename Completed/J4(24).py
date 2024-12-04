word = input()
sticky = input()
silly = "-"
og = "-"
quiet = "-"
silent = True
first = False

if len(word) != len(sticky):
    silent = False

if silent: #3 points
    for i in range(len(word)):
        if word[i] != sticky[i]:
            silly = sticky[i]
            og = word[i]
            break

else: #6 points

    for i in range(len(sticky)):
        if word[i] != sticky[i]:
            silly = sticky[i]
            og = word[i]
            break
    if silly in word: #Looks for if quiet or silly is first, returns true if quiet is first
        first = True
    else:
        for char in word:
            if char not in sticky:
                quiet = char
    if first: #quiet is first 
        for char in word:
            if char not in sticky:
                quiet = char
                break
        for char in sticky:
            if char not in word:
                silly = char 
        test = list(word)
        test.remove(quiet)
        for char in word:
            if char not in sticky:
                og = char

print(og, silly)
print(quiet)