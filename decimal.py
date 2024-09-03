print("the decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")


#wap area of rectangle
i=int(input("length in cm"))
b=int(input("breath in cm"))
a=l*b
print("your area rectangle is:",a,"cm^2")

r=int(input("enter your radius"))
a=3.14*(r*r)
print("your area is:"a)

num=int(input("enter the number rows"))
for i in range(0,num):
    for j in range(0,num-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print("")


ch=str(input("enter a character"))
a=ord(ch)
for x in range(65,x+1):
    for c in range(65,x+1):
        print(chr(c),end="")
    print("")


x=int(input("enter no"))
b=int(input("enter power"))
y=x
for a in range(0,b-1):
    y=x*y
print(y)


n=int(input("enter rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end="")
    print()

    


num=int(input("enter number"))
lim=int(num/2)+1
for i in range(2,lim):
    rem=num%i
    if rem==0:
        print(num,"is not prime number")
        break

else:

      print(num,"is prime number")

      


n=int(input("enter number"))
x=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n/10
if x==r:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

    








    




    
