""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
import time
import random

def closest1(L):
    '''
    Return the two closest values in a given list.

    >>> closest1([ 15.1,-12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    
    >>> closest1([1, 2, 4, 6, -9])
    (1, 2)
    
    >>> closest1([1])
    (None, None)
    '''
    if len(L) < 2:
        return (None, None)
    x = L[0]
    y = L[1]
    distance = abs(x - y)
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if abs(L[i] - L[j]) < distance:
                x = L[i]
                y = L[j]
                distance = abs(x - y)
    return (x, y)

def closest2(L):
    '''
    Return the two closest values in a given list.

    >>> closest2([ 15.1,-12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)

    >>> closest2([1, 2, 4, 6, -9])
    (1, 2)

    >>> closest2([1])
    (None, None)
    '''
    if len(L) < 2:
        return (None, None)
    L2 = L.copy()
    L2.sort()
    distance = abs(L2[0]-L2[1])
    x = L2[0]
    y = L2[1]
    for i in range(len(L2) - 1):
        if abs(L2[i] - L2[i+1]) < distance:
            x = L2[i]
            y = L2[i+1]
            distance = abs(x-y)
    return (x, y)
    

if __name__ == "__main__":
    L1 = []
    for i in range(100000):
        L1.append(random.uniform(0.0, 1000.0))
    start_time = time.time()
    closest1 = closest1(L1)
    end_time = time.time()
    print("Time for closest1: {}".format(end_time - start_time))
    start_time = time.time()
    closest2 = closest2(L1)
    end_time = time.time()
    print("Time for closest2: {}".format(end_time - start_time))
    print()
    
    
    
    
    