import random

a = "abcdefghjiklmnopqrstuvwxyz"
b = "ABCDEFGHJIKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "[]{}()/,.?|;:'!@#$%^&*_-=+"

length = input("Enter the length of the password: ")
ali = a + b + c + d
password = "".join(random.sample(ali, length))
print("Generate password ...")
print(password)