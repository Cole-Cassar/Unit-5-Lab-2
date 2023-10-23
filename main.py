file = open("sample.ini")
# Opens up file "sample.ini"
num_words = 0
# Initial counter
with open("sample.ini") as file:
    for line in file:
        # Process which takes the file and reads each line
        words = line.split()
        num_words += len(words)
# Reads all "words" and produces the total number
print("Number of words: ")
print(num_words)
# Shows how many words were in the file
file = open("counts.txt", "w")
file.write(f"Total number of words:\n {num_words}")
file.close
# Creating "counts.txt", this file will show the amount of words in the "sample.ini" file