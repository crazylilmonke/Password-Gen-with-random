import string
import random
n = int(input("how many elements in password:"))
if n<6:
    print("Regenerate , password not long enough!")
else:
 z = (random.choice(string.ascii_letters) for i in range(n-3))
 y = (random.choice(string.digits) for j in range(3))
 a = ''.join(z)
 b = ''.join(y)
 c = a+b
 print(f"Your generated password is:{c}")
