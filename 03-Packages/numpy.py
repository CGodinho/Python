###############################################################################
# Numpy examples
###############################################################################
import numpy as np


###############################################################################
#                      C R E A T I O N
###############################################################################
# creating a 4x5 matrix
matrix = np.arange(20).reshape(4, 5)

# identity matrix
np.identity(10)

# filled with unique value
np.full((3, 3), 2)

# From array and using booleans
np.array([[True, True, False, False], [ False, True, False, True]])


###############################################################################
#                          D E T A I L S
###############################################################################
# size
matrix.shape

# dump
matrix

# pretty print
print(matrix)


###############################################################################
#                       A G G R E G A T I O N
###############################################################################
# sum columns
matrix.sum(axis = 0)

# sum lines
matrix.sum(axis = 1)

# the mean of all elements
matrix.mean()

# the mean of all elements
matrix.max()


###############################################################################
#                   R E S H A P E   and   I N D E X I N G
###############################################################################
# reshape
matrix.reshape(5,4)

# get an element
matrix[2,3]

# subsetting
matrix[1:3, 2:4]

# Iterating
for row in matrix:
    print(row)

# List of elements
matrix.tolist()

###############################################################################
#            B A S I C   A R I T H M E T I C
###############################################################################
# applied toevery element
matrix + 1
matrix * 2


