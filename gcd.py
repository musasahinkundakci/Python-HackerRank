def gcd(a,b):
  if(a<b):
    a,b=b,a
    while(b!=0):
      r=a%b
      a=b
      b=r
    return a
print(gcd(12,24))
def gcd2(a,b):
  if(b==0):
    return a
  else:
    return gcd(b,a%b)
print(gcd(363,12))
