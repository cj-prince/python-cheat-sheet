import random
from user import User

def main():
  
  while True:
    print('welcome! save you password ' + '/n')
    print('for new users select nw: to login select lg: to exit select ex')
    sort_code = input().lower()
    print('/n')
    
    if sort_code == 'nw':
      print('create new user')
      created_user_name = input()
      
      print('Enter a password')
      created_password = input()
      
      print('confirm password')
      confirm_password = input()
      
      while confirm_password != created_password:
        print("Password don't match")
        print('enter password')
        created_password = input()
        print('confirm password')
        confirm_password = input()
      else:
        print(f'your {created_user_name}! was created successfully' + '/n')
        print('login')
        print('enter user name')
        enter_username = input()
        print('enter your password')
        enter_password = input()
      
      while enter_username != created_user_name or enter_password != created_password:
        print('username or password is not correct')
        print('enter user name')
        enter_username = input()
        print('enter your password')
        enter_password = input()
      else:
        print('login successful' + '/n')
    
    elif sort_code =='lg':
      print('welcome')
      print('enter your username')
      main_username = input()
      
      print ('enter password')
      main_password = input()
      print('/n')
      while main_username !='admin' or main_password!='admin':
        print('wrong username or password')
        print('enter your username')
        main_username = input()

        print('enter password')
        main_password = input()
        print('/n')
      else:
        print('login successful')
        print('/n')
    
    elif sort_code == 'ex':
      break
    else:
      print('enter a valid code')
if __name__ == '__main__':
  main()
      