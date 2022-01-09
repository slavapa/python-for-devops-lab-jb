ls = [1,2,3,4,5,6,7,8,9,10]
print(ls)

print(ls[1])
print(ls[-1])
print(ls[::-1])

print(ls.reverse())

ls1 = [10,9,8,7,6,5,4,3,2,1]
ls1.sort()
print(ls1)

print(ls1.count(2))

#ls1.append( int( input( "Enter a numner: ") ) )
#ls1.append( int( input( "Enter a numner: ") ) )
#ls1.append( int( input( "Enter a numner: ") ) )
#ls1.append(11)
#ls1.append(12)
#ls1.append(13)

ls1.append([11, 12, 13])

print(ls1)

#index = input("Enter a index to remove itme from a list: ")
index=2
ls1.remove(index)
print(ls1)

ls1.pop(index)
print(ls1)

ls1[index:index+1] = []
print(ls1)



