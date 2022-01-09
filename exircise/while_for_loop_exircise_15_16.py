
n = int( input( "Enter a number to define list dimension(n): " ) )

count = 0
sum = 0
ls = []


while (count < n):
    num = int( input( "Enter a number to add to a list: " ) )
    ls.append(num)
    sum += num
    count+=1; 
    
avg = sum / n
    
print(f"The list: {ls}")
print(f"the average is: {avg}")

userNum = 0

while (userNum != -999):
    userNum = int( input( "Enter a number to parse, to exit eneter -999 : " ) )
    userNumTmp = userNum
    
    if (userNumTmp < 0):
        userNumTmp = userNumTmp * -1
        
    numStr = str(userNumTmp)
    resStr = f"Number of digits: {len(numStr)}"
    print(resStr)
    
    for i in range(len(numStr)):
        resStr += f"\nThe {i+1} digit is: {numStr[i]}"
        
    # dig = userNum % 10
    print(resStr)
    
# #1
# n = int(input("enter n:"))
# s=0
# for i in range(n):
#     s+=int(input("enter num:"))
#     print(s/n)
    
# #2
# x=0
# while x != -999: 
#     s=0 
#     while (num!=0):
#         s+=1
#         num //= 10
        
#     print(s)
#     x = int(input( "more? (-999 to stop):" )




   
    

            
        