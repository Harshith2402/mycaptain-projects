from collections import Counter

#taking the word from user/initializing string

a = input('enter the word: ')

#developinf the 'most_frequent' function

def most_frequent(a):
    
#taking a new empty dictionary
    
    d= dict()
    
#using 'for loop' and 'if-else' with the help of 'd'
    
    for i in a:

        if i not in d:

          d[i] = 1

        else :

          d[i] += 1

    return d

#using collections.counter() to get cout of each element in the given string
res = Counter(most_frequent(a))


print(res)


  
