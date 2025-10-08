def is_isogram(string):
    temp_str = ''.join(char for char in string.lower() if char.islower())
    str_set = set(temp_str)
    return len(temp_str) == len(str_set)
