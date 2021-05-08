def prime(num):
  
  if(num==0 or num ==1 ):
    return False
  elif(num==2):
    return True
  
  else:
    for i in range(2,int(num/2)+1):
      if(num%i==0):
        return False
  return True
def primefactor(num):
  liste=[]
  temp=num
  while(temp!=1):
    for i in range(2,int(num/2)+1):
      if(temp%i==0):
        liste.append(i)
        temp/=i
        break
  return(list(set(liste)))
num=int(input("The number;\n? "))
if(prime(num)):
  print("Number of positive integers not greater than m and relatively prime to m =>{}".format(num-1))
else:
  primes=primefactor(num)
  result=num
  for i in primes:
    result*=(1-1/i)
  result=int(result)
  print("Number of positive integers not greater than m and relatively prime to m =>{}".format(result))
