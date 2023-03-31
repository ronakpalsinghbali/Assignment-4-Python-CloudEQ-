# Recursive Function example:


print("Program to calculate the Sum of numbers from 1 to n")

#(i) Taking input from the user. 

user_input = int(input("Enter the value of \'n\': "))      




#(ii) Storing that input into another variable.

n=user_input            




#(iii) Function to calculate sum of number from 1 to the number entered by the user.

def sum_of_nums(n):                                          
    if n == 1:
        return 1
    return n + sum_of_nums(n - 1)                             # Function calling itself ,i.e. Recursive function




#(iv) Function calling. 

print(f"The sum of numbers from 1 to {n} is :" , sum_of_nums(n))                                         
