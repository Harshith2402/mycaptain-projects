#program to obtain positive numbers in a given range

print('\n enter your elements by giving space to each element')     #instructing user to give the input in correct format

elements = input('\n The elements required in your list:')          #taking input from the user to make a list

a = (elements.split( ))                                             # using split function to develop required list

print(a)                                                            

for i in range(0 , len(a)) :                                        #using 'for loop' to encounter each element in the list
    
    if float(a[i])>0 :                                              #converting each element from 'string' to 'float' for applying mathematical operations
       print((a[i]))

