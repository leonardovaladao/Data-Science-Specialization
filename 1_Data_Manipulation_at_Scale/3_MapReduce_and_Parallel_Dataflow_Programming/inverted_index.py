import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document ID
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of docs
    l = list(set(list_of_values))
    mr.emit((key, l))

if __name__ == '__main__':
  data = open(sys.argv[1])
  mr.execute(data, mapper, reducer)