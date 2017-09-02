def a(val,ll = []):
  ll.append(val)
  return ll

l1 = a(1)
l2 = a(2,[])
l3 = a(3)
print l1
print l2
print l3


def multipliers():
  return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]

