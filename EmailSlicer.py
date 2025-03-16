#Email Slicer 

email = input('Enter Your Email :')

index = email.index('@')

username = email[:index]
domain = email[index + 1:]

print(f"Your Username is: {username}\nYour Domain is: {domain}")