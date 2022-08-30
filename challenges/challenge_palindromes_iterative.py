def is_palindrome_iterative(word):
    index_end = len(word)
    if index_end > 0:
        for letter in word:
            index_end -= 1
            if letter != word[index_end]:
                return False
        return True
    return False
