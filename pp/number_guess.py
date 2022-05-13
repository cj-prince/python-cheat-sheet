import random

secretNumber = random.randint(1,20)
print('take a guess you have 6 chance')

for guesses in range(1, 7):
  guess = int(input())
  
  if guess < secretNumber:
    print('low guess')
  elif guess > secretNumber:
    print('to high')
  else:
    break

if guess ==secretNumber:
  print('nice one' + '' + 'it took'+ '' + str(guesses) + '' + 'guesses')
else:
  print('try time passed' + '' 'the number is'+ str(secretNumber))
