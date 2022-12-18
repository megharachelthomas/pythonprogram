# Reverse of a number
n = 1234
r_num=0
while n !=0:
    digit = n%10
    r_num = r_num*10+digit
    n //=10
print("Reversed number is :"+str(r_num))