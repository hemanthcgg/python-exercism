def is_pangram(sentence):
    req_set = set({
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    })
    temp_str = sentence.lower()
    user_set = set(tuple(''.join(char for char in temp_str if char.islower())))
    return req_set == user_set
    
