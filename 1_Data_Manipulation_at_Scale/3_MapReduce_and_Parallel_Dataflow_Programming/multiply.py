import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence id
    # value: string of nucleotides
    m = record[0]
    r = record[1]
    c = record[2]
    v = record[3]

    if m=="a":
        for i in range(0, 5):
            mr.emit_intermediate((r, i), [m, c, v])
    else:
        for j in range(0, 5):
            mr.emit_intermediate((j, c), [m, r, v])

def reducer(key, value):
    # key: sequence of id
    # value: string of nucleotides without 10 last letters
    a_v = filter(lambda cell: cell[0]=="a", value)
    b_v = filter(lambda cell: cell[0]=="b", value)

    a_s = set(map(lambda s:s[1], a_v))
    b_s = set(map(lambda s: s[1], b_v))
    a_b_s = a_s & b_s

    b_r = filter(lambda row:row[1] in a_b_s, b_v)
    a_c = filter(lambda row:row[1] in a_b_s, a_v)

    a_b_m = map(lambda x: x[0][2] * x[1][2], zip(b_r, a_c))
    mr.emit((key[0], key[1], sum(a_b_m)))

if __name__ == '__main__':
  data = open(sys.argv[1])
  mr.execute(data, mapper, reducer)