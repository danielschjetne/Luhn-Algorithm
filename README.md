# Luhn-Algorithm
A simple project on the Luhn-algorithm in Python, mainly used for validating credit card numbers.

The Luhn algorithm or Luhn formula, also known as "modulus 10" is a checksum formula used to validate a variety of identification numbers. In this case we will use Python to validate credit card numbers with the algorithm.

The user will be able to input a credit card number, and the program will return if it's valid or not.

The formula checks the sum of the digits in the card number and checks wheter the sum matches the expected result, or if there is an error in the number sequence. If the total modulus 10 equals zero, the number is valid according to the algorithm.

Steps:
- From the last digit, excluding the check digit, and moving left, double the value of every second digit.
- If the result of this doubling operating is greater than 9, we subtract 9 from the result.
- Take the sum of all digits, including the check digit.
- Check if the total modulo 10 is equal to 0.
- Prompt if the input is valid or invalid. 
