def recite(start_verse, end_verse):
    RHYME_LINES = [
        None,
        ["house", "that Jack built."], # 1 (Used only for the item, not the action)
        ["malt", "that lay in"],       # 2
        ["rat", "that ate"],           # 3
        ["cat", "that killed"],        # 4
        ["dog", "that worried"],       # 5
        ["cow with the crumpled horn", "that tossed"], # 6
        ["maiden all forlorn", "that milked"], # 7
        ["man all tattered and torn", "that kissed"], # 8
        ["priest all shaven and shorn", "that married"], # 9
        ["rooster", "that crowed in the morn that woke"], # 10
        ["farmer sowing his corn", "that kept"], # 11
        ["horse and the hound and the horn", "that belonged to"], # 12
    ]

    all_verses = []
    FINAL_PHRASE = "that lay in the house that Jack built."
    for verse_number in range(start_verse, end_verse + 1):
        current_verse = f"This is the {RHYME_LINES[verse_number][0]}"
        for i in range(verse_number, 2, -1):
            current_action = RHYME_LINES[i][1]
            prev_item = RHYME_LINES[i - 1][0]
            current_verse += f" {current_action} the {prev_item}"
        if verse_number == 1:
            current_verse = f"This is the {RHYME_LINES[1][0]} that Jack built."
        else:
            current_verse += f" {FINAL_PHRASE}"
        all_verses.append(current_verse)
    return all_verses