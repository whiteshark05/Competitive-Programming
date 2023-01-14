import itertools
for x,y,z in itertools.product([True, False],repeat=3):
    if (x and y or z) != (x and (y or z)): print(x,y,z)