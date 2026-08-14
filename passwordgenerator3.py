import random
import string

# Get password length from the user
length = int(input("Enter password length: "))

# Check whether the length is valid
if length <= 0:
    print("Enter a valid length")

else:
    # Combine letters, numbers, and symbols
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Ask how many passwords to generate
    total = int(input("How many passwords do you want? "))

    # Generate passwords
    for i in range(total):

        password = ""

        for j in range(length):
            password += random.choice(characters)

        print("Password", i + 1, ":", password)
