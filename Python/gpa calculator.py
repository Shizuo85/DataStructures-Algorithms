def convert(grade):
    """
    This function takes in a number and returns its point equivalent based on unilag's grading system
    """
    if grade>=70:
        return 5
    elif grade>=60 and grade<70:
        return 4
    elif grade>=50 and grade<60:
        return 3
    elif grade>=45 and grade<50:
        return 2
    elif grade>=40 and grade<45:
        return 1
    else:
        return 0
def gpa_calculator(score, unit):
    """
    This funtion takes in two lists of numbers as parameters, one containing scores and
    the other corresponding units and returns the gpa
    """
    if type(score)!=list or type(unit)!=list:
        return "Wrong argument type"
    elif len(score)!=len(unit):
        return "Score and list dont tally"
    else:
        TCU, TQP=0, 0
        #TCU is the total credit unit(total points x unit) and TQP is the total quality point(total unit) 
        for i in range(len(score)):
            if type(score[i])!=int and type(score[i])!=float or type(unit[i])!=int and type(unit[i])!=float:
                return "Wrong element type"
            elif score[i]<0 or unit[i]<0 or score[i]>100:
                return "Element can not be less than zero or greater than 100"
            else:
                TQP=TQP+unit[i]
                TCU=TCU+convert(score[i])*unit[i]
        return round(TCU/TQP, 2)
print(gpa_calculator([81,78,60,60,55,65,67,58.5,75,70],[2,2,2,2,1,2,2,2,1,3]))
                
