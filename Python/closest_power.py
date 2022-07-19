def cloest_power(base, target):
    """
    This function takes in a base number and a target number as input then returns the smallest
    number that the base number has to be raised to, that brings it cloest to the target number
    """
    if type(base)!=int or type(target)!=int:    #ensures the right type of argument is inputted
        return "Wrong argument type"

    elif base<2 or target<1:
        #target cant be zero or negative
        #base cant be zero, negative or 1(since 1 risedd to the power of anything is 1)
        return "Number out of range"
    else:
        power=0
        test=target                             #this variable is created to ensure the target can be reused in the rest of the program
        if target>base:
            #else the power is 0
            while test>=base:
                """in this loop, the number of iterations is equal to the power to which the base
                will be raised to to get the closest number to the target number equal to or less than it"""
                test=test/base
                power=power+1
        #next the base to power just before the target is compared to that just after the target to determine the closest power
        if (target-base**power)>(base**(power+1)- target):  
            return (power+1)
        elif(target-base**power)<(base**(power+1)- target):
            return power
        else:
            return "Both "+ str(power) + " and " + str(power+1) + " are the closest"    
#print(cloest_power(3, 18))
    
    
