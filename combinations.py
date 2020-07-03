def combinations(n,l):
  if n==1:
    return [[i] for i in l]
  else:
    send=[]
    for i in range(len(l)):
      possible = combinations(n-1,l[i+1:])
      for b in range(len(possible)):
        possible[b].append(l[i])
      send+=possible
    return send

#checks if there are duplicates and prints the amount of combinations present
def dup(collect):
  print('len of list is: '+ str(len(collect)))
  check = [set(i) for i in collect]
  for i in check:
    if check.count(i)>1:
      return True
    else:
      return False
