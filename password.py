import random

password = "1234567890qwertyuiopasdfghjklzxcvbnm"
question = int(input("pick how many characters in the password: "))
generated_password = ""
for i in range(question):
    generated_password += random.choice(password)
print("your generated password is: " + generated_password)


