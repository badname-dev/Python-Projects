#lex_auth_0127135739583692801137

def add_string(str1):
  #start writing your code here
  if len(str1)<3:
    pass
  if len(str1)==3:
    str1 = "N/A"
    return (str1+"ing")
  elif len(str1)>3 and "ing" not in str1:
    return (str1+"ing")
  elif "ing" in str1:
    return (str1+"ly")
  return str1

str1="amazing"
print(add_string(str1))
