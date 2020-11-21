enbüyük=dict()
number=int()
for i in range (100,1000):
    for j in range(100,1000):
        if str(i*j) == str(i*j)[::-1] and number<i*j:
            number=i*j
            enbüyük={"i":i,"j":j,"i*j":i*j}
print("""
/*************/
i:{}
j:{}
i*j:{}
/*************/
""".format(enbüyük["i"],enbüyük["j"],number))