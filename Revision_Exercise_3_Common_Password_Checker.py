# Exercise 3: Common Password Checker

# 1. Get Password:
print("Please enter a password:")
password = input()

# 2. Check Against Weak Passwords:
if password == "password" or password == "123456" or password == "admin":
    print("This password is too common. Please choose a different one.")
else:
    print("This password is not on our list of common weak passwords.")

# 3. Run and Test:
# Test with passwords like: "password", "123456", "admin", "MySecureP@ss!", "test".