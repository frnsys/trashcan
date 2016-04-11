import math


class Item(Option):
    pass


state = {}
food = Item(cost=10, nutrition=10)

person = Person('David', {
    'nutrition': lambda v, s: v/2 if not s['hungry'] else 2*v,
    'cost': lambda v, s: -v/2
}, {'hungry': False})




mop_the_floor = 100 # square feet
mop_per_minute = 1 # square feet


donatello   = Person('Donatello')
leonardo    = Person('Leonardo')
rafael      = Person('Rafael')
michael     = Person('Michaelangelo')
shredder    = Person('Shredder')

tmnt = [donatello, leonardo, rafael, michael]
for t in tmnt:
    relate(shredder, t, Relationship.professional)
    authority(shredder, t, 10)

print(social_network.edges(data=True))
print(authority_network.edges(data=True))


# print(person.evaluate(food, state))


# class Transportation(Option):
    # pass

# transit = {
    # 'subway': Transportation(convenience=5, mcost=2, ncost=3, pleasantness=3),
    # 'taxi': Transportation(convenience=7.5, mcost=6, ncost=1.5, pleasantness=5),
    # 'walk': Transportation(convenience=2, mcost=0, ncost=1, pleasantness=lambda s: 6.5 if s['nice_out'] else -1),
    # 'swim': Transportation(convenience=0, mcost=0, ncost=9, pleasantness=1),
# }

# state = {
    # 'nice_out': True
# }

# eamon = Person('Eamon', {
    # 'convenience': lambda x: 4*x,
    # 'mcost': lambda x: -(x**2),
    # 'ncost': lambda x: -(math.e ** x/4),
    # 'pleasantness': lambda x: x,
    obedience: -10
# })

# for transport_name, transport in transit.items():
    # print(transport_name)
    # print(eamon.evaluate(transport, state))