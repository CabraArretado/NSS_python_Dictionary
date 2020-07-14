
word_definitions = dict()

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Tired"] = "What I am now"
word_definitions["Handsome"] = "The person reading this"


print(word_definitions["Awesome"])
print(word_definitions["Tired"])


for word, definition in word_definitions.items():
    print(f"The definition of {word} is {definition}")
