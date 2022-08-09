import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: friendA
    # value: 1
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: friendA
    # value: sum of friends
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

if __name__ == '__main__':
  data = open(sys.argv[1])
  mr.execute(data, mapper, reducer)