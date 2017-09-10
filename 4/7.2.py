
#generators useful for init lists
# 4 * 3 matrix
# 4 rows and 3 columns
# stored row-wise
#Always init using generators. best way

l = [ [ 1 for i in range(3)]
    for j in range(4)]

print l
