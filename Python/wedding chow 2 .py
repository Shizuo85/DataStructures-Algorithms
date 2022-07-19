https://amp.reddit.com/r/nasa/def wedding_chow(supplies):
    """
    This function takes in a string of 5 different letters(r,s,d,f,m) representing meals each repeated 0 or more times in any
    order(A set of the 5 meals makes a complete chow) and returns a tuple of two elements.The first element is an integer
    reprsenting the maximum number of complete chows. The second is the left over chow as a string in the order rsmfd
    """
    if type(supplies)!=str:
        return "Invlid input"
    #the maximum set is formed when the minimum meal is exhausted. 'a' represents the minimum meal
    a=min(supplies.count("r"), supplies.count("m"), supplies.count("f"), supplies.count("d"), supplies.count("s"))
    #b reprsents the leftover meals, which is gotten when the set containing 'a' of each meal is formed
    b=str((supplies.count("r")-a)*"r")+str((supplies.count("s")-a)*"s")+str((supplies.count("m")-a)*"m")+str((supplies.count("f")-a)*"f")+str((supplies.count("d")-a)*"d")
    return (a,b)