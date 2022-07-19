def desc_triangle(a,b,c):
    """
    This function takes in three numbers representing the length of the sides of a triangle and returns a tuple with one
    element being the area of the triangle as a float and the other element describing the type of the triangle as a string
    """
    if type(a)!= int and type(a)!= float or type(b)!= int and type(b)!= float or type(c)!= int and type(c)!= float:
        #ie only numbers allowed
        return "Wrong argument type"
    elif a<=0 or b<=0 or c<=0:
        return "The length can not be less than or equal to zero"
    elif max(a,b,c)>(a+b+c-max(a,b,c)):
        #this checks whether the largest side is greater than the sum of the two other sides
        return "The three sides do not form a triangle"
    else:
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        if a**2==b**+c**2 or b**2==c**2+a**2 or c**2==b**2+c**2:
            #using pythagoras theorem, we determine it is a right triangle
            return ("Right Triangle", area)
        elif a==b!=c or a==c!=b or a!=b==c:
            #since two sides are equal, it iis an isosceles triangle
            return ("Isosceles Triangle", area)
        elif a==b==c:
            #when all sides are equal it is equilateral
            return ("Equilateral Triangle", area)
        else:
            #else all sides are unequal and it is a right triangle, hence it is scalene 
            return ("Scalene Triangle", area)
print(desc_triangle(5.0,13,12))
