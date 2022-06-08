#Have the function Palindrome(str) take the str parameter being passed and return the string true 
#if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. 
#For example: "racecar" is also "racecar" backwards. 

def Palindrome(strParam):
  f=strParam.replace(" ","")
  if f[::-1]==f:
    return "true"
  else:
    return "false"