paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()

paragraph = paragraph.replace(",", "")
paragraph = paragraph.replace(".", "")
paragraph = paragraph.replace("?", "")
paragraph = paragraph.replace("!", "")

words = paragraph.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_frequent_word = None
highest_count = 0

for word in word_counts:
    if word_counts[word] > highest_count:
        highest_count = word_counts[word]
        most_frequent_word = word

print("Word counts:", word_counts)
print("Most frequent word:", most_frequent_word,"- ", (f"{highest_count}"))