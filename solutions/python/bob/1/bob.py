def response(hey_bob):
    trimmed_phrase = hey_bob.strip()

    if not trimmed_phrase:
        return "Fine. Be that way!"
        
    is_question = trimmed_phrase.endswith('?')
    is_yelling = trimmed_phrase.isupper()
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    if is_yelling:
        return "Whoa, chill out!"
        
    if is_question:
        return "Sure."
        
    return "Whatever."
