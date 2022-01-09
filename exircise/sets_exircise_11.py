

ls1 = [10,20,30,40,50,60]
ls2 = [3,4,5,3,7,5,9,10,20,10]

s1 = set(ls2)

print(s1)

s2 = set(ls1) & set(ls2)
print(s2)

ls3 = list( set(ls1) - {20,40} )
s3 = set(ls1)
print(s3)

s4 = s3 - {20,40}
ls4= list(s4)
print(ls4)


ls5 = list( set(ls1) - set(ls2))
print(ls5)
