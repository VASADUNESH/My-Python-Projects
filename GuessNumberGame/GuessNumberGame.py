from random import randint

lowerNum,higherNum=1,10
randomNumber=randint(lowerNum,higherNum)
print(f"I'm thinking of a number between {lowerNum} :{higherNum}.")

while True:
  try:
    userGuess=int(input('\nGuess: '))
  except ValueError as e:
    print(e)
    continue

  if userGuess>randomNumber:
    print('The number is lower.')
  elif userGuess<randomNumber:
    print('The number is Higher.')
  else :
    print('You guesed it!')
    break