n = int(input("Enter a number :"))
sum = 0
temp = n
while temp>0:
    dig =temp%10
    sum+=dig** 3
    temp//=10
if n==sum:
    print("It is an amstrong number")
else:
    print("It is not an amstrong number")