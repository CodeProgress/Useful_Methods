import collections

# iterating over key and value in a dict
x = {x:x**3 for x in range(10)}

for key, value in x.iteritems():
    print key, value

# flip dict
y = {value: key for key, value in x.iteritems()}

print x, y
# Named tuples
Point3D = collections.namedtuple('Point', ['x', 'y', 'z'])
start = Point3D(x=0, y=0 , z=0)
end = Point3D(x=1, y=1, z=1)
