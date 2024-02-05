sum = "+"
sub = "-"
mul = "*"
div = "//"
operator = ""

a = int(input("Enter a number 1st: "))
b = int(input("Enter a number 2nd: "))
operator = str(input("Enter operator: "))

if(operator == sum):
    print("sum : ", a+b)
elif(operator == sub):
    print("sub : ", a-b)
elif(operator == mul):
    print("mul : ", a*b)
elif(operator == div):
    print("div : ", a//b)