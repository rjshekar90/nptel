
#List comprehension
#Pythagorean Triplets
#a2 + b2 = c2


#Gives duplicates

#print [(x,y,z) for x in range(100) for y in range(100)
#  for z in range(100) if (x*x + y*y == z*z) ]


#y starts from x, y > x
#z starts from y, z > y > x
#Avoids duplicates
# Inner generators can be dependent on outer generators.


print [(x,y,z) for x in range(100) for y in range(x,100)
  for z in range(y,100) if (x*x + y*y == z*z) ]
