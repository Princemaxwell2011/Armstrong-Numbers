n = int(input("Enter the number: "))
num = n
s = 0

flag=False

while(n>0):
    digit = n%10 #Finding th last digit
    s = s+(digit**3)
    n = n//10  
    if(s==num):
     print(" Number is Armstrong Number")
    else:
     print("Number is Not an Armstrong Number")