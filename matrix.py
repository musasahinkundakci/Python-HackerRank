import time
a=[[1,-1,2,4],
[1,0,1,6],
[2,-3,5,4],
[3,2,-1,1],
]


print("There are some operations and with them you can obtain a row echolon form or reduce echelon form.The thing is what you need make the operations due to that.")
while True:
  b=input("""
  The operations you can make:
  1:Interchange two rows
  2:Multiply a column with a nonzero number 
  3:Add a multiple of one equation to another
  4:See the matrix of final version 
  5:See what are the values of m*n
  """)
  print("İşleminiz gerçekleşiyor...")
  time.sleep(1)
  
  if b=="1":
    c=int(input("Please choose the first column you wanna interchange: "))
    d=int(input("Please choose the second column you wanna interchange with first one: "))
    a[c-1],a[d-1]=a[d-1],a[c-1]    
  
  
  elif b=="2":
    c=int(input("Which column do you wanna multiply: "))-1
    d=int(input("Which number do you wanna multiply with: "))
    liste=[]
    for i in a[c]:
      i*=d
      liste.append(i)
    a[c]=liste
    
    
  
  
  
  elif b=="3":
    x=int(input("Choose a column for adding to another one"))-1
    y=int(input("which column do you wanna add to: "))-1
    z=int(input("Which value do you pick for multiply"))
    listex=[]
    listey=a[y]
    for i in a[x]:
      i*=z
      listex.append(i)
    for i in range(4):
      listey[i]+=listex[i]
    a[y]=listey


  
  elif b=="4":
    for x,y,z,d in a:
      print("""
      | {} {} {} {} |
      """.format(x,y,z,d),end="")
      
