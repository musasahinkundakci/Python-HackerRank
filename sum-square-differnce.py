öncekare=0
sonrakare=0
for i in range(1,101):
    öncekare=i**2+öncekare
    sonrakare+=i
sonrakare=sonrakare**2

print(""""
/*************/
İlk yüz doğal sayının karelerinin toplamı: {}

İlk yüz doğal sayının toplamının karesi :{}

İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı :{}
/*************/
""".format(öncekare,sonrakare,sonrakare-öncekare))

