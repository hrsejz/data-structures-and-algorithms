# Define a function that calculates the factorial of a number and provides the step-by-step process
def factorial_with_process(n):
    # Base case: If n is 0, return 1 (since 0! = 1) and the process as "1"
    if n == 0:
        return 1, "1"  # 0! = 1 and the process is simply "1"
    else:
        # Recursive call: Get the factorial and process for n-1
        sub_result, process = factorial_with_process(n - 1)
        # Append the current number (n) to the process string, following the format "n.process"
        current_process = f"{n}.{process}"  
        # Return the result of the multiplication (n * sub_result) and the updated process string
        return n * sub_result, current_process

n = int(input("Enter number to get factorial: ")) 

if n < 0:
    print("Factorial is not defined for negative numbers.")  # Display a message for invalid input
else:
    result, process = factorial_with_process(n)  # Call the function to calculate factorial and get process string

    # If the process string ends with ".1", remove the unnecessary last part (the base case "1")
    if process.endswith(".1"):
        process = process[:-2]  
    
    print(f"{n}! = {process} = {result}") # Print the result in a readable format: "<n>! = <process> = <result>"


#####################

# if n in [0, 1]:
# The base case checks for both n = 0 and n = 1, returning 1 in either case. 
# For other values, the function recursively calculates the factorial and constructs the process string.

