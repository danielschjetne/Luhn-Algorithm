# Prompting the user for the card number, turning it into a list and removing whitespace.
card_number = list(input('Please enter a card number: ').strip())

# Removing the last digit (the check digit) and storing it in a new variable
check_digit = card_number.pop()

# Reversing the card number
card_number.reverse()

# Creating an empty list to store our digits
processed_digits = []

# Defining the for-loop.
for index, digit in enumerate(card_number):
    if index % 2 == 0:  # Even index
        doubled_digit = int(digit) * 2  # Doubling the digit
        if doubled_digit > 9:  # Checking if digit is > 9
            doubled_digit -= 9  # Subtracting 9
        processed_digits.append(doubled_digit)

    else:
        processed_digits.append(int(digit))

# Creating the final number
total = int(check_digit) + sum(processed_digits)

# Checking if the total is divisible by 10
if total % 10 == 0:
    print('Valid card number!')
else:
    print('Invalid card number!')

