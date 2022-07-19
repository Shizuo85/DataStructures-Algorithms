def is_pali(word): return word==word[::-1]
def match(lst):
    """
    This  function takes in a list of words andd returns a list of tuples of indexes pairs that form a palindrome 
    """
    assert type(lst)==list
    for i in lst:assert type(i)==str and i.isalpha()
    matched=[]
    for i in range(len(lst)):
        for k in range(len(lst)):
            if i==k: continue
            elif is_pali(lst[i]+lst[k]): matched.append((i, k))
    return matched


def isBalanced(bracket):
    """
    This function takes in a string of paraentheses and returns the minimum number of paraentheses(as an
    integer) to be removed to make the string valid, that is each open parantheses is eventually closed
    """
    assert type(bracket)==str
    for i in bracket: assert i=="(" or i==")" or i=="*"
    if "*" not in bracket:
        while "()" in bracket:
            bracket="".join(bracket.split("()"))
        return len(bracket)==0
    else:
        while "*" in bracket:
            while "()" in bracket:
                bracket="".join(bracket.split("()"))
            if bracket[:bracket.index("*")].count("(")<bracket[bracket.index("*"):].count(")"):
                bracket= bracket[:bracket.index("*")+1].replace("*", "(")+ bracket[bracket.index("*")+1:]
            elif bracket[:bracket.index("*")].count("(")>bracket[bracket.index("*"):].count(")"):
                bracket= bracket[:bracket.index("*")+1].replace("*", ")")+ bracket[bracket.index("*")+1:]
            else:
                bracket= bracket[:bracket.index("*")+1].replace("*", "")+ bracket[bracket.index("*")+1:]
    while "()" in bracket:
            bracket="".join(bracket.split("()"))
    return len(bracket)==0
