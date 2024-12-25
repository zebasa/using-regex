import re
while True:
    email=input("what is your email:    ").strip().lower()
    if re.search(r"^(\w|\.)\+@(\w+\.)?\w+\.edu$",email,) and "gmail" in email:
        print("that email is valid")
        print(email)
        break
    else:
        print("that email is invalid")
        
