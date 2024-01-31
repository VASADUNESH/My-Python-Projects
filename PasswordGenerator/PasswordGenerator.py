import string,secrets
'''
def containsUpper(pwd):
  for char in pwd:
    if char.isupper():
      return True
  return False

def containsSymbols(pwd):
  for char in pwd:
   if char in string.punctuation:
     return True
  return False
'''

def generatePWD(length,symbols,uppercase):
  combination =string.ascii_lowercase+string.digits
  if symbols:
    combination+=string.punctuation
  if uppercase:
    combination+=string.ascii_uppercase

  combinationLength=len(combination)
  newPwd=''
  for i in range(length):
    newPwd+=combination[secrets.randbelow(combinationLength)]
  return newPwd

def main():
  newPwd=generatePWD(length=10,symbols=True,uppercase=True)
  print(newPwd)

main()