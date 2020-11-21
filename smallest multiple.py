number=1
while True:
    for i in range(1,21):
        if number % i !=0:

            number*=i
    break
print(number)