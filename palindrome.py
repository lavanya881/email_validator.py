text = input("Enter a string: ")
text = text.lower()

reverse_text = text[::-1]

if text == reverse_text:
    print("It is a palindrome")
else:
    print("Not a palindrome")