count = 0
sentence = input("enter sentence = ")
vowels = ["a","e","i","o","u"]
sentence = list(sentence)
print(sentence)
for letters in sentence:
    if letters in vowels:
        count = count + 1
        print(count)
