def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

num=int(input("Enter the value of n:"))
print("Fibonacci series")
for i in range(num):
    print(fibonacci(i),end=" ")
