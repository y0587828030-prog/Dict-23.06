#stap 1
agent = {'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
#stap 2
print(agent["name"])

#stap 3
# level = agent.get("level")
# print(level)

print(agent.get("level"))
print(agent.get("0"))
# print(agent["0"])

#stap4
agent["score"]= 95
print(agent)

#stap 5
agent["level"]=5
print(agent)

#stap 6
del(agent["active"])
print(agent)

#stap 7
keys = agent.keys()
print(keys)

values = agent.values()
print(values)

items = agent.items()
print(items)
