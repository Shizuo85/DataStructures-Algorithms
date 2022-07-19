def numToHex(num):
  """
  This function takes in a number in base ten and returns its'
  hexadecimal equivalent
  """
  if num==0 or type(num)!= int: return num
    
  hexDict = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9", 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}

  hex= ""
  while num!=0:
    hex += hexDict[num%16] #this adds the remainder
    num = num//16
  
  return hex[::-1]

print(numToHex(475565475565475565))
#print(hex(475565475565475565)) #to compare