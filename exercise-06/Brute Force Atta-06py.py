# Exercise 6: Brute Force Attack
# 1. [span_1](start_span)Define the correct password[span_1](end_span)
correct_password = "12345"

# [span_2](start_span)Optional: Limit attempts to 5[span_2](end_span)
attempts = 5 

# 2. [span_3](start_span)While loop to repeatedly ask for password[span_3](end_span)
while attempts > 0:
    # [span_4](start_span)Ask the user for the password[span_4](end_span)
    user_input = input(f"Enter password: ")
    
    if user_input == correct_password:
        # 3. [span_5](start_span)Output message when correct[span_5](end_span)
        print("Correct password. Access Granted!")
        break
    else:
        attempts -= 1
        # [span_6](start_span)Inform of remaining attempts[span_6](end_span)
        if attempts > 0:
            print(f"Wrong password. Remaining attempts: {attempts}")
        else:
            # [span_7](start_span)Inform when maximum attempts reached[span_7](end_span)
            print("Maximum attempts reached. Authorities alerted!")
