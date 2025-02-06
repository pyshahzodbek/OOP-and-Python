#20.01.2025
# 9-dars
#Mavzu: if elif else
# yosh=int(input('Yoshingiz nechida?'))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m.')
# else:
#     print('Sizga kirish 10000.')
# yosh=int(input('Yoshingiz nechida?'))
# if yosh<=4:
#     narh=0
# elif yosh<=12:
#     narh=5000
# else:
#     narh=10000
# print(f"Sizga kirish {narh}so'm.")
# kun =input('Bugun qaysi kun?>>>')
# if kun.lower()=='shanba'or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni.')
#
# kun =input('Bugun nima kun?')
# harorat=float(input('Havo harorati qanday?'))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print('Chumilgani ketdik!')
# elif kun.lower()=='yakshanba'and harorat<30:
#     print("Uyda dam olamiz")
# kun = input('Bugun nima kun?')
# harorat = float(input('Havo harorati qanday?'))
# if (kun.lower()=='yakshanba'or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani ketdik.")
# elif  (kun.lower()=='shanba'or kun.lower()=='yakshanba')and harorat<30:
#     print('Uyda dam olamiz!!!')
# else:
#     print('Ish kuni bugun.')
# narh =15000 # mijoz 15000 so'mga taom oldi
# choy=True # mijoz choy ham oldi
# salat=False # mijoz salat olmadi
#
#
# if choy and salat:  # agar mijoz choy ham salat ham olgan bo'lsa
#     narh=narh+10000 #  narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh=narh+5000   # narhga 5000 so'm qo'shamiz
# print(f'Jami {narh}so\'m ') # Yakuniy narhni chiqaramiz
# narh=15000
# choy=True
# salat=False
# non= True
# kompot=True
# assorti=False
# if choy:
#     print('Mijoz choy oldi.')
#     narh=narh+3000
# if salat:
#     print('Mijoz salat oldi.')
#     narh=narh+5000
# if non:
#     print('Mijoz non oldi.')
#     narh=narh+2000
# if kompot:
#     print('Mijoz kompot oldi')
#     narh=narh+5000
# if assorti:
#     print('Mijoz assorti oldi.')
#     narh=narh+15000
# print(f'Jami {narh}so\'m.')
# menu =['osh','qozonkabob','shashlik','norin','somsa']
# print('manti' in menu)
# menu =['osh','qozonkabob','shashlik','norin','somsa']
# ovqat=input('Nima ovqat yeysiz?>>>')
# if ovqat.lower()in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#   print('Afsuski bizada bunday ovqat yo\'q')
# menu =['osh','qozonkabob','shashlik','norin','somsa']
# print('manti'not in menu)
#
# menu =['osh','qozonkabob','shashlik','norin','somsa']
# buyurtmalar=['osh','somsa','manti','shashlik']
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#   for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menuda {taom } bor')
#     else:
#         print(f'kechirasiz , menuda {taom} yo\'q')
# else:
#     print("Savatchangiz bo'sh!")
#1

# a= float(input('Birinchi sonni kiriting:'))
# b=float(input('Ikkinchi sonni kiriting:'))
# if a==b:
#     print(a,"=",b)
# elif a<b:
#     print(f'{a}<{b}')
# else:
#     print(f"{a}>{b}")
#
# mahsulotlar=['anor','kartoshka','sabzi','coca cola','uzum','shaftoli','olma','tarvuz']
# savat=[]
# for n in range(5):
#     savat.append(input(f'savatga {n+1}-mahsulotni qo\'shing'))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Do\'konimizda {mahsulot } bor')
#     else:
#         print(f'Do\'konimizda {mahsulot} yo\'q')
#
# foydalanuvchilar=['Ahmad','Ali','Vali','Anavar','Shahzod']
# login=input('Yangi login kiriting:')
# if login in foydalanuvchilar :
#     print("Login band, yangi login tanlang")
# else:
#     print('xush kelibsiz',login.title())
# son=int(input("Istalgan butun sonni kiriting:"))
# for n in range(2,11):
#     if not son%(n):
#         print(f'{son} soni {n} ga qoldiqsiz bulinadi')
#
# mahsulot=[]
# for n in range(5):
#   mahsulot.append(input(f'{n+1}-savatga mahsulot qo\'shing:'))
#   print(mahsulot)
# bor_mahsulotlar=['un','yog\'','go\'sht','anor','tarvuz','kartoshka','sabzi']
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat=[]
for n in range(5):
    savat.append(input(f'Savatga{n+1}-mahsultni kiriting: '))
bor_mahsulotlar=[]
yoq_mahsulotlar=[]
for i in savat:
    if i in mahsulotlar:
        bor_mahsulotlar.append(i)
    else:
        yoq_mahsulotlar.append(i)
for j in yoq_mahsulotlar:
        print(j)
if yoq_mahsulotlar:
    print(f'Do\'konimizda quyidagi mahsulot yo\'q')
else:
    print("Siz suragan barcha mahsulotlar bor")





