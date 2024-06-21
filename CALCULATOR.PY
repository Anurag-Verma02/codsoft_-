print("WELCOME TO YOU PYTHON CALCULATOR")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("~~~~F~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("For addition press 1")
print("For subtraction press 2")
print("For multiplication press 3")
print("For division press 4")
print("For modulus press 5")
print("For floor division press 6")
print("For exponential press 7")
print("For percentage press 8")
print("For square root press 9")
print("For cube root press 10")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
c = input("Enter your choice: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if c == "1":
  print("The addition of", a, "and", b, "is", a + b)
elif c == "2":
  print("The subtraction of", a, "and", b, "is", a - b)
elif c == "3":
  print("The multiplication of", a, "and", b, "is", a * b)
elif c == "4":
  print("The division of", a, "and", b, "is", a / b)
elif c == "5":
  print("The modulus of", a, "and", b, "is", a % b)
elif c == "6":
  print("The floor division of", a, "and", b, "is", a // b)
elif c == "7":
  print("The exponential of", a, "and", b, "is", a**b)
elif c == "8":
  print("The percentage of", a, "and", b, "is", a * b / 100)
elif c == "9":
  print("The square root of", a, "is", a**0.5)
elif c == "10":
  print("The cube root of", a, "is", a**(1 / 3))
else:
  print("Invalid choice")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("THANKYOU FOR USING YOUR PYTHON CALCULATOR")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
