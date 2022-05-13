import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
Number = '1234567890'
Symbol = '!@#$%^&*(){}[].,/><?~`'

all = upper + lower + Number + Symbol
length = 10

password = ''.join(random.sample(all,length))

print('generated password :', password)