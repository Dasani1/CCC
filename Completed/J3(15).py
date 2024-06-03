word = input()
vowels = ["a","e","i","o","u"]
vowels_2 = [97, 101, 105, 111, 117]
final_word = []
def vowel_finder(send_it):
    x = send_it
    y = send_it
    counter = 0
    for i in range(7):
        x += 1
        y -= 1
        counter += 2

        if y in vowels_2:
            send_it = y
            break
        elif x in vowels_2:
            send_it = x
            break
    send_it = chr(send_it)
    return send_it

for i in range(len(word)):
    if word[i] in vowels:
        final_word.append(word[i])  
    elif word[i] not in vowels:
        final_word.append(word[i])
        send_it = ord(word[i])
        send_it = vowel_finder(send_it)
        final_word.append(send_it)
        j = ord(word[i])+1
        if j not in vowels_2:
            if j == 123:
                final_word.append("z")
            else:
                final_word.append(chr(j))
        elif j in vowels_2:
            j += 1
            final_word.append(chr(j))
print(*final_word,sep="")

