def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  
    

def sum_for_list(lst):
    count = {}
    res = []

    absl = map(abs, lst)

    for i in range(2, max(absl)):
        for num in lst:
            if num % i == 0:
                if is_prime(i):
                    if i in count.keys():
                        count[i].append(num)
                    else:
                        count.update({i:[num]})
    for fact in count:

        arc = map(abs, count[fact])
        if fact != max(arc):
            res.append([fact, sum(count[fact])])
    print(count)
    return sorted(res, key=lambda x: x[0])

print(sum_for_list([81, -96, -49, -198, -65, 199, -134, -75, -157, -177, 69, -145, -114]))