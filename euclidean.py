print("With euclidean algorithm.\n","Give me two number");
a,b=input().split()
a=int(a)
b=int(b)
while(1):
  i=1
  while(b*(i+1)<=a):
    i+=1
  r=a-b*i
  if(r==0):
    print(b)
    break
  a=b
  b=r

