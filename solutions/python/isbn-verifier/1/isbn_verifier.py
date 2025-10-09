def is_valid(isbn):
    cleaned_isbn = isbn.replace('-', '').replace(' ', '')
    if len(cleaned_isbn) != 10:
        return False
    weighted_sum = 0
    for i in range(10):
        char = cleaned_isbn[i]
        weight = 10 - i
        if i < 9:
            if not char.isdigit():
                return False
            digit = int(char)
        else:
            if char.isdigit():
                digit = int(char)
            elif char.upper() == 'X':
                digit = 10
            else:
                return False
        weighted_sum += digit * weight
    return weighted_sum % 11 == 0