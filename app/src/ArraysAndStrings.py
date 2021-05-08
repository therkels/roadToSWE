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

def is_palindrome(string):
    #check string length
    string_len = len(string)
    
    if string_len < 3:
        return False
    #build a frequency dictionary
    freq_dict = dict()
    for char in string:
        char = char.lower()
        if char == ' ':
            continue
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
        print(freq_dict)
    #build odd and evens
    odd_even = {"odd": 0, "even": 0}
    for item in freq_dict.keys():
        if freq_dict[item] % 2 == 0:
            odd_even["even"] += 1
        else:
            odd_even["odd"] += 1

    return odd_even["odd"] <= 1

def is_one_away(string_tup):
    if string_tup[0] == string_tup[1]:
        return True
    
    set_1 = set()
    set_2 = set()

    for char in string_tup[0]:
        set_1.add(char)

    for char in string_tup[1]:
        set_2.add(char)
    
    return len(set_1 ^ set_2)//2 < 2


def compress_string(string):
    ret_str_arr = []
    ret_str = ""
    max_count = 0
    i = 0
    while i < len(string):
        local_count = 1
        curr_letter = string[i]
        while i+1 < len(string) and string[i+1] == curr_letter:
            local_count += 1
            i += 1
        if local_count > max_count:
            max_count = local_count
        ret_str_arr.append(curr_letter)
        ret_str_arr.append(str(local_count))
        i += 1

    if max_count == 1:
        return string
    return ret_str.join(ret_str_arr)

        


print(compress_string("aabccccaaa"))
print(compress_string("abca"))