#              x  y  z
coordinates = (1, 2, 3)
stuff = [4, 5, 6]

'''
One might do the following to avoid using the long variable name
coordinates everytime elements need to be accessed.
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

The following is called unpacking and does the exact same thing as
the lines above.
'''

x, y, z = coordinates
print(x, y, z)

a, b, c = stuff
print(a, b, c)