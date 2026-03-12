from FilteringEngine import FilterEngine
from PrioritySorter import PrioritySorter
from data.input import data
filters = [
    ('weight', '=', 3),
    ('width', '>', 2),
]

order = 'DESC'

filter_engine = FilterEngine(filters)
sorter = PrioritySorter(order)
result = sorter.sort(data, filter_engine)

print(result)