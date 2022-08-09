import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: string indentifier of table where record originates from
    # value: order_id
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: key
    # value: order_id
    orderId = list_of_values[0]
    line_items = list_of_values[1:]
    for l in line_items:
        mr.emit(orderId + l)

if __name__ == '__main__':
  data = open(sys.argv[1])
  mr.execute(data, mapper, reducer)