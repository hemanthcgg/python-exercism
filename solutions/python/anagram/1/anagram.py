def find_anagrams(word, candidates):
    result = [w for w in candidates if(set(tuple(w.lower()))==set(tuple(word.lower())) and  w.lower()!=word.lower() and sorted(w.lower())==sorted(word.lower()))]
    return result

    
