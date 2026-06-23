
##Part 1 — Basics: dict CRUD, keys, values, items
#stap 1
# agent = {'name': 'Alpha', 'level': 3, 'active': True}
# print(agent)
# #stap 2
# print(agent["name"])

# #stap 3
# # level = agent.get("level")
# # print(level)

# print(agent.get("level"))
# print(agent.get("0"))
# # print(agent["0"])

# #stap4
# agent["score"]= 95
# print(agent)

# #stap 5
# agent["level"]=5
# print(agent)

# #stap 6
# del(agent["active"])
# print(agent)

# #stap 7
# keys = agent.keys()
# print(keys)

# values = agent.values()
# print(values)

# items = agent.items()
# print(items)

# #stap 8
# if "score" in agent:
#  print("True")

#  #stap 9
# scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
# print(scores)
# A_winning_agent = max(scores, key=scores.get)
# print(A_winning_agent)
# #print(max(scores.values()))



# #stap 10
# copy_agent = agent.copy()
# print(copy_agent)

# copy_agent["name"]= "yehoshua"
# print(copy_agent)
# print(agent)

# OPart 2 — Optional Advanced Basics

#stap 1
config ={}
print(config)
# new_key = config.setdefault("timeout" , 30)
# print(new_key)
config.setdefault("timeout" , 30)
print(config)
config.setdefault("timeout" , 40)
print(config)

#stap 2
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = d1 | d2 
print(d3)

#stap 3
d1.pop("a")
print(d1)
# d1.pop("1")
# print(d1)

#stap 4
nested = {'server': {'host': 'localhost', 'port': 8080}}
print(nested["server"]["port"])