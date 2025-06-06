# Exercise 4: Basic Temperature Adviser

# 1. Get Temperature:
print("What is the current temperature in Celsius?")
temp_input = input()
# Assume the user will enter a valid number.
temperature = float(temp_input)

# 2. Provide Advice:
if temperature > 25.0:
    print("It's hot! Wear light clothing like a t-shirt and shorts.")
elif temperature >= 15.0: # and temperature <= 25.0 (implicitly)
    print("It's pleasant! A t-shirt or a light jacket would be good.")
elif temperature >= 5.0: # and temperature < 15.0 (implicitly)
    print("It's cool. Consider wearing a sweater or a jacket.")
else: # temperature < 5.0
    print("It's cold! Wear a warm coat, scarf, and gloves.")

# 3. Run and Test:
# Test with temperatures: 30.5, 22, 15, 10.2, 0, -5.