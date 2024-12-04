word = list(input())
vowels = list("aeiou")
def vowel_check(x,y):
    for _ in range(26):
        x += 1
        let = chr(x)
        if let == vowels:
            return x
        else:
            let = ord(x)
        y -= 1
        lett = chr(y)
        if lett == vowels:
            return y
        else:
            lett = ord(y)
        
        

for i in range(len(word)):
    for j in range(26):
        if word[i] != vowels:
            x = ord(word[i])
            y = ord(word[i])
            vowel = vowel_check(x,y)
print(vowel)
