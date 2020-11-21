try:
    a=int(input("Bir sayı gir: "))
except ValueError:
    print("Integer deger giriniz!")
asalmı=True
largestone=int()
while True:
    for i in range(2,int(a/2)+1):
        if i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%11==0 and i%13==0 and i%17==0 and i%19==0:
            continue
        else:
            if a % i==0:
                for j in range(2,int(i/2)+1):
                    if i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%11==0 and i%13==0 and i%17==0 and i%19==0:
                        asalmı=False
                        break
                    elif i%j==0:
                        asalmı=False
                        break
                if asalmı==True:
                    largestone=i
    break
print(largestone)

