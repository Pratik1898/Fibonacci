num=int(input("Enter the nth digit: "))
first=0
second=1
if num == 0 or num ==1:
    print("Fibonacci Series :",first)
else:
    print("Fibonacci Series",first, second,end=' ')
    for i in range(2,num):

        next=first+second
        print(next,end=' ')
        first=second
        second=next
