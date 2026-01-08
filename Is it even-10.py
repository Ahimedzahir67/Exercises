# Exercise 10: Is it even?
# This function determines if the value is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    # Ask the user for a number from within the main function
    val = int(input("Enter a number: "))
    
    # Pass the number to the function and get the returned message
    result = check_even_odd(val)
    
    # Print the message from within the main function
    print(result)

if __name__ == "__main__":
    main()