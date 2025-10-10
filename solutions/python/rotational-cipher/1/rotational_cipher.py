def rotate(text, key):
    encrypted_text = ''
    for i in text:
        if(i.isalpha() and i.isupper()):
            encrypted_text+=chr((ord('A') + (ord(i) - ord('A') + key) % 26))
        elif(i.isalpha() and (not i.isupper())):
            encrypted_text+=chr(ord('a') + ((ord(i) - ord('a') + key) % 26))
        else:
            encrypted_text+=i
        # print(encrypted_text, end=',')
    return encrypted_text
