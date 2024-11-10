# this program gives longest word from the list
def longest_word(find_list):
    word_len =[]
    for n in find_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][1]

# find_list = ["c","php","python","java","javascript","html"]
print(longest_word( ["c","php","python","java","javascript","html"]))