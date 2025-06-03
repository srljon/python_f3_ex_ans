# Exercise 2: Basic Age Group Classifier

# 1. Get Age:
print("Please enter your age:")
age_input = input()
# Assume the user will enter a valid whole number.
user_age = int(age_input)

# 2. Determine Age Group (check in this specific order):
if user_age < 0:
    print("Invalid age entered.")
elif user_age < 13:  # 0 to 12
    print("You are a Child.")
elif user_age < 20:  # 13 to 19
    print("You are a Teenager.")
elif user_age < 65:  # 20 to 64
    print("You are an Adult.")
else:  # 65 or greater
    print("You are a Senior.")

# 3. Run and Test:
# Test with ages: 5, 12, 13, 19, 20, 64, 65, 100. (Also test -2).