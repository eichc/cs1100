'''
Author: Cam

Calculate a runner's skew, minimum, maximum, and average given 5 running times.
'''
def calcSkew(t1, t2, t3, t4, t5):
    '''
    Calculate the skew given 5 running times.
    '''
    avg = (t1 + t2 + t3 + t4 + t5) / 5
    var = (t1-avg)**2 + (t2-avg)**2 + (t3-avg)**2 + (t4-avg)**2 + (t5-avg)**2
    var /= 5
    skew = (t1-avg)**3 + (t2-avg)**3 + (t3-avg)**3 + (t4-avg)**3 + (t5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew

def stats(name, t1, t2, t3, t4, t5):
    '''
    Calculate min, max, and average given 5 times.
    '''
    minimum = min(t1, t2, t3, t4, t5)
    maximum = max(t1, t2, t3, t4, t5)
    total = t1 + t2 + t3 + t4 + t5
    avg = (total - minimum - maximum) / 3
    print("{}'s stats-- min: {}, max: {}, avg: {:.1f}".format(name, minimum, maximum, avg))

#calculate each person's skew
name_1 = "Stan"
stanSkew = calcSkew(34, 34, 35, 31, 29)
name_2 = "Kyle"
kyleSkew = calcSkew(30, 31, 29, 29, 28)
name_3 = "Cartman"
cartmanSkew = calcSkew(36, 31, 32, 33, 33)
name_4 = "Kenny"
kennySkew = calcSkew(33, 32, 34, 31, 35)
name_5 = "Bebe"
bebeSkew = calcSkew(27, 29, 29, 28, 30)

#print the skews
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,stanSkew))
print ("{0}'s running times have a skew of {1:.2f}".format(name_2,kyleSkew))
print ("{0}'s running times have a skew of {1:.2f}".format(name_3,cartmanSkew))
print ("{0}'s running times have a skew of {1:.2f}".format(name_4,kennySkew))
print ("{0}'s running times have a skew of {1:.2f}".format(name_5,bebeSkew))

#print the stats
print("")
stats(name_1, 34, 34, 35, 31, 29)
stats(name_2, 30, 31, 29, 29, 28)
stats(name_3, 36, 31, 32, 33, 33)
stats(name_4, 33, 32, 34, 31, 35)
stats(name_5, 27, 29, 29, 28, 30)