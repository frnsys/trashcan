import math
from trashcan.option import Option
from trashcan.person import Person


class Transportation(Option):
    pass

transit = {
    'subway': Transportation(convenience=lambda w: 2 if w['subway_delay'] else 5, money_cost=2, nonmoney_cost=3),
    'taxi': Transportation(convenience=7.5, money_cost=6, nonmoney_cost=1.5),
    'walk': Transportation(convenience=2, money_cost=0, nonmoney_cost=1),
    'swim': Transportation(convenience=0, money_cost=0, nonmoney_cost=9),
}

person = Person({
    'convenience': lambda v,s,w: 4*v,
    'money_cost': lambda v,s,w: -((10/(max(1, s['cash']-v)))**2),
    'nonmoney_cost': lambda v,s,w: -(math.e ** v/4),
    'pleasantness': lambda v,s,w: v
}, {'cash': 0})

worlds = [{
    'subway_delay': True
}, {
    'subway_delay': False
}]

states = [{
    'cash': 100
}, {
    'cash': 5
}]

for world in worlds:
    print('world:', world)
    for state in states:
        print('  state:', state)
        person.state = state
        for transport_name, transport in transit.items():
            score = person.evaluate(transport, world)
            print('    ', transport_name, ':', score)
