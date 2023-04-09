
vowels = set('aeiouAEIOU')
num_vowels = 0
num_consonants = 0

with open("data01.txt",'r') as file:
    for line in file:
        for word in line:
            if word.isalpha():
                if word in vowels:
                    num_vowels+=1
                else:
                    num_consonants+=1

print('Number of vowels:', num_vowels)
print('Number of consonants:', num_consonants)
