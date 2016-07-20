def x(n):
  if n == 1:
    sum = term = 1 
    return (sum, term)
  else:
    sum,term = x(n-1)
    term = (sum*2)+1
    sum = sum+term
    return (sum,term)


