## Sets And Tuples Exercises

#stap 1
tags = {'python', 'bash', 'git', 'python'}
print(tags)
print(len(tags))

#stap 2
tags.add('linux')
print(tags)

#stap 3
#tags.remove('bash')
tags.discard("bash")
print(tags)
tags.discard("bash")
print(tags)

#stap 4
a = {1, 2, 3}
b = {3, 4, 5}
together = a.union(b)
print(together)

shared = a.intersection(b)
print(shared)