from DataProcessor import DataProcessor
from data.input import data
filters = [
    ('weight', '=', 3),
    ('width', '>', 2),
]

order = 'DESC'


processor = DataProcessor(filters, order)
result = processor.process(data)

print(result)