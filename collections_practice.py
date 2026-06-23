# ## Sets And Tuples Exercises

# #stap 1
# tags = {'python', 'bash', 'git', 'python'}
# print(tags)
# print(len(tags))

# #stap 2
# tags.add('linux')
# print(tags)

# #stap 3
# #tags.remove('bash')
# tags.discard("bash")
# print(tags)
# tags.discard("bash")
# print(tags)

# #stap 4
# a = {1, 2, 3}
# b = {3, 4, 5}
# together = a.union(b)
# print(together)

# shared = a.intersection(b)
# print(shared)

# difference = a.difference(b)
# print(difference)
# difference = b.difference(a)
# print(difference)

# #stap 5

# print(True) if "git" in tags else print(False)

# #stap 6
# point = (10, 20)
# print(point)
# print(point[:1:])
# print(point[1:])

# #stap 7
# #point[0]=99
# #print(point)#TypeError: 'tuple' object does not support item assignment

# #stap8
# rgb = (255, 128, 0)
# r = rgb[0]
# print(r)
# g = rgb[1]
# print(g)
# b = rgb[2]
# print(b)

# #stap 9
# coords = (1, 2, 3, 2, 1)
# print(coords.count(2))
# print(coords.index(3))

# #stap 10
# list=(1,2,3)
# set=(1,2,3)
# tuple=(1,2,3)
# print(list)
# print(set)
# print(tuple)
#Only in the list can the values ​​be changed.

##Part 2 — Optional Advanced Basics
#stap 1
a = {1, 2, 3}
b = {3, 4, 5}
x = a.issubset(b)
print(x)
z = b.issubset(a)
print(z)
# print(a.issubset(b))
# print(a. issuperset(b))

#stap 2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(pairs[1])
