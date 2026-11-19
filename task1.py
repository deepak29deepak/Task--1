#Arthimetic operation
#Addition
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("add:",a+b)'''

#Subtraction
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("subtract:",a-b)'''

#divisioin
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("div:",a/b)'''

#multiplication
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("mul:",a*b)'''

#floor division
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("f.div:",a//b)'''

#remainder
'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("remainder:",a%b)'''

#square
'''a=int(input("Enter the value:"))
print(a**a)'''

#average
'''a=int(input("a mark:"))
b=int(input("b mark:"))
c=int(input("c mark:"))
d=int(input("d mark:"))
e=int(input("e mark:"))
t=a+b+c+d+e
m=t/5
print("Total:",a+b+c+d+e)
print("Average:",m)'''

#last two digit
'''a=int(input("enter a:"))
b=a%100
print("last two digit:",b)'''

#last three digit
'''a=int(input("enter a:"))
b=a%1000
print("last three digit:",b)'''

#name
'''a="Deepak"
print(a)'''

#assingment operator
'''a=100
a+=50
print(a)
a-=20
print(a)
a*=5
print(a)
a/=2
print(a)
a%=2
print(a)'''

#comparison operator
'''a=int(input("enter value:"))
b=int(input("enter value:"))
print(a==b)'''

#!=
'''a=int(input("enter value:"))
b=int(input("enter value:"))
print(a!=b)'''

#>
'''a=int(input("enter value:"))
b=int(input("enter value:"))
print(a>b)'''

#voting
'''a=int(input("Enter age:"))
print(a>=18)'''

#marks
'''a=int(input("Enter mark:"))
print(a>=35)'''
#logical operator
'''x=4
print(x>0 and x%2==0)'''

#voting
'''x=20
print(x>18)'''

#passing
'''x=50
y=34
print(x>35 or y>35)'''

#1-50
'''x=25
print(x>1 or x<50)'''

#not
'''x=12
print(not(x==0))'''

#membership operator
'''x=['name']
print("a"in x)'''

#python
'''x=['java','python' ,'c++'] 
print("python" in x)'''

#number
'''x=[1,2,3,4,5]
print("3"in x)'''

#character
'''x=['apple','mango']
print('banana' not in x)'''

#identity operator
'''a=20
b=20
print(a is b)'''

#list
'''a=[1,2,3]
b=a
print(a is b)'''

#same variable
'''a=[1,2,3,4]
b=a
print(a is b)'''

#not same
'''x=['apple','mango']
print('banana' is not x)'''

#bitwise operator
'''a=10
b=5
print("AND:",a&b)
print("OR:",a|b)
print("XOR:",a^b)
print("~a;",~a)'''

#student result
'''Name=str(input("Enter student name:"))

s1=float(input("Enter mark of subject 1:"))
s2=float(input("Enter mark of subject 2:"))
s3=float(input("Enter mark of subject 3:"))
s4=float(input("Enter mark of subject 4:"))
s5=float(input("Enter mark of subject 5:"))
    
Total=s1+s2+s3+s4+s5
average=Total/5
print("Total marks:",Total)
print("Average marks:",average)
p=35
if(s1>35 and s2>35 and s3>35 and s4>35 and s5>35):
    print("passed in all subject")
else:
    print("Failed")'''

#Electricity unit
'''previous_unit=int(input("Enter the unit:"))
current_unit=int(input("Enter the unit:"))
unit_rate=float(input("Enter unit rate:"))

unit=current_unit-previous_unit
bill= unit*unit_rate

print("Unit consumed:",unit)
print("Bill:",bill)'''

#product and price
'''Price =float(input("Enter product price:"))
Quantity =int(input("Enter quantity:"))
discount_rate =float(input("Enter discount percent:"))

Total =Price*Quantity
Discount =Total * discount_rate/100
Final_price = Total-Discount

print("Total Amount:",Total)
print("Discount:",Discount)
print("Final Amount:",Final_price)'''

#voting
'''Age =int(input("Enter the age:"))
if(Age>18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")'''

#odd or even
'''x=int(input("Enter number:"))
if(x%2==0):
 print("The number is even")
elif(x%2!=0):
    print("The number is odd")'''

#username and password
'''u=input("Enter the username: ")
p=input("Enter the password: ")

if(u=="Deepak"):
    print("Correct username")

    if(p=="12345"):
        print("Correct password")
    else:
        print("Incorrect password")
elif(""):
    print("Incorrect username")
else:
    print("Incorrect details")'''

#Number comparison
'''a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))

if(a>b and a>c):
    print("the number a is Largest",a)
elif(b>a and b>c):
        print("the number b is largest",b)
else:
    print("the number c is largest",c)'''



      
 
    




