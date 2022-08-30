def is_palindrome_recursive(word, low_index, high_index):
    try:
        if high_index == 0:
            return True
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
    except IndexError:
        return False


# if __name__ == "__main__":
#     word = ""
#     print(is_palindrome_recursive(word, 0, len(word) - 1))
