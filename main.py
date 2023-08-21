# Function that creates the fibonacci sequence up to the users input number
def fibonacci(n):
    a =0
    b= 1
    x = [a, b]
    if n ==1:
        return [a]
    if n == 2:
        return [0,1]
    elif n<=0:
        return "error enter valid input"
    for i in range(2, n+1):
        c= a+b
        a= b
        b= c
        x.append(c)
    return x


print(fibonacci(n=int(input())))