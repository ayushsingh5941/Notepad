import numpy as np
list1 = [0, 1, 2, 3, 4]
# Numpy array
arid = np.array(list1)
''' numpy arrays are designed to handle vectorized operation python list not, array size can not be increased once defined although list size can be increased using append'''
print(arid)
# adding in array is easy example: adding 2 to each element
print(arid+2)

''' Lets create a 2d array '''
list2 = [[1,1, 1], [2,2,2], [3,3,3]]
arr2d = np.array(list2)
print(arr2d)
print(arr2d.dtype)
# converting dtype to float
arr2d = np.array(list2, dtype='float')
print(arr2d.dtype)
#converting again in integer, simmilarly to string


'''Another diffrence in list and array'''
# we can enter multiple datatype in list whereas numpy array can only be a single datatype

'''Converting Numpy array in list'''

np2list = arr2d.tolist()
print(np2list)
# simmliary to string and bytes, helpful in communication protocal for data recieving and data transfer


'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

'''How to inspect size and shape of numpy array'''
print('array shape', arr2d.shape)
#size
print(arr2d.size)
print('size : ',arid.size)
# dimension
print('dimension : ',arr2d.ndim)

'''Extracting specific item from array'''

# by indexing
print('Extracting by index', arid[0])
# for 2-d array [r][c]
print('2d array extracting', arr2d[2][1])

#selecting some number with condition boolean indexing

boolarr = arr2d < 3
print(boolarr)
print(arr2d[boolarr])

''' row interchange andReverse the rows and columns in array'''
print('Before reversing', arr2d)
print(arr2d[::-1])
# transposing rows to columns
print('Transpose',arr2d[::-1, ::-1])


''' represinting infinity numbers in numnpy'''
print(np.nan) # null not a number
print(np.inf) #infinity stats operation cannot done on nan and inf

#How to insert or manipulate number in numpy array
arr2d[0][0] = np.nan
arr2d[0][1] = np.inf
print(arr2d) # mean of col1 and col2 can't be calculated
# np.isnan to check nan in array
print(np.isnan(arr2d).sum())
print(np.isinf(arr2d))
# replacing nan and inf
missing_flag = np.isnan(arr2d) | np.isinf(arr2d)
print(missing_flag)
arr2d[missing_flag] = 0
print('nan and inf are replaced to 0',arr2d)



'''Compute statistical operations on numpy array'''

# find mean, s.d, variance e.t.c
print('Mean : ',arr2d.mean())
print('max', arr2d.max())
print('Min  : ', arr2d.min())
print('Sd : ', arr2d.std())
print('variance : ', arr2d.var())
print('squeeze', arr2d.squeeze())
# cummulative su,m adding no. by no.
print('Cumulative sum : ',arr2d.cumsum())

'''Creating an array from existing array'''

arr = arr2d[:2,:2]
print(arr)

# Reshaping, converting 3X3 in some other form
print(arr2d.reshape(1,9)) # single row multiple columns
print(arr2d.reshape(9,1)) # single column multiple rows

# flatten the array when we don't know size or shape of array (single dim array)
print('Flatten:',arr2d.flatten()) # copy of arr2d
# ravel changes will affect parent whereas changes will not affect flatten
print('Ravel', arr2d.ravel()) # refrence of arr2d

'''Create a sequence, repetition, and random number'''
# to genatare nyumpy array
print(np.arange(1,5, dtype='int')) # it will include 1 but not 5
# another example with gap more than 1
print(np.arange(1,50,2)) # LAST ARGS DEFINE HOW MANY ELEMNTS

#linespcae
print('Line space', np.linspace(1, 50, 2))
print('Line space', np.linspace(1, 50, 100))

#logspace

print('Log space', np.logspace(1, 50, 10))

#np.zeros
print(np.zeros([2,2]))
#np.ones
print(np.ones([3,3]))



a = [1, 2, 3]
print('Repeat: ',np.tile(a, 3)) # repeating a list
#np.repeat
print(np.repeat(a, 3))
print(np.repeat(arr2d,3))

# generating a random number
print('Random of size 3',np.random.rand(3)) # dimension of array in argument
print('Random of size 3x3',np.random.rand(3,3))

#uniformly distributed random no.
print(np.random.randn(3,3))
# random no. of integer
print(np.random.randint(0,10, [3,3])) #[] defines dimesnion of number



'''How we can get unique items and counts'''
#unique numbers
print('Unique ',np.unique(arr2d))
#count
uniques, counts = np.unique(arr2d, return_counts=True)
print('Uni',uniques)
print('count', counts)










































