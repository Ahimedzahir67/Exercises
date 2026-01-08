# [span_4](start_span)Exercise 3: Store and print info using a dictionary[span_4](end_span)
# [span_5](start_span)Advanced: Get user input instead of hardcoding[span_5](end_span)
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age_input = input("Enter your age: ")

# [span_6](start_span)Handle string value for age[span_6](end_span)
try:
    age = int(age_input)
except ValueError:
    print("Invalid age input. Defaulting to 0.")
    age = 0

biography = {"name": name, "hometown": hometown, "age": age}

# [span_7](start_span)Print on separate lines using a single print statement[span_7](end_span)
print(f"Name: {biography['name']}\nHome: {biography['hometown']}\nAge: {biography['age']}")
