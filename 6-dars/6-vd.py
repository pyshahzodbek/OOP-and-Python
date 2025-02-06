# 18.01.2025
#6-Dars
# Mavzu: Ro'yxatni tartiblash
cars=['bmw', 'ferari','lasetti','cobalt','gentra']
cars.sort()# Tartiblaydi
print(cars)
cars.sort(reverse=True) # Teskari tartiblaydi
print(cars)
mehmonlar=['Ozod','Otabek','Dilshod','Ulug\'bek']
print('sorted() chiqargan ro\'yxat:',sorted(mehmonlar))
print('Asl ruyxat uzgarmas qoldi:',mehmonlar)
print(sorted(mehmonlar,reverse=True)) #sorted() funktsiyasi yordamida teskari tartiblash uchun ham
# reverse=True argumentini beramiz:
sonlar=[12,15,-6,-14,66,47]
sonlar.sort()
print(sonlar)
print(sorted(sonlar,reverse=True))
fruits=['pear','banana','apple','watermelon','lemon']
fruits.reverse() #Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga)
# talab qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
print(fruits)
print('Ruyxat uzunligi:',len(fruits))# # len(fruits) ro'yxat uzunligini qaytaradi

sonlar=list(range(0,10)) #Yuqoridagi misolda range(0,10) funktsiyasi
# 0 dan 9 gacha sonlar ketma-ketligini shakllantirdi, list(range(0,9)) esa
# bu ketma-ketlikni ro'yxatga aylantirdi.
print(sonlar)
juft_sonlar=list(range(0,12,2))
Toq_sonlar=list(range(1,12,2))
print("Juft sonlar:",juft_sonlar) # 0 dan 20 gacha 2 qadam bilan
print('Toq sonlar:',Toq_sonlar) # 1 dan 20 gacha 2 qadam bilan
narhlar=[12000,5600,89000,36000,2400,]
Arzon=min(narhlar)
Qimmat=max(narhlar)
jami=sum(narhlar)
print(f'Eng qimmat narx: {Qimmat} , eng arzon {Arzon}')
print('Jami:',jami)
cars=['bmw','lasetti','cobalt','nexia 3','damas']
my_cars=cars[0:3]
print(my_cars)
print(cars[2:5])  # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(cars[:5])  # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
sonlar=[1,78,5,-7,45,6,0.5]
sonlar2=sonlar
sonlar2.append(45) # sonlar2 ga 45 sonini qo'shamiz
sonlar2.append(-78)
print(sonlar2)
print(sonlar)
sonlar=[1,78,5,-7,45,6,0.5]
sonlar2=sonlar[:]
sonlar2.append(2)
sonlar2.append(-89)
print('Bu sonlar2 ro\'yxati',sonlar2)
print('Bu sonlar ro\'yxat',sonlar)
toys=('Bear','car' ,'bus','snake')
print(toys)
toys=list(toys)
toys.append('dragon')
print(toys)
toys.remove('bus')
del toys[1]
print(toys)
toys[1]='mcquen'
toys=tuple(toys)
print(toys)
print(type(toys))
#Amaliy mashg'ulot
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=['O\'zbekiston','Xitoy','Tojikiston','Qirg\'iziston']
print('Davlatlar ro\'yxati',davlatlar)
#Ro'yxatning uzunligini konsolga chiqaring
print('Ro\'yxat uzunligi:',len(davlatlar))
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))
print(davlatlar)
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print('Teskari tartib',sorted(davlatlar,reverse=True))
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
sonlar=list(range(120,1200,2))
y=sum(sonlar)
print(sonlar)
print('yig\'indisi',y)
katta=max(sonlar)
kichik=min(sonlar)
print('kattasidan kichigini ayirmasi:',katta-kichik)
print('Ro\'yxat uzunligi:',len(sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])
taomlar=['osh','manti','sho\'rva','mastava','qozonkabob']
print(taomlar)
nonushta=taomlar[:]
print(nonushta)
print(taomlar)
nonushta.append('Katlet')
nonushta.append('Qovurdoq')
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
print(type(nonushta))
