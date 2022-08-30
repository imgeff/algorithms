def is_palindrome_recursive(word, low_index, high_index):
    if high_index < 0:
        return False
    if len(word) % 2 != 0:
        if high_index == low_index:
            return True
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        if high_index - low_index == -1:
            return True
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False


# if __name__ == "__main__":
#     word = ""
#     print(is_palindrome_recursive(word, 0, len(word) - 1))
