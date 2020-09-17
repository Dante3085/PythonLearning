
user_input = input(">")
words = user_input.split(" ")

words_to_special = {
    ":)": "😀",
    ":(": "😥"
}

output = ""
for word in words:
    output += words_to_special.get(word, word) + " "
print(output)