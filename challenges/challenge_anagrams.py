def is_anagram(first_string: str, second_string):
    if len(first_string) == len(second_string):
        first_string, second_string = (
            first_string.lower(),
            second_string.lower()
        )
        for letter in first_string:
            second_string = second_string.replace(letter, "", 1)
        if len(second_string) == 0:
            return True
    return False


# if __name__ == "__main__":
#     print(is_anagram("pedra", "perda"))
