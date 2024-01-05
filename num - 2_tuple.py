# Tuples using this method
tup1 = (100,"b",True,"c",False)

# types
print(type(tup1))

# num values
print(tup1[0])
print(tup1[1])
print(tup1[-1])
print(tup1[1:3])
print(tup1[2])

# length
print(len(tup1))

# concatinating tuple
tup1 = (1,2,3)
tup2=(4,5,6)
print(tup1+tup2)

# repeating tuple elements
tup1 = ("poorna",300)
print(tup1*3)

# repeating & concatinating
tup1 = ("poorna",300)
tup2 = (4,5,6)
print(tup1*3 + tup2)

# Tuple functions min & max value
tup1 = (1,2,3,4,5)
print(min(tup1))
print(max(tup1))
