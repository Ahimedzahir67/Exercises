# Initialize the list with specific names as required
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# 1. Allow user to input the search term
# Use .strip() to remove accidental spaces
search_term = input("Enter the name to search for: ").strip()

# 2. Implement the search functionality
# Optional: Use .capitalize() so it matches "Sam" even if user types "sam"
if search_term.capitalize() in names:
    print(f"{search_term} found in the list.")
else:
    print(f"{search_term} not found.")
