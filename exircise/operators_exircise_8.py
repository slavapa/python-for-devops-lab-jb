n1=67895
#n1 = int(input("Enter A 5-digit number: "))


print(n1)

res = n1/3
strFormat = "The number is divided by 3: {0}\n"
strRes = strFormat.format(res)
print(strRes)


res = n1//3
strFormat = "The number is divided by 3 by integers: {0}\n"
strRes = strFormat.format(res)
print(strRes)

res = n1%10
strFormat = "The unity digit only: {0}\n"
strRes = strFormat.format(res)
print(strRes)

res = (n1//10)%10
strFormat = "Digit number only: {0}\n"
strRes = strFormat.format(res)
print(strRes)

res = (n1//10)%10
strFormat = "Digit number only: {0}\n"
strRes = strFormat.format(res)
print(strRes)

res = (n1%10)**5
strFormat = "The unity digit in the power 5: {0}\n"
strRes = strFormat.format(res)
print(strRes)

strn = str(n1)

lowerestNum1 = 10
lowerestNum2 = 10
result = 12

for snum in strn:
    num = int(snum)
        
    if ( num < lowerestNum1 and lowerestNum1 == 10 ): 
        lowerestNum1 = num
        lowerestNum2 = num
    elif ( num < lowerestNum1 ):
        lowerestNum2 = lowerestNum1
        lowerestNum1 = num
    elif ( num > lowerestNum2  and lowerestNum1 == lowerestNum2):
        lowerestNum2 = num
        

result = str(lowerestNum1) + str(lowerestNum2)
strFormat = "A number consisting of the two digits lower: {0}{1}\n"
strRes = strFormat.format(lowerestNum1, lowerestNum2)
print(strRes)
#print(result)


num = n1
print(num/3) 
print(num//3) 
d1 = num % 10 
print(d1) 
d2  = ((num//10) % 10) 
print(d2) 
print((num % 10) ** 5) 
print((d1*10) + d2)












    