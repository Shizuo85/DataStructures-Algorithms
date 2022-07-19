def Bcalculator(num1, num2):
    """
    this function takes in two binary numbers as arguments and returns their sum in decimal
    """ 
    assert type(num1)==type(num2)==str
    for i in num1: assert i=="0" or i=="1"
    for k in num2: assert k=="0" or k=="1"   
    return (int(num1,2)+int(num2,2))