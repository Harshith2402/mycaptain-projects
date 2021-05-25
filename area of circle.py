#python program to find area of a circle

r=float(input('enter the radius of circle: ')) #getting input from the user

import math
math.pi  #for getting the exact value of pi , I had imported math module

a=(math.pi)*r**2 #assigning the formula

print('Area of circle is: ', a)


#python program to accept a filename and its extension

file = input('enter your file name: ') #taking input from user 

fn = f.split('.') #using split function to find the extension

print('extension of file is : ' +fn[-1] , " 'python' ") #printing the extension
