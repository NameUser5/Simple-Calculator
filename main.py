section1 = "Simple, breakable calculator:"
section1= section1.upper()

print(section1)
print("\nWelcome! Feast your eyes upon the great Calcu-maton! Enter two numbers below and prepare to be amazed!~")


num1 = float(input("Enter your first number: ")) 
operation = str(input("Enter your operation: "))
'''operations = ["+","-","*","/","^","**"]'''
num2 = float(input("Enter your second number: ")) 

def add(num1,num2):
  if operation == "+":
    total = num1 + num2
  return total
def subtract(num1,num2):
  if operation == "-":
    total = num1 - num2
  return total
def multiply(num1,num2):
  if operation == "*":
    total = num1 * num2
  return total
def divide(num1,num2):
  if operation == "/":
    total = num1 / num2
  return total



operations = ["+","-","*","/"]

# def add(num1,num2):
#   print(add)
# subtract = num1 - num2
# multiply = num1 * num2
# divide = num1 / num2
# exponent = num1 ** num2

for o in operations:
  if operation == "+":
    result = add(num1,num2)
  if operation == "-":
    result = subtract(num1,num2)
  if operation == "*":
    result = multiply(num1,num2)
  if operation == "/":
    result = divide(num1,num2)

  
print(f"\nYour result is {result}.")