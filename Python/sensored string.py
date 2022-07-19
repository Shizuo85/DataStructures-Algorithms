def uncensor(txt,vowels):
    """
    This function takes in two strings, one with the vowels replaced by "*" and the other
    with the missing vowels in order, and returns the right combiination of the two
    """
    assert type(txt)==type(vowels)==str and txt.count("*")==len(vowels)
    vowel=["a", "e", "i", "o", "u"]
    for i in vowels:
        assert i.lower() in vowel
        txt=txt[:txt.index("*")+1].replace("*", i)+txt[txt.index("*")+1:]
    return txt
