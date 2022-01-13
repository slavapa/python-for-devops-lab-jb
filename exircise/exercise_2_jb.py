
##############################################


# 1

def isodd(num):
    return num % 2 == 1

a = int(input("enter num:"))
print(isodd(a))


##############################################


# 2

def avg(n): s=0
    for i in range(n):
        s+=in t( input("enter num:"))
    return s/n ##############################################


# 3
def numdigits(num):
    s=0 while (num!=0):
        s +=1
        n um //=10
    ret urn s

def numdigi \


2(num):
    return len(str(abs(num)))

###########


#################################


# 4
s  = int(input( "enter num:"))
print("20 - " , s//20)
pint (" 10 - " , s%20 //10) pr int("5 - " , s%10 // 5)
pr i nt("1 - " , s%5)


##### # #######################################


# 5
def mypow(x,y):
    s = 1
    for i in range(y):
        s*=x
    retur n s

############


################################


# 6
def getdis():
    x = float(input("enter discount:"))
    return x

def getprice( \


pr):
    discount=0.1
    if pr > 1000:
        discount = getdis()

    return pr-pr*discount


# # ############################################


# 7

def isnotzero(a):
    return a!=0

def getd et (a,


b,c):
    r et urn (b**2 - 4*a*c )

def de t p os(a \


,b,c): return getdet(a,b,c) >= 0

a = i nt (input(


"enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if isnotzero(a) == False:
    print("divide by zero")
elif detpos(a,b,c) == False:
    print("Negative det")
else:
    print("x1=" , (-1*b + getet(a, b ,c) / (2*a)))
    prin t ("x2=" , (-1*b - getet(a, b ,c) / (2*a)))



##### # ####


################################

# 9
def smalldiv(a,b):
    m = mi n(a,b)
    for i i n range(2,m):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

def biggest(a,


b):
    m=mi n(a,b)
    for i in range(m,1,-1):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

def mypow(a,


b):
    re turn pow(a,b)

def sq diff \


(a,b): return pow(a,0.5) - pow(b, 0.5)

a = int (input


("enter a:"))
b = int(input("enter b:"))

d = {'a':biggest , ' b':smaldiv , 'c':mypow, 'd': sqdiff}

wh ile True:
    print("a-	the biggest devider")
    print("b-	the smallest divider")
    print("c-	the result of pow(a,b)")
    print("d-	the result of sqrt(a)-sqrt(b)")
    print("e-	exit")
    c = input("")
    if c=='e':
        break
    print(d[c](a,b))




### ###


###################################


# 10
def factorial(x):
    m = 1
    for i in range(2,x+1):
        m*=i
    ret ur n m

def exp(s


ps, x):
    s = 0
    m = 1
    for i in range(steps):
        s+= m * ((x ** i) / factorial(i))
        m*=-1

    re tu rn s

##########


##################################


# 11

def printmsg(cid):
    print(cid ," - VIP cut omer")

num = int(


input("enter customer id:"))
sm = int(input("enter total orders:"))
good = int(input("pay on time? "))
years = int(input("enter number of years:"))

a = (sm > 8000)
b = (good == 1)
c = (years > 5)

if ((a == True) and (c == True)) or (b == True):
    printmsg(num)



























