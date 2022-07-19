def encoder(text, shift):
  """
  This function takes in a string to encode and a shift value as an
  integer to use for encoding
  """
  if type(text)!=str or text.isalpha()!= True or type(shift)!=int or shift<0: 
    return "Invalid argument(s)"

  result=""
  for i in text:
    if i.isupper():
      if (ord(i)+shift)>90:
        result+=chr((ord(i)+shift-91)%26+65) 
      else:
        result+=chr((ord(i)+shift))
    else:
      if (ord(i)+shift)>122:
        result+=chr((ord(i)+shift-123)%26+97)
      else:
        result+=chr((ord(i)+shift))
  return result

  
def decoder(text, shift):
  """
  This function takes in a string to decode and a shift value as an
  integer to use for decoding
  """
  if type(text)!=str or text.isalpha()!= True or type(shift)!=int or shift<0: 
    return "Invalid argument(s)"

  result=""
  for i in text:
    if i.isupper():
      if (ord(i)-shift)<65:
        result+=chr(90-abs(26+ord(i)-90-shift)%26)
      else:
        result+=chr(ord(i)-shift)
    else:
      if (ord(i)-shift)<97:
        result+=chr(122-abs(26+ord(i)-122-shift)%26)
      else:
        result+=chr(ord(i)-shift)
  return result


def endec(text, shift, action):
  """
  This function takes in a string to encode or decode, a shift
  value as an integer to use for the action and finally a boolean
  value to decide which action
  """

  if type(text)!=str or text.isalpha()!= True or type(shift)!=int or shift<0 or type(action)!=bool: 
    return "Invalid argument(s)"

  if action: return encoder(text, shift)
  else: return decoder(text, shift)

print(endec("python", 5, True))
print(endec("udymts", 5, False))