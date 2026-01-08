# Exercise 4: Primitive Quiz - Advanced Requirements
questions = {
    "France": "Paris", 
    "Germany": "Berlin", # Corrected spelling: "Germany"
    "Italy": "Rome",
    "Spain": "Madrid", 
    "Austria": "Vienna", # Added missing quote before Vienna
    "Sweden": "Stockholm",
    "Norway": "Oslo", 
    "Belgium": "Brussels", 
    "Portugal": "Lisbon", # Corrected spelling: "Portugal"
    "Greece": "Athens"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")
    
    # Advanced Requirement: Ignore capitalization
    # Corrected: capital.lower() (used dot instead of comma)
    if answer.strip().lower() == capital.lower():
        print("Correct!")
    else: # Corrected spelling: "else" instead of "eles"
        print(f"Wrong. The correct answer is {capital}.")
