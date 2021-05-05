"""
Check if a string is unique.
:param in_str The string being tested
:return [boolean]
"""
def is_unique(in_str):
    char_list = [False for i in range(128)]
    for char in in_str:
        ascii_val = ord(char)
        if char_list[ascii_val]:
            return False
        char_list[ascii_val] = True
    return True


"""
Decide if one string is a permutation of the other.
:param str_a The first string
:param str_b The second string
:return [boolean] whether two strings are permutations
"""
def check_permutation(str_a, str_b):
    freq_dict = dict()
    for char in str_a:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    for char in str_b:
        if char not in freq_dict:
            return False
        freq_dict[char] -= 1

    for key in freq_dict.keys():
        if freq_dict[key] != 0:
            return False
    return True

"""
Converts string to a URL, removing all spaces.
:param in_str The string to be converted
:param str_length The length of the string
"""
def URLify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string