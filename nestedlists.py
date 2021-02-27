Solvation of https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    nested1=[]
    nestedscore=[]
    nestedname=[]
    nested2=[]
    nested3=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested1.append([name,score])
        nestedname.append(name)
        nestedscore.append(score)
        sozluk[name]=score
    nestedscore.sort()
    m=min(nestedscore)
    while(m==min(nestedscore)):
        nestedscore.remove(m)
        if(min(nestedscore)!=m):
            break
    m2=min(nestedscore)
    
    for i in nestedscore:
        if(i==m2):
            nested2.append(i)
    
    for i in nested1:
        if(i[1]==nested2[0]):
            nested3.append(i[0])
    nested3.sort()
    for i in nested3:
        print(i)
    
