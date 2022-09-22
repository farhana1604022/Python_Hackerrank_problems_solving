var1=open('myfile.txt','w')

print('name :',var1.name)
print('Is closed: ',var1.closed)
print('Opening mode : ',var1.mode)



#write to file
var1.write('I love Python')
var1.write('I also love C++')