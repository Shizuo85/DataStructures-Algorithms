#Note: units must be inputted in the right form(proper upper amd lower cases), as the SI unit demands 
def intensive_properties(tuple1,tuple2):
    """
    This function takes in a tuple(tuple1) of pressure and temperature values in SI units and a tuple(tuple2) containing
    the desired output unit as parameters and returns a tuple of the pressure and temperature in the desired unit.
    """
    if type(tuple1)!= tuple or type(tuple2)!=tuple:
        return "Wrong argument type"
    elif len(tuple1)!=2 or len(tuple2)!=2:
        return "Invalid tuple length"
    Dict={"C":tuple1[1]-273, "F":32+9*(tuple1[1]-273)/5, "R":tuple1[1]*9/5, "Pa":tuple1[0], "atm": tuple1[0]/101325, "mmHg":tuple1[0]/133.32, "Bar":tuple1[0]/100000}
    #this dictionary contains units as keys and their conversion from SI unit using the first tuple as values
    if type(tuple1[0])!=int and type(tuple1[0])!=float or type(tuple1[1])!=float and type(tuple1[1])!=int or tuple2[1] not in Dict or tuple2[0] not in Dict:
        return "Invalid tuple element"
    else:
        temp=Dict[tuple2[1]]
        pres=Dict[tuple2[0]]
        return (pres, temp)
print(intensive_properties((0,0),("atm", "F")))
