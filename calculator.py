a = int(input("Enter the first no :"))
b = int(input("Enter the second no :"))
c = int(input("Select an operation to perform :\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division"))
if (c==1):
    print("The result is :",a+b)
elif(c==2):
    print("The result is :",a-b)
elif(c==3):
    print("The result is :",a*b)
elif(c==4):
    print("The result is :",a/b)
else:
    print("Invalid")
