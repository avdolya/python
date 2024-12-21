word_list = []
def add_word(word):
    word_list.append(word)
def get_work():
    return f'{", ".join(map(str, word_list))}. ({len(word_list)})'


add_word("мама")
add_word("мыла")
print(get_work())
add_word("раму")
print(get_work())

