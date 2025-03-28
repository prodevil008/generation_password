import random

a = "abcdefghjiklmnopqrstuvwxyz"
b = "ABCDEFGHJIKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "[]{}()/,.?|;:'!@#$%^&*_-=+"

ali = a + b + c + d
length = 25
password = "".join(random.sample(ali, length))
print("Generate password")
print(password)