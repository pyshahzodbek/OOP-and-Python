# 27.01.2025
# 15-dars
# Mavzu: While, ro'yxatlar va lug'atlar
# ismlar =[]
# print('Yaqin do\'stlaringiz ro\'yxatini tuzamiz.')
# n=1 # # ismlarni sanash uchun o'zgaruvch
# while True:
#     savol=f"{n}- do'stingiz ismini kiriting:"
#     ism= input(savol)
#     ismlar.append(ism)
#     javob =input('Yana ism qo\'shasizmi?(ha/yo\'q)')
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora =True
# while ishora:
#     ism =input("Do'stning ismini kiriting: ")
#     yosh=input(f"{ism.title()} yoshini kiriting: ")
#     dostlar[ism]=int(yosh) # ism kalit, yosh qiymat
#     javob=input("Yana ism qo'shasizmi?(ha/yo'q)")
#     if javob=='yo\'q':
#        ishora= False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()}  {yosh} yoshda.")
# cars=['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars:  # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia')  # nexia ni ro'yxatdan olib tashla
# print(cars)
# talabalar=['hasan','husan','olim','botir']
# baholamgan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning baholami kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholamgan_talabalar[talaba]=baho
# print(baholamgan_talabalar)
# Amaliyot
# buyurtma=[]
# print('Buyurtmalar qabul qiluvchi dastur.')
# while True:
#     buyurtma.append(input('Buyurtmangizni kiriting: '))
#     javob=input('Yana buyurtmangizni kiriting? (ha/yo\'q)')
#     if javob=='ha':
#         continue
#     else:
#         break
# print(buyurtma )
print("e-bozor mahsulotlari")
e_bozor = {}
while True:
    mahsulot = input("Mahsulotni kiriting:")
    narxi = int(input("Narxini kiriting:"))
    e_bozor[mahsulot] = narxi
    javob = input("Yana mahsulotni kiriting? (ha/yo'q)")
    if javob=='ha':
        continue
    else:
        break
print(e_bozor)
buyurtma = []
print('Buyurtmalar qabul qiluvchi dastur.')
while True:
    buyurtma.append(input('Buyurtmangizni kiriting: '))
    javob = input('Yana buyurtmangizni kiriting? (ha/yo\'q)')
    if javob == 'ha':
        continue
    else:
        break
for i in buyurtma:
    if i in e_bozor:
        narxi = e_bozor[i]
        print(f"{i} mahsulotni e-bozordagi narxi {narxi}so'm")
    else:
        print(f"Bizda {i}bu mahsulot yo'q")
