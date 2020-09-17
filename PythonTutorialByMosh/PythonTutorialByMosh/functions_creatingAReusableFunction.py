
words_to_special = {
    ":)": "😀",
    ":(": "😥"
}


def convert_special_words(message):
    words = message.split(" ")
    output = ""

    for word in words:
        output += words_to_special.get(word, word) + " "
    return output


user_input = input(">")
print(convert_special_words(user_input))