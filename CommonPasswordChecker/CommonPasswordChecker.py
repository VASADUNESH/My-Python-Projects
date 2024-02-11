def check_password(password: str):
  with open('passwords.txt','r') as file:
    common_passwords: list[str] = file.read().splitlines()
    #print(common_passwords)

  for i, common_password in enumerate(common_passwords,start=1):
    if password == common_password:
      print(f'{password}:❌({i})\n')
      return
  print(f'{password}:✅ (Unique)')

def main():
  user_password = input('Enter the password: ')
  check_password(user_password)

if __name__ == '__main__':
  main()