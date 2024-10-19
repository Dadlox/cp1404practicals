"""
CP1404/CP5632 Practical
Name: Hein Htet
Make a program to count how many times a word was used in a sentence
Estimate: 20 minutes
Actual: 13 minutes
"""

#Input text here
text = input("Text: ")
text_list = text.split()
print(text)
print(text_list)
TEXT_TO_COUNT = {}

#Count up how many of the text are repeated. If they are not repeated, then add that to the dictionary.
for word in text_list:
    if word in TEXT_TO_COUNT:
        TEXT_TO_COUNT[word] += 1
    else:
        TEXT_TO_COUNT[word] = 1

#Check for how much space is needed so the words line up at :
text_width = (max(len(text) for text in TEXT_TO_COUNT))
count_width = (max(len(str(count)) for count in TEXT_TO_COUNT.values())) #On the side note, probably don't need this.

print(text_width, count_width)
for text, total_text in TEXT_TO_COUNT.items():
    print(f"{text:{text_width}} : {total_text:{count_width}}")