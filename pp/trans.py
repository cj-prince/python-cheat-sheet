# change every vowel to jg

def trans(pharse):
  trans = ''
  for letter in pharse:
    if letter in 'AEIOUaeiou':
      trans= trans + 'jg'
    else:
      trans = trans + letter
  return trans
print(trans(input('enter a phrase')))
      