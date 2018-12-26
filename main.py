# Raymond.Ginting@gmail.com

# Display three first letter of a given input string N times, but when the input is less then three, display in reverse.

def displayMulti(string, times):
  #make sure string is more than 3 letters
  if(len(string) >= 3):
    return string[:3]*times
  #when the input is less then three letter
  else:
    return string[::-1]*times

displayMulti('Jakarta', 2)
displayMulti("Jakarta", 3)
displayMulti("Rey", 2)
displayMulti("Or", 2)