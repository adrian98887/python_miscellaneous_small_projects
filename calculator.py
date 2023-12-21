#Calculator
def add(n1, n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

op_dict = {'+': add, '-': substract, '*': multiply, '/': divide}

def calculator():
  n1 = float(input("Enter the first number: "))
  for key in op_dict:
    print(key)
  should_continue = True
  
  while should_continue:
    symbol = input(f"Pick an operation from the line above: ")
    n2 = float(input("Enter the second number: "))
    calculation_function = op_dict[symbol]
    answer = calculation_function(n1,n2)
    print(f"{n1} {symbol} {n2} = {answer}")

    if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation ") == 'y':
      n1 = answer
    else:
      should_continue = False
      calculator()

calculator()
    
    
    
  
 

  
  
  
