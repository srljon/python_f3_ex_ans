# Exercise 1: Simple Vowel or Consonant Guesser

# 1. Get a Letter:
print("Enter a single lowercase letter:")
user_letter = input()

# 2. Assume Valid Input: For this exercise, we will assume the user enters a single lowercase letter as requested.

# 3. Check for Vowel or Consonant:
if user_letter == "a" or user_letter == "e" or user_letter == "i" or user_letter == "o" or user_letter == "u":
    # Use print() to display: "You entered [letter], which is a vowel."
    print(f"You entered {user_letter}, which is a vowel.")
else:
    # Use print() to display: "You entered [letter], which is likely a consonant."
    print(f"You entered {user_letter}, which is likely a consonant.")

# 4. Run and Test:
# Test with different lowercase letters: "a", "b", "e", "z".