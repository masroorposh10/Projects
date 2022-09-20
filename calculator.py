# calculator.py
# MASROOR AHMAD POSH, ENDG 233 F21, UCID: 30156171
# BLOCK 11
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.




first_val = int(input('Enter first value: '))                # Get the input from user for value of first number(integer) to be evaluated.
first_operator = input('Enter first operator: ')             # Get the input from the user for the first operator in the form of string to perform the mathematical operation.
second_val = int(input('Enter second value: '))             # Get the input from user for value of second number(integer) to be evaluated.
second_operator = input('Enter second operator: ')          # Get the input from the user for the second operator in the form of string to perform the mathematical operation.
third_val = int(input('Enter third value: '))                 # Get the input from user for value of third number(integer) to be evaluated.


print('Entered expression: ', first_val, first_operator, second_val, second_operator, third_val )      # Dislay the expression according to the input in the output.



if first_operator == '+':                                  # Using the IF statement for first operator to be '+' then addition will be done as the first operation.
  if second_operator == '+':                               # Creating the branches for the IF statement for the first operator to be '+'.
     print('Your final answer: ', first_val + second_val + third_val)    # IF the second operator is '+'then additon will be done as the second operation and this result to be printed.
  elif second_operator == '-':                                    
    print('Your final answer:', first_val + second_val -third_val)    # IF the second operator is '-' then subtraction will be done as the second operation and this result will be printed.
  elif second_operator == '*':
    print('Your final answer: ', first_val + second_val * third_val)    # IF the second operator is '*' then multiplication will be performed as the second operationthen this result will be printed.
  elif second_operator == '/':
    print('Your final answer: ', first_val + second_val // third_val)   ## IF the second operator is '/' then the floor division will be perfomed as the second operation and this result will be printed.
     
              
if first_operator == '-':                                         # Using second IF statement for the first operator to be '-' then subtraction will be perfomed as the first operation.
  if second_operator == '+':
    print('Your final answer: ', first_val - second_val + third_val)          # IF the second operator is '+'then additon will be done as the second operation and this result to be printed.
  elif second_operator == '-':
    print('Your final answer: ', first_val - second_val - third_val)         # IF the second operator is '-'then subtraction will be done as the second operation and this result to be printed.
  elif second_operator == '*':
    print('Your final answer: ', first_val - second_val * third_val)         # IF the second operator is '*'then multiplication will be done as the second operation and this result to be printed.
  elif second_operator == '/':
    print('Your final answer: ', first_val - second_val // third_val)        # IF the second operator is '/'then floor division will be done as the second operation and this result to be printed.


if first_operator == '*':                                          # using third IF statement for the first operator to be '*' then subtraction will be done as the first operation.
  if second_operator == '+':
    print('Your final answer: ', first_val * second_val + third_val)# IF the second operator is '+'then additon will be done as the second operation and this result to be printed.
  elif second_operator == '-':
    print('Your final answer: ', first_val * second_val - third_val) # IF the second operator is '-'then subtraction will be done as the second operation and this result to be printed.
  elif second_operator == '*':
    print('Your final answer: ', first_val * second_val * third_val)# IF the second operator is '*'then multiplication will be done as the second operation and this result to be printed.
  elif second_operator == '/':
    print('Your final answer: ', first_val * second_val // third_val) # IF the second operator is '/'then floor division will be done as the second operation and this result to be printed.


if first_operator == '/':                                          # Using fourth IF statement for first operator to be '/' then floor division will be performed as the first operation.    
  if second_operator == '+':
    print('Your final answer: ', first_val // second_val + third_val)     # IF the second operator is '+'then additon will be done as the second operation andthis result to be printed.
  elif second_operator == '-':
    print('Your final answer: ', first_val // second_val - third_val)     # IF the second operator is '-'then subtraction will be done as the second operation andthis result to be printed.
  elif second_operator == '*':
    print('Your final answer: ', first_val // second_val * third_val)     # IF the second operator is '*'then multiplication will be done as the second operation andthis result to be printed.
  elif second_operator == '/':
    print('Your final answer: ', first_val // second_val // third_val)    # IF the second operator is '/'then floor division will be done as the second operation andthis result to be printed.  

        