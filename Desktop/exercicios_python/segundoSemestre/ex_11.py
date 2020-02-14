from randint import random
def intercala (tup1, tup2):
  for i in range (random.randint(1,3)):
      tup3 = ()
      tup3 += tup1[i]
      i += 1
      tup3 += tup2
      i += 1
    return tup3



