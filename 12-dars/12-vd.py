# 23.01.2025
# 12-dars
# Mavzu:Lug'at bilan ishlash .
# .items() metodi
talaba_0 = {
    'ism': 'alijon',
    'familya': 'shamshiyev',
    'fakultet': 'matematika',
    'kurs': '4'
}
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat}\n")
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310'
}
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
# .keys() metodi
mahsulotlar = {
    'olma': '10000',
    'anor': '20000',
    'uzum': '40000',
    'anjir': '25000',
    'shaftoli': '30000'
}
# print(mahsulotlar.keys())
# print("do'konimizda mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
bozorlik = ['anor', 'uzum', 'non''baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm.")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#     print("Do'konimizdagi mahsulot:")
#     for mahsulot in sorted(mahsulotlar):
#         print(mahsulot.title())
# .values() metodi
# print(telefonlar.values())
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
# telefonlar={
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawe p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
# }
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)
# Amaliy mashg'ulot
# py={
#     'Boolean':'Mantiqiy qiymat',
#     'float':'O\'nlik son',
#     'For':'Biror amalni qayta-qayta bajarish tsikli',
#     'If':"SHartni tekshirish operatori",
#     'Integer':'Butun son',
#     'Values':'Lug\'at qiymatini chiqaradi',
#     'Title':'Bosh harflarini katta qiladi',
#     'Lower':'Bosh harfni kichik qiladi',
#     'Len':"Listdagi ro'yxat uzunligini chiqaradi",
#     'Else':"SHart tekshirish operatori"
# }
# print(py.items())
# for k,q in sorted(py.items()):
# #     print(k,"-",q)
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# print('Dunyo davlatlari:')
# for i in sorted(davlatlar.keys()):
#     print(i.upper())
# print("\nDavlatlarning poytaxti:")
# for i in sorted(davlatlar.values()):
#     print(i.title())
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# i = davlatlar.get(country)
# if i==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# else:
#     print(f"{country.upper()}ning poytaxti {i.title()} shahri")

taomlar = {
    'manti': 15000,
    "xonim": 15000,
    'somsa': 9000,
    'lavash': 30000,
    'gamburger': 25000,
    'sho\'rva': 18000,
    'osh': 25000,
    'mastava': 20000
}

#
buyurtma = []
for i in range(1, 4):
    a = input(f"{i}-taomni kiriting: ").lower()  # Taomlarni kichik harfda solishtirish uchun
    b = taomlar.get(a)  # Kiritilgan taom uchun qiymatni olish
    if b:  # Agar `b` qiymat mavjud bo'lsa (ya'ni None bo'lmasa)
        buyurtma.append(b)
    else:
        print(f"Kechirasiz, bizda {a} yo'q.")
print("Buyurtmangiz qiymatlari:", buyurtma)

#
# for j in buyurtma:
#     if j in taomlar:
#         print(f"Taom {j} {taomlar[j]}")
#     else:
#         print(f"{j} --- bu taom bizda yo'q")
# print('3 ta taom buyurtma bering.')
# a=input("1-taom:")
# b=input('2-taom:')
# c=input('3-taom:')
# i=taomlar.get(a)
# j=taomlar.get(b)
# h=taomlar.get(c)
#
# if i==None:
#     print(f"Kechirasiz, bizda {a} yo'q")
# if j==None:
#     print(f"Kechirasiz, bizda {b} yo'q")
# if h==None:
#  print(f"Kechirasiz, bizda {c} yo'q")
# else:
#  print(f'{a}-{i}\n{b}-{j}\n{c}-{h}')
#  print('3 ta taom buyurtma qiling.')

# buyurtmalar=[]
# for n in range(3):
#      buyurtmalar.append(input(f"{n+1}-taom:").lower())
# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"{buyurtma.title()} {taomlar[buyurtma]}so'm")
#     else:
#         print(f'Kechirasiz, bizda {buyurtma} yo\'q')


