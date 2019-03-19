def Fizzbuzz(listA, listB):

    x = len(listA)
    y = len(listB)

    z = x+y
 
    if z%5 == 0 and z%3 == 0:        
        return "Fizzbuzz"
    elif z%3 == 0:
        return "Fizz"

    elif z%5 == 0:
        return "Buzz"
    
print(Fizzbuzz([3,6,7,9], [1,2,2,3,4,7,9,7,8,8,7]))