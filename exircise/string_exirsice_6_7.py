
#*********** Task 1
s = "xy" * 50
print(s + "\n")

#*********** Task 2
s=""

for i in range(37, 127):
    s+=chr(i)

for i in range(0,10):
    s+=str(i)
    
    
#s = input("Enter string at leats 100 length: ")
strFormat = "The original string s is: {0}\n"
strRes = strFormat.format(s)
print(strRes)
#print(s + "\n")


strFormat = "The length of s is: {0}\n"
strRes = strFormat.format(len(s))
print(strRes)
#print("The s length is: " + str(len(s)))


strFormat = "The First 5 letters is: {0}\n"   
strRes = strFormat.format(s[:5])
print(strRes)
#print(s[:5])


strFormat = "The last 5 letters is: {0}\n"   
strRes = strFormat.format(s[-5:])
print(strRes)
#print(s[-5:])

strFormat = "Each second letter s[::2] : {0}\n"   
strRes = strFormat.format(s[::2])
print(strRes)

endIndex = int(len(s)/2)
strFormat = "The first helf of string s[:int(len(s)/2)] : {0}\n"   
strRes = strFormat.format(s[:endIndex])
print(strRes)
strFormat = "The length of s is: {0}\n"
strRes = strFormat.format(len(s[:endIndex]))
print(strRes)

strFormat = "To uppesr case : {0}\n"   
strRes = strFormat.format(s.upper())
print(strRes)