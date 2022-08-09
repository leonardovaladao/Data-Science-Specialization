import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence id
    # value: string of nucleotides
    key = record[0]
    value = record[1]
    trimmed = value[:len(value)-10]
    mr.emit_intermediate(trimmed, 1)

def reducer(key, value):
    # key: sequence of id
    # value: string of nucleotides without 10 last letters
    mr.emit(key)


if __name__ == '__main__':
  data = open(sys.argv[1])
  mr.execute(data, mapper, reducer)