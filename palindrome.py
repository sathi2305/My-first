# Check if a string is a palindrome

s = input("Enter a string: ")

# Convert to lowercase and remove spaces for accurate comparison
s = s.replace(" ", "").lower()

if s == s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
