def lar(k,l):
  l=list(set(l))
  l.sort(reverse=True)
  print(l[k-1])