import string
import random

def generate_password(length):
    if length < 6:
        print("Regenerate, password not long enough!")
        return None

  
    letters = [random.choice(string.ascii_letters) for _ in range(length - 3)]
    digits = [random.choice(string.digits) for _ in range(3)]
    
   
    password_list = letters + digits
    random.SystemRandom().shuffle(password_list)
    
    return ''.join(password_list)


if __name__ == "__main__":
    try:
        n = int(input("How many elements in password: "))
        password = generate_password(n)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")
