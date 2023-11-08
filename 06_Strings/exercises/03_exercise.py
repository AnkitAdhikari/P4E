# generalizing a function called count_char that counts the given char in the given string


def count_char(word, char):
    count = 0
    for letter in word:
        if letter == char:
            count += 1

    print(count)
    return count


count_char("banana", "a")
