# Lambda function example:

add = lambda a,b: a+b

print(add(3,3))




# Using lambda funtion in another function:


def lambda_func(j,k):
    return lambda a,b : (a + b) + (j-k)


result = lambda_func(6,4)                   
print(result(10,5))






