file = open("sample.ini")

num_words = 0

with open("sample.ini") as file:
    for line in file:
        
        words = line.split()
        num_words += len(words)

print("Number of words: ")
print(num_words)
